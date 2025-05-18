from ui.pages.leadforms_page import LeadformsPage
from ui.pages.audiences_page import AudiencesPage
from ui.pages.commerce_page import CommercePage
from ui.pages.campaign_page import CampaignPage

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import pathlib

import time

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
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
    elif browser == 'firefox':
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
def campaign_page(driver):
    driver.get(CampaignPage.url)
    return CampaignPage(driver=driver)

@pytest.fixture
def leadforms_page(driver): 
    return LeadformsPage(driver=driver)

@pytest.fixture
def audiences_page(driver):
    driver.get(AudiencesPage.url)
    return AudiencesPage(driver=driver)
  
@pytest.fixture
def commerce_page(driver): 
    return CommercePage(driver=driver)

@pytest.fixture
def prepare_audience(audiences_page):
    audience_name = f"Test Audience {int(time.time())}"
    audiences_page.create_audience(audience_name)
    yield audience_name

@pytest.fixture
def cleanup_all_audiences(audiences_page):
    yield
    if audiences_page.has_audiences():
        audiences_page.delete_all_audiences()    
