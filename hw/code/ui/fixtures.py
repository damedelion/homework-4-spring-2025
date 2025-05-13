from ui.pages.feed_page import FeedPage
from ui.pages.audiences_page import AudiencesPage

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

import pathlib


@pytest.fixture()
def driver(config, request):
    browser = config['browser']
    url = config['url']
    selenoid = config['selenoid']
    vnc = config['vnc']
    options = Options()
    if selenoid:
        capabilities = {
            'browserName': 'chrome',
            'version': '118.0',
        }
        if vnc:
            capabilities['enableVNC'] = True
        driver = webdriver.Remote(
            'http://127.0.0.1:4444/wd/hub',
            options=options,
            desired_capabilities=capabilities
        )
    elif browser == 'chrome':
        options.add_argument('user-data-dir=vkads-userdata')
        options.add_argument('profile-directory=vkads-profile')
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
    elif browser == 'firefox':
        service = Service(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service, options=options)
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)
    else:
        raise RuntimeError(f'unsupported browser: "{browser}"')
    
    driver.get(url)
    driver.maximize_window()

    yield driver
    
    driver.quit()


def get_driver(browser_name):
    if browser_name == 'chrome':
        browser = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    elif browser_name == 'firefox':
        browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    else:
        raise RuntimeError(f'unsupported browser: "{browser_name}"')
    browser.maximize_window()
    return browser


@pytest.fixture(scope='session', params=['chrome', 'firefox'])
def all_drivers(config, request):
    url = config['url']
    browser = get_driver(request.param)
    browser.get(url)
    yield browser
    browser.quit()


@pytest.fixture
def feed_page(driver):
    return FeedPage(driver=driver)


@pytest.fixture
def audiences_page(driver): 
    return AudiencesPage(driver=driver)
