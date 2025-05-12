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

        
    
