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
    return AudiencesPage(driver=driver)
  
@pytest.fixture
def commerce_page(driver): 
    return CommercePage(driver=driver)

@pytest.fixture
def cleanup_campaign(campaign_page):
    yield
    campaign_page.choose_option('Удалить')
    assert campaign_page.check_no_campaigns()

@pytest.fixture
def cleanup_campaign(campaign_page):
    yield
    campaign_page.choose_option('Удалить')

@pytest.fixture
def prepare_campaign(campaign_page):
    url = "https://github.com/damedelion/homework-4-spring-2025"
    budget = "123"
    title = "Test title"
    desc = "Test description"
    new_name = "Test campaign"

    campaign_page.click_create_btn()
    campaign_page.change_name(new_name)
    campaign_page.click_site_field()
    campaign_page.fill_site_url_field(url)
    campaign_page.click_budget_field()
    campaign_page.fill_budget_field(budget)
    campaign_page.choose_date()

    campaign_page.click_continue_btn()
    campaign_page.choose_region()
    campaign_page.click_continue_btn()

    campaign_page.fill_ad_title(title)
    campaign_page.fill_ad_short_desc(desc)
    campaign_page.choose_default_media()
    campaign_page.wait_media_generation()
    campaign_page.click_submit_btn()
