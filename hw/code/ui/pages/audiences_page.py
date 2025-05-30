from selenium.webdriver.common.keys import Keys
from ui.pages.base_page import BasePage
from ui.locators.audiences_page_locators import AudiencesPageLocators
from ui.pages.base_url import VKADS_BASE_URL
from selenium.common.exceptions import NoSuchElementException


class AudiencesPage(BasePage):
    url = f'{VKADS_BASE_URL}/hq/audience'

    # ===== КОМПОЗИТНЫЕ МЕТОДЫ ДЛЯ SETUP И TEARDOWN =======

    def create_audience(self, name):
        self.click_create_audience_button()
        self.enter_audience_name(name)
        self.add_mobile_app_category_source()
        self.save_audience()
    
    def add_mobile_app_category_source(self):
        source = "Категории мобильного приложения"
        category_option = "Бизнес"
        self.click_add_source_button()
        self.click_category_link(source)
        self.select_category_option(category_option)
        self.confirm_source_selection(source)

    def delete_audience(self, audience_name):
        row = self.get_audience_row(audience_name)
        self.select_audience_checkbox(row)
        self.click_navbar_delete_button()
        self.confirm_deletion_in_dialog()
        self.wait_for_audience_disappear(audience_name)

    def delete_all_audiences(self):
        checkbox_label = self.find(AudiencesPageLocators.ALL_AUDIENCES_CHECKBOX)
        if (not self.is_checkbox_checked(checkbox_label)):
            checkbox_label.click()
        self.click(AudiencesPageLocators.NAVBAR_DELETE_BUTTON)
        self.wait_until_visible(AudiencesPageLocators.CONFIRM_DELETE_AUDIENCE_BUTTON)
        self.click(AudiencesPageLocators.CONFIRM_DELETE_AUDIENCE_BUTTON)
        self.wait_until_invisible(AudiencesPageLocators.AUDIENCE_IN_LIST_CHECKBOX_LOCATOR)

    # ========== СОЗДАНИЕ АУДИТОРИИ ==========

    def click_create_audience_button(self):
        self.click(AudiencesPageLocators.CREATE_AUDIENCE_BUTTON)

    def click_add_source_button(self):
        self.click(AudiencesPageLocators.ADD_SOURCE_BUTTON)
    
    def select_category_option(self, option):
        self.click(AudiencesPageLocators.CATEGORY_SELECTOR)
        self.click(AudiencesPageLocators.CATEGORY_OPTION(option))
    
    def confirm_source_selection(self, source):
        self.click(AudiencesPageLocators.SELECT_SOURCE_BUTTON(source))
        self.wait_until_invisible(AudiencesPageLocators.SOURCE_MODAL_OVERLAY(source))
    
    def save_audience(self):
        self.click(self.SAVE_BUTTON)

    def enter_audience_name(self, name):
        name_input = self.find(AudiencesPageLocators.CREATE_AUDIENCE_NAME_INPUT)
        name_input.clear()
        name_input.send_keys(name)
    
    def save_audience(self):
        self.click(AudiencesPageLocators.CREATE_AUDIENCE_SAVE_BUTTON)
        self.wait_to_disappear(AudiencesPageLocators.CREATE_AUDIENCE_MODAL_OVERLAY)

    # ========== УПРАВЛЕНИЕ АУДИТОРИЕЙ ==========

    def is_checkbox_checked(self, checkbox_container):
        try:
            checkbox_on_icon = checkbox_container.find_element(*AudiencesPageLocators.AUDIENCE_IN_LIST_CHECKBOX_LOCATOR_ON)
            return checkbox_on_icon.is_displayed()
        except NoSuchElementException:
            return False

    def get_audience_row(self, audience_name):
        rows = self.find_elements(AudiencesPageLocators.AUDIENCE_ROW)
        for row in rows:
            try:
                name_element = row.find_element(*AudiencesPageLocators.REL_AUDIENCE_NAME_IN_ROW(audience_name))
                if name_element.text == audience_name:
                    return row
            except NoSuchElementException:
                continue
        return None

    def wait_until_invisible_row(self, audience_name):
        self.wait_until_invisible(AudiencesPageLocators.ABS_AUDIENCE_NAME_IN_ROW(audience_name))
        
    def select_audience_checkbox(self, row_element):
        checkbox_label = row_element.find_element(*AudiencesPageLocators.AUDIENCE_IN_LIST_CHECKBOX_LOCATOR)
        if (not self.is_checkbox_checked(checkbox_label)):
            checkbox_label.click()
    
    def click_navbar_delete_button(self):
        self.click(AudiencesPageLocators.NAVBAR_DELETE_BUTTON)
    
    def confirm_deletion_in_dialog(self):
        self.wait_until_visible(AudiencesPageLocators.CONFIRM_DELETE_AUDIENCE_BUTTON)
        self.click(AudiencesPageLocators.CONFIRM_DELETE_AUDIENCE_BUTTON)
    
    def wait_for_audience_disappear(self, audience_name):
        self.wait_until_invisible(AudiencesPageLocators.ABS_AUDIENCE_NAME_IN_ROW(audience_name))      

    def hover_navbar_delete_button(self):
        self.hover(AudiencesPageLocators.NAVBAR_DELETE_BUTTON)

    def input_create_audience_name(self, name):
        self.input_text(AudiencesPageLocators.CREATE_AUDIENCE_NAME_INPUT, name)

    # ========== НАВБАР: КЕБАБ ==========

    def click_kebab_menu(self):
        self.click(AudiencesPageLocators.KEBAB_MENU)

    # ========== НАВБАР: ШЕРИНГ / ДОСТУП ==========

    def click_navbar_share_button(self):
        self.click(AudiencesPageLocators.NAVBAR_SHARE_BUTTON)

    def select_public_key_radio(self):
        self.click(AudiencesPageLocators.SHARE_PUBLIC_KEY_RADIO)

    def click_share_settings_save_button(self):
        self.click(AudiencesPageLocators.SHARE_SETTINGS_SAVE_BUTTON)

    def wait_for_share_window_to_close(self):
        self.wait_to_disappear(AudiencesPageLocators.SHARE_SETTINGS_WINDOW)

    def get_sharing_link_text(self):
        return self.find(AudiencesPageLocators.SHARING_LINK).text

    def close_share_link_window(self):
        self.click(AudiencesPageLocators.SHARE_LINK_WINDOW_CLOSE_BUTTON)

    def hover_navbar_share_button(self):
        self.hover(AudiencesPageLocators.NAVBAR_SHARE_BUTTON)

    # ========== НАВБАР: ФИЛЬТРАЦИЯ И ПОИСК ==========

    def click_navbar_filter_button(self):
        self.click(AudiencesPageLocators.NAVBAR_FILTER_BUTTON)

    def click_filter_option(self, option):
        self.click(AudiencesPageLocators.FILTER_OPTION(option))

    def click_apply_filter_button(self):
        self.click(AudiencesPageLocators.APPLY_FILTER_BUTTON)

    def clear_filters(self):
        self.click(AudiencesPageLocators.FILTER_CLEAR_BUTTON)

    def clear_search(self):
        self.click(AudiencesPageLocators.SEARCH_CLEAR_BUTTON)

    def input_text(self, locator, text):
        elem = self.find(locator)
        elem.clear()
        elem.send_keys(text)

    def input_navbar_search(self, search_query):
        self.input_text(AudiencesPageLocators.NAVBAR_SEARCH_INPUT, search_query)

    # ========== РАБОТА С ИСТОЧНИКАМИ ==========

    def click_add_source_button(self):
        self.click(AudiencesPageLocators.CREATE_AUDIENCE_ADD_SOURCE_BUTTON)

    def click_exclude_source_button(self):
        self.click(AudiencesPageLocators.CREATE_AUDIENCE_EXCLUDE_SOURCE_BUTTON)

    def click_category_link(self, source):
        self.click(AudiencesPageLocators.CATEGORY_LINK(source))

    # ========== ВСПОМОГАТЕЛЬНЫЕ МЕТОДЫ ==========

    def has_audiences(self):
        return self.is_visible(AudiencesPageLocators.AUDIENCE_ITEM)

    def get_hint_tooltip_message(self):
        return self.find(AudiencesPageLocators.HINT_TOOLTIP).text

    def get_error_message(self):
        return self.find(AudiencesPageLocators.ERROR_MESSAGE).text

    def get_error_description(self):
        return self.find(AudiencesPageLocators.ERROR_DESCRIPTION).text

    def get_actions_text(self):
        return [button.text for button in self.find_elements(AudiencesPageLocators.ACTION_BUTTON)]

    def get_content_layout_text(self):
        return self.find(AudiencesPageLocators.CONTENT_LAYOUT).text
