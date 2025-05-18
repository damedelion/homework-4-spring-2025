from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from ui.pages.base_page import BasePage
from ui.pages.base_url import VKADS_BASE_URL

from ui.locators.campaign_locators import CampaignLocators


class CampaignPage(BasePage):
    url = f"{VKADS_BASE_URL}/hq/dashboard"

    # Common
    def wait_redirect(self, redirect_url, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.url_contains(redirect_url))

    def wait_displayed(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def wait_input(self, locator, input_text, timeout=10):
        by, value = locator
        WebDriverWait(self.driver, timeout).until(
            lambda d: d.find_element(by, value).get_attribute("value").replace('\xa0', ' ') == input_text
        )

    def get_error_message(self):
        return self.find(CampaignLocators.ERROR_MESSAGE).text

    def click_continue_btn(self):
        self.click(CampaignLocators.CONTINUE_BTN)

    def click_submit_btn(self):
        self.click(CampaignLocators.SUBMIT_BTN)

    def click_cancel_btn(self):
        self.click(CampaignLocators.CANCEL_BTN)

    def change_name(self, name):
        self.click(CampaignLocators.CHANGE_NAME_BTN)
        name_field = self.find(CampaignLocators.CHANGE_NAME_FIELD)
        name_field.send_keys(name)
        self.click(CampaignLocators.CHANGE_NAME_ACCEPT)

    def get_name(self):
        return self.find(CampaignLocators.CHANGE_NAME_BTN).text

    # Functions for create campaign
    def click_create_btn(self):
        self.click(CampaignLocators.CREATE_BTN)

    def click_site_field(self):
        self.click(CampaignLocators.SITE_FIELD)

    def fill_site_url_field(self, url):
        site_field = self.find(CampaignLocators.SITE_URL_FIELD)
        site_field.clear()
        site_field.send_keys(url + Keys.RETURN)

    def wait_displayed_budget(self):
        self.wait_displayed(CampaignLocators.SITE_BUDGET)

    def click_budget_field(self):
        self.click(CampaignLocators.SITE_BUDGET)

    def fill_budget_field(self, budget):
        budget_field = self.find(CampaignLocators.SITE_BUDGET_INPUT)
        budget_field.clear()
        budget_field.send_keys(budget + Keys.RETURN)
        self.wait_input(CampaignLocators.SITE_BUDGET_INPUT, f"{budget} ₽")

    def choose_date(self):
        self.wait_displayed(CampaignLocators.END_DATE_FIELD)
        self.click(CampaignLocators.END_DATE_FIELD)
        self.wait_displayed(CampaignLocators.FIRST_AVAILABLE_DATE)
        self.click(CampaignLocators.FIRST_AVAILABLE_DATE)

    def choose_region(self):
        self.click(CampaignLocators.GROUP_REGION)

    def fill_ad_title(self, title):
        ad_title = self.find(CampaignLocators.AD_TITLE_INPUT)
        ad_title.clear()
        ad_title.send_keys(title)

    def fill_ad_short_desc(self, desc):
        ad_short_desc = self.find(CampaignLocators.AD_SHORT_DESCRIPTION_INPUT)
        ad_short_desc.clear()
        ad_short_desc.send_keys(desc)

    def choose_default_media(self):
        self.click(CampaignLocators.AD_MEDIA_BTN)
        self.click(CampaignLocators.AD_MEDIA_SITES_BTN)
        self.click(CampaignLocators.AD_MEDIA_SITES_IMG)
        self.wait_displayed(CampaignLocators.AD_MEDIA_ADD_BTN)
        self.click(CampaignLocators.AD_MEDIA_ADD_BTN)

    def choose_option(self, option):
        self.click(CampaignLocators.CAMPAIGNS_TABLE_CHECKBOX)
        self.click(CampaignLocators.CAMPAIGNS_TABLE_ACTIONS)
        self.click(CampaignLocators.CAMPAIGNS_TABLE_CHOOSE_OPTIONS(option))

    def campaign_main_page_text(self):
        self.wait_displayed(CampaignLocators.NO_ACTIVE_CAMPAIGNS_LABEL)
        return self.find(CampaignLocators.NO_ACTIVE_CAMPAIGNS_LABEL).text

    def wait_media_generation(self):
        self.wait_displayed(CampaignLocators.VIDEO_CONTAINER)