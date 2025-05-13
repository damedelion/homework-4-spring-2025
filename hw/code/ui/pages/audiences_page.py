from selenium.webdriver.common.keys import Keys
from ui.pages.base_page import BasePage
from ui.locators.audiences_page_locators import AudiencesPageLocators
from ui.pages.base_url import VKADS_BASE_URL
from selenium.common.exceptions import NoSuchElementException


class AudiencesPage(BasePage):
    locators = AudiencesPageLocators()
    url = f'{VKADS_BASE_URL}/hq/audience'

    # ========== СОЗДАНИЕ АУДИТОРИИ ==========

    def open_create_audience_menu(self):
        self.click_create_audience_button()

    def click_create_audience_button(self):
        self.click(self.locators.CREATE_AUDIENCE_BUTTON)

    def is_create_audience_menu_opened(self):
        return self.is_visible(self.locators.CREATE_AUDIENCE_MENU_TITLE)

    def enter_audience_name(self, name):
        name_input = self.find(self.locators.CREATE_AUDIENCE_NAME_INPUT)
        name_input.clear()
        name_input.send_keys(name)
        return self

    def add_mobile_app_category_source(self):
        self.click_add_source_button()

        self.click_mobile_app_category_link()

        self.click(self.locators.CATEGORY_SELECTOR)
        self.click(self.locators.BUSINESS_CATEGORY_OPTION)

        self.click(self.locators.SELECT_SOURCE_BUTTON)

        return self

    def create_audience(self, name):
        self.open_create_audience_menu()
        self.enter_audience_name(name)
        self.add_mobile_app_category_source()
        self.wait_to_disappear(self.locators.SOURCE_MODAL_OVERLAY)
        self.save_audience()
        self.wait_to_disappear(self.locators.CREATE_AUDIENCE_MODAL_OVERLAY)
        return self

    def save_audience(self):
        self.click(self.locators.CREATE_AUDIENCE_SAVE_BUTTON)

    # ========== УПРАВЛЕНИЕ АУДИТОРИЕЙ ==========

    def is_checkbox_checked(self, checkbox_container):
        try:
            checkbox_on_icon = checkbox_container.find_element(*self.locators.AUDIENCE_IN_LIST_CHECKBOX_LOCATOR_ON)
            return checkbox_on_icon.is_displayed()
        except NoSuchElementException:
            return False

    def is_audience_present(self, audience_name):
        rows = self.find_elements(self.locators.AUDIENCE_ROW)
        for row in rows:
            try:
                name_element = row.find_element(*self.locators.REL_AUDIENCE_NAME_IN_ROW(audience_name))
                if name_element.text.strip() == audience_name:
                    return True
            except NoSuchElementException:
                continue
        return False

    def get_audience_row(self, audience_name):
        rows = self.find_elements(self.locators.AUDIENCE_ROW)
        for row in rows:
            try:
                name_element = row.find_element(*self.locators.REL_AUDIENCE_NAME_IN_ROW(audience_name))
                if name_element.text == audience_name:
                    return row
            except NoSuchElementException:
                continue
        raise NoSuchElementException

    def delete_audience(self, audience_name):
        if not self.is_audience_present(audience_name):
            return True

        row = self.get_audience_row(audience_name)
        checkbox_label = row.find_element(*self.locators.AUDIENCE_IN_LIST_CHECKBOX_LOCATOR)
        if (not self.is_checkbox_checked(checkbox_label)):
            self.click_element(checkbox_label)

        self.click(self.locators.NAVBAR_DELETE_BUTTON)
        self.wait_until_visible(self.locators.CONFIRM_DELETE_AUDIENCE_BUTTON)
        self.click(self.locators.CONFIRM_DELETE_AUDIENCE_BUTTON)
        self.wait_until_invisible(self.locators.ABS_AUDIENCE_NAME_IN_ROW(audience_name))

    def hover_navbar_delete_button(self):
        self.hover(self.locators.NAVBAR_DELETE_BUTTON)

    def is_visible_delete_hint(self):
        return self.is_visible(self.locators.DELETE_HINT_TOOLTIP)

    # ========== UI ПРОВЕРКИ ==========

    def is_empty_state_ui_correct(self):
        return (self.is_visible(self.locators.EMPTY_STATE_MESSAGE) and
                self.is_visible(self.locators.CREATE_AUDIENCE_BUTTON) and
                self.is_visible(self.locators.KEBAB_MENU) and
                self.is_visible(self.locators.HOW_AUDIENCES_WORK_LINK))

    def check_kebab_menu_options_empty_state(self):
        self.click(self.locators.KEBAB_MENU)
        return (self.is_visible(self.locators.ACTIVATE_EXTERNAL_AUDIENCE_OPTION) and
                self.is_visible(self.locators.TRANSFER_VK_AUDIENCE_OPTION))

    def is_navbar_ui_correct(self):
        return (self.is_visible(self.locators.NAVBAR) and
                self.is_visible(self.locators.CREATE_AUDIENCE_BUTTON) and
                self.is_visible(self.locators.NAVBAR_KEBAB_MENU) and
                self.is_visible(self.locators.NAVBAR_FILTER_BUTTON) and
                self.is_visible(self.locators.NAVBAR_SHARE_BUTTON) and
                self.is_visible(self.locators.NAVBAR_DELETE_BUTTON) and
                self.is_visible(self.locators.NAVBAR_SEARCH_INPUT))

    def is_audience_list_ui_correct(self):
        return (self.is_visible(self.locators.AUDIENCE_LIST) and
                self.is_visible(self.locators.AUDIENCE_NAME_COLUMN) and
                self.is_visible(self.locators.AUDIENCE_REACH_COLUMN))

    def is_create_audience_menu_ui_correct(self):
        return (self.is_visible(self.locators.CREATE_AUDIENCE_MENU_TITLE) and
                self.is_visible(self.locators.CREATE_AUDIENCE_NAME_INPUT) and
                self.is_visible(self.locators.CREATE_AUDIENCE_ADD_SOURCE_BUTTON) and
                self.is_visible(self.locators.CREATE_AUDIENCE_EXCLUDE_SOURCE_BUTTON))

    def is_add_source_menu_ui_correct(self):
        return (self.is_visible(self.locators.ADD_SOURCE_MENU_TITLE) and
                self.is_visible(self.locators.MY_AUDIENCES_SECTION) and
                self.is_visible(self.locators.MOBILE_APP_CATEGORY_LINK))

    def is_exclude_source_menu_ui_correct(self):
        return (self.is_visible(self.locators.EXCLUDE_SOURCE_MENU_TITLE) and
                self.is_visible(self.locators.MY_AUDIENCES_SECTION) and
                self.is_visible(self.locators.MOBILE_APP_CATEGORY_LINK))

    # ========== ШЕРИНГ / ДОСТУП ==========

    def share_audience(self):
        self.click(self.locators.AUDIENCE_IN_LIST_CHECKBOX_LOCATOR)
        self.click(self.locators.NAVBAR_SHARE_BUTTON)
        self.click(self.locators.SHARE_PUBLIC_KEY_RADIO)
        self.click(self.locators.SHARE_SETTINGS_SAVE_BUTTON)
        self.wait_to_disappear(self.locators.SHARE_SETTINGS_WINDOW)

    def is_share_link_present(self):
        return self.is_present(self.locators.SHARING_LINK)

    def close_share_link_window(self):
        self.click(self.locators.SHARE_LINK_WINDOW_CLOSE_BUTTON)

    def hover_navbar_share_button(self):
        self.hover(self.locators.NAVBAR_SHARE_BUTTON)

    def is_visible_share_hint(self):
        return self.is_visible(self.locators.SHARE_HINT_TOOLTIP)

    # ========== ФИЛЬТРАЦИЯ И ПОИСК ==========

    def check_filter_functionality(self):
        self.click(self.locators.NAVBAR_FILTER_BUTTON)
        self.click(self.locators.FIRST_FILTER_OPTION)
        self.click(self.locators.APPLY_FILTER_BUTTON)
        return self.is_visible(self.locators.ACTIVE_FILTER_TAG)

    def clear_filters(self):
        self.click(self.locators.FILTER_CLEAR_BUTTON)

    def clear_search(self):
        self.click(self.locators.SEARCH_CLEAR_BUTTON)

    def input_text(self, locator, text):
        elem = self.find(locator)
        elem.clear()
        elem.send_keys(text)

    def check_search_functionality(self, search_query):
        self.input_text(self.locators.NAVBAR_SEARCH_INPUT, search_query)
        return self.is_visible(self.locators.SEARCH_RESULTS)

    def check_search_empty_result(self, search_query):
        self.input_text(self.locators.NAVBAR_SEARCH_INPUT, search_query)
        return self.is_visible(self.locators.EMPTY_SEARCH_RESULT)

    def check_search_validation(self):
        search_query = "a" * 256
        self.input_text(self.locators.NAVBAR_SEARCH_INPUT, search_query)
        return self.is_visible(self.locators.SEARCH_INPUT_ERROR_HINT_TOOLTIP)

    # ========== РАБОТА С ИСТОЧНИКАМИ ==========

    def click_add_source_button(self):
        self.click(self.locators.CREATE_AUDIENCE_ADD_SOURCE_BUTTON)

    def is_add_source_menu_opened(self):
        return self.is_visible(self.locators.ADD_SOURCE_MENU_TITLE)

    def click_exclude_source_button(self):
        self.click(self.locators.CREATE_AUDIENCE_EXCLUDE_SOURCE_BUTTON)

    def is_exclude_source_menu_opened(self):
        return self.is_visible(self.locators.EXCLUDE_SOURCE_MENU_TITLE)

    def open_add_source_menu(self):
        self.open_create_audience_menu()
        self.click_add_source_button()

    def open_exclude_source_menu(self):
        self.open_create_audience_menu()
        self.click_exclude_source_button()

    def click_mobile_app_category_link(self):
        self.click(self.locators.MOBILE_APP_CATEGORY_LINK)

    def is_source_menu_opened(self):
        return self.is_visible(self.locators.CREATE_AUDIENCE_MODAL_OVERLAY)

    def is_source_present(self, timeout=5):
        return self.is_present(self.locators.CREATE_AUDIENCE_ADDED_SOURCE_HEADER)

    def add_test_source(self):
        self.click_add_source_button()
        self.click_mobile_app_category_link()
        self.click(self.locators.CATEGORY_SELECTOR)
        self.click(self.locators.BUSINESS_CATEGORY_OPTION)
        self.click(self.locators.SELECT_SOURCE_BUTTON)
        self.wait_to_disappear(self.locators.SOURCE_MODAL_OVERLAY)

    def add_test_excluded_source(self):
        self.click_exclude_source_button()
        self.click_mobile_app_category_link()
        self.click(self.locators.CATEGORY_SELECTOR)
        self.click(self.locators.BUSINESS_CATEGORY_OPTION)
        self.click(self.locators.SELECT_SOURCE_BUTTON)
        self.wait_to_disappear(self.locators.SOURCE_MODAL_OVERLAY)

    def add_same_excluded_source(self):
        self.wait_to_disappear(self.locators.SOURCE_MODAL_OVERLAY)
        return self.add_test_excluded_source()

    def click_edit_source_button(self):
        self.click(self.locators.EDIT_SOURCE_BUTTON)

    def click_delete_source_button(self):
        self.click(self.locators.DELETE_SOURCE_BUTTON)

    def click_edit_excluded_source_button(self):
        self.click(self.locators.EDIT_EXCLUDED_SOURCE_BUTTON)

    def click_delete_excluded_source_button(self):
        self.click(self.locators.DELETE_EXCLUDED_SOURCE_BUTTON)

    def is_excluded_source_present(self):
        return self.is_visible(self.locators.ADDED_EXCLUDED_SOURCE)

    def is_same_source_error_visible(self):
        return self.is_visible(self.locators.SAME_SOURCE_ERROR)

    # ========== ВСПОМОГАТЕЛЬНЫЕ МЕТОДЫ ==========

    def has_audiences(self):
        return self.is_visible(self.locators.AUDIENCE_ITEM)

    def check_name_validation(self):
        long_name = "a" * 256
        self.input_text(self.locators.CREATE_AUDIENCE_NAME_INPUT, long_name)
        return self.is_visible(self.locators.CREATE_AUDIENCE_NAME_ERROR)
