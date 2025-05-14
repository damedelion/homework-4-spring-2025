import time

from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from ui.pages.base_page import BasePage
from ui.pages.base_url import VKADS_BASE_URL

from ui.locators.campaign_locators import CampaignLocators


class CampaignPage(BasePage):
    url = f"{VKADS_BASE_URL}/hq/dashboard"
    locators = CampaignLocators()

    # Common
    def wait_redirect(self, redirect_url, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.url_contains(redirect_url))

    def wait_displayed(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def get_error_message(self):
        return self.find(self.locators.ERROR_MESSAGE).text

    def click_continue_btn(self):
        self.click(self.locators.CONTINUE_BTN)

    def click_submit_btn(self):
        self.click(self.locators.SUBMIT_BTN)

    def click_cancel_btn(self):
        self.click(self.locators.CANCEL_BTN)

    def change_name(self, name):
        self.click(self.locators.CHANGE_NAME_BTN)
        name_field = self.find(self.locators.CHANGE_NAME_FIELD)
        name_field.send_keys(name)
        self.click(self.locators.CHANGE_NAME_ACCEPT)

    def get_name(self):
        return self.find(self.locators.CHANGE_NAME_BTN).text

    # Functions for create campaign
    def click_create_btn(self):
        self.click(self.locators.CREATE_BTN)

    def click_site_field(self):
        self.click(self.locators.SITE_FIELD)

    def fill_site_url_field(self, url):
        site_field = self.find(self.locators.SITE_URL_FIELD)
        site_field.clear()
        site_field.send_keys(url + Keys.RETURN)

    def wait_displayed_budget(self):
        self.wait_displayed(self.locators.SITE_BUDGET)

    def click_budget_field(self):
        self.click(self.locators.SITE_BUDGET)

    def fill_budget_field(self, budget):
        budget_field = self.find(self.locators.SITE_BUDGET_INPUT)
        budget_field.clear()
        budget_field.send_keys(budget + Keys.RETURN)

    def choose_region(self):
        self.click(self.locators.GROUP_REGION)

    def fill_ad_title(self, title):
        ad_title = self.find(self.locators.AD_TITLE_INPUT)
        ad_title.clear()
        ad_title.send_keys(title)

    def fill_ad_short_desc(self, desc):
        ad_short_desc = self.find(self.locators.AD_SHORT_DESCRIPTION_INPUT)
        ad_short_desc.clear()
        ad_short_desc.send_keys(desc)

    def choose_default_media(self):
        self.click(self.locators.AD_MEDIA_BTN)
        self.click(self.locators.AD_MEDIA_SITES_BTN)
        self.click(self.locators.AD_MEDIA_SITES_IMG)
        self.wait_displayed(self.locators.AD_MEDIA_ADD_BTN)
        self.click(self.locators.AD_MEDIA_ADD_BTN)

    def choose_option(self, option):
        self.click(self.locators.CAMPAIGNS_TABLE_CHECKBOX)
        self.click(self.locators.CAMPAIGNS_TABLE_ACTIONS)
        self.click(self.locators.CAMPAIGNS_TABLE_CHOOSE_OPTIONS(option))

    def check_no_campaigns(self):
        self.wait_displayed(self.locators.NO_ACTIVE_CAMPAIGNS_LABEL)
        txt = self.find(self.locators.NO_ACTIVE_CAMPAIGNS_LABEL).text
        return txt == 'Нет активных кампаний'