from ui.pages.base_url import VKADS_BASE_URL

from ui.pages.base_page import BasePage
from ui.locators.commerce_locators import CommerceLocators


class CommercePage(BasePage):
    url = f'{VKADS_BASE_URL}/hq/ecomm/catalogs'

    def click_create_catalog_button(self):
        self.click(CommerceLocators.CREATE_CATALOG_BUTTON)
    
    def create_catalog_header_exists(self):
        return self.find(CommerceLocators.NEW_CATALOG_HEADER)
    
    def click_start_onboarding_button(self):
        self.click(CommerceLocators.START_ONBOARDING_BUTTON)
    
    def select_onboarding_modal_exists(self):
        return self.find(CommerceLocators.SELECT_ONBOARDING_MODAL)

    def find_catalog_name_input(self):
        return self.find(CommerceLocators.CATALOG_NAME_INPUT)
    
    def submit_create_catalog_button(self):
        self.click(CommerceLocators.SUBMIT_CREATE_CATALOG_BUTTON)
    
    def find_required_field_error(self):
        return self.find(CommerceLocators.REQUIRED_FIELD_ERROR)
    
    def find_required_http_protocol_error(self):
        return self.find(CommerceLocators.REQUIRED_HTTP_PROTOCOL_ERROR)
    
    def find_invalid_url_error(self):
        return self.find(CommerceLocators.INVALID_URL_ERROR)
    
    def find_invalid_file_format_error(self):
        return self.find(CommerceLocators.INVALID_FILE_FORMAT_ERROR)

    def find_unsupported_marketplace_url_error(self):
        return self.find(CommerceLocators.UNSUPPORTED_MARKETPLACE_URL_ERROR)    

    def select_catalog_from_url(self):
        self.click(CommerceLocators.CATALOG_FROM_URL_SELECT)
    
    def find_catalog_from_url_select(self):
        return self.find(CommerceLocators.CATALOG_FROM_URL_SELECT)
    
    def select_catalog_from_marketplace(self):
        self.click(CommerceLocators.CATALOG_FROM_MARKETPLACE_SELECT)

    def select_catalog_from_file(self):
        self.click(CommerceLocators.CATALOG_FROM_FILE_SELECT)
    
    def find_catalog_from_url_input(self):
        return self.find(CommerceLocators.CATALOG_URL_INPUT)
    
    def find_catalog_from_marketplace_input(self):
        return self.find(CommerceLocators.CATALOG_MARKETPLACE_INPUT)

    def find_catalog_from_file_input(self):
        return self.find(CommerceLocators.CATALOG_FILE_INPUT)
    
    def find_catalog_tabs_history(self):
        return self.find(CommerceLocators.CATALOG_TABS_HISTORY)
    
    def close_create_catalog_modal(self):
        self.click(CommerceLocators.CLOSE_CREATE_CATALOG_MODAL_BUTTON)
    
    def cancel_create_catalog_modal(self):
        self.click(CommerceLocators.CANCEL_CREATE_CATALOG_MODAL_BUTTON)

    def find_catalog_url_auth_button(self):
        return self.find(CommerceLocators.CATALOG_URL_AUTH_BUTTON)
    
    def search_for_catalog(self, query):
        search_input = self.find(CommerceLocators.SEARCH_CATALOG_INPUT)
        search_input.send_keys(query)
        return search_input
    
    def find_search_results_table(self):
        return self.find(CommerceLocators.SEARCH_RESULTS_TABLE)
    
    def find_search_not_found_message(self):
        return self.find(CommerceLocators.SEARCH_NOT_FOUND_MESSAGE)
    
    def open_catalog(self, index):
        self.wait().until(
            lambda d: len(d.find_elements(*CommerceLocators.CATALOG_ROW)) > index
        )
        catalogs = self.driver.find_elements(*CommerceLocators.CATALOG_ROW)
        catalogs[index].click()

    def open_catalog_settings(self):
        self.click(CommerceLocators.CATALOG_SETTINGS_BUTTON)
    
    def find_catalog_settings_header(self):
        return self.find(CommerceLocators.CATALOG_SETTINGS_HEADER)
    
    def submit_catalog_settings(self):
        self.click(CommerceLocators.CATALOG_SETTINGS_SUBMIT_BUTTON)
    
    def delete_catalog_from_settings(self):
        self.click(CommerceLocators.CATALOG_SETTINGS_DELETE_BUTTON)
    
    def cancel_catalog_settings(self):
        self.click(CommerceLocators.CANCEL_CATALOG_SETTINGS_BUTTON)
    
    def fill_settings_catalog_name(self, name):
        name_input = self.find(CommerceLocators.CATALOG_SETTINGS_NAME_INPUT)
        name_input.clear()
        name_input.send_keys(name)
    
    def find_catalog_name(self):
        return self.find(CommerceLocators.CATALOG_NAME)
    
    def wait_catalog_name(self, name):
        self.wait().until(
            lambda d: name == self.find(CommerceLocators.CATALOG_NAME).text
        )
        return True
    
    def close_catalog_settings(self):
        self.click(CommerceLocators.CLOSE_CATALOG_SETTINGS_BUTTON)
    
    def cancel_catalog_settings(self):
        self.click(CommerceLocators.CANCEL_CATALOG_SETTINGS_BUTTON)
    
    def open_catalog_settings(self):
        self.click(CommerceLocators.TABLE_SETTINGS_BUTTON)
    
    def find_table_settings_header(self):
        return self.find(CommerceLocators.TABLE_SETTINGS_HEADER)
