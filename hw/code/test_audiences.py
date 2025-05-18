import pytest
import time

from base import BaseCase

from ui.locators.audiences_page_locators import AudiencesPageLocators

class TestAudiences(BaseCase):       
    
    # ========== Вкладка "Аудитории": пустое состояние ==========

    def test_empty_state_ui_elements(self, audiences_page):
        audiences_page.open()

        assert (
            audiences_page.is_visible(AudiencesPageLocators.HEADER("Аудиторий пока нет")) and
            audiences_page.is_visible(AudiencesPageLocators.CREATE_AUDIENCE_BUTTON) and
            audiences_page.is_visible(AudiencesPageLocators.KEBAB_MENU) and
            audiences_page.is_visible(AudiencesPageLocators.LINK("Как работают аудитории"))
        )

    def test_kebab_menu_options_empty_state(self, audiences_page):
        audiences_page.open()
        audiences_page.click_kebab_menu()

        expected_first_action_test = "Активировать внешнюю аудиторию"
        expected_second_action_text = "Перенести аудитории из кабинета ВКонтакте"
        options_text = audiences_page.get_actions_text()
        assert len(options_text) == 2
        got_first_action_test, got_second_action_text = options_text
        assert (
            got_first_action_test == expected_first_action_test and
            got_second_action_text == expected_second_action_text
        )

    # ========== Вкладка "Аудитории": при наличии аудиторий ==========

    def test_navbar_ui_with_audiences(self, audiences_page, prepare_audience, cleanup_all_audiences):
        audiences_page.open()

        assert (
            audiences_page.is_visible(AudiencesPageLocators.NAVBAR) and
            audiences_page.is_visible(AudiencesPageLocators.CREATE_AUDIENCE_BUTTON) and
            audiences_page.is_visible(AudiencesPageLocators.NAVBAR_KEBAB_MENU) and
            audiences_page.is_visible(AudiencesPageLocators.NAVBAR_FILTER_BUTTON) and
            audiences_page.is_visible(AudiencesPageLocators.NAVBAR_SHARE_BUTTON) and
            audiences_page.is_visible(AudiencesPageLocators.NAVBAR_DELETE_BUTTON) and
            audiences_page.is_visible(AudiencesPageLocators.NAVBAR_SEARCH_INPUT)
        )

    def test_audience_list_ui(self, audiences_page, prepare_audience, cleanup_all_audiences):
        audiences_page.open()

        assert (
            audiences_page.is_visible(AudiencesPageLocators.AUDIENCE_LIST) and
            audiences_page.is_visible(AudiencesPageLocators.AUDIENCE_NAME_COLUMN) and
            audiences_page.is_visible(AudiencesPageLocators.AUDIENCE_REACH_COLUMN)
        )

    def test_filter_functionality(self, audiences_page, prepare_audience, cleanup_all_audiences):
        audiences_page.open()

        audiences_page.click_navbar_filter_button()
        filter_option = "Слушатели музыкантов"
        audiences_page.click_filter_option(filter_option)

        audiences_page.click_apply_filter_button()

        audiences_page.wait_until_invisible_row(prepare_audience)
        content_layout_text = audiences_page.get_content_layout_text()

        audiences_page.clear_filters()

        assert "Ничего не нашлось" in content_layout_text

    def test_share_button_tooltip_without_selection(self, audiences_page, prepare_audience, cleanup_all_audiences):
        audiences_page.open()

        audiences_page.hover_navbar_share_button()

        share_hint_tooltip_message = "Выберите аудитории, которыми хотите поделиться"
        got_hint_tooltip_message = audiences_page.get_hint_tooltip_message()

        assert got_hint_tooltip_message == share_hint_tooltip_message

    def test_delete_button_tooltip_without_selection(self, audiences_page, prepare_audience, cleanup_all_audiences):
        audiences_page.open()

        audiences_page.hover_navbar_delete_button()

        delete_hint_tooltip_message = "Выберите аудитории, которые хотите удалить"
        got_hint_tooltip_message = audiences_page.get_hint_tooltip_message()

        assert got_hint_tooltip_message == delete_hint_tooltip_message

    def test_search_functionality(self, audiences_page, prepare_audience, cleanup_all_audiences):
        audiences_page.open()

        audiences_page.input_navbar_search(prepare_audience)

        audience_row = audiences_page.get_audience_row(prepare_audience)

        audiences_page.clear_search()

        assert audience_row

    def test_search_empty_results(self, audiences_page, prepare_audience, cleanup_all_audiences):
        audiences_page.open()

        audiences_page.input_navbar_search(int(time.time()))

        audiences_page.wait_until_invisible_row(prepare_audience)
        content_layout_text = audiences_page.get_content_layout_text()

        audiences_page.clear_search()

        assert "Ничего не нашлось" in content_layout_text

    def test_search_max_length_validation(self, audiences_page, prepare_audience, cleanup_all_audiences):
        audiences_page.open()

        audiences_page.input_navbar_search("a" * 256)

        search_input_error_hint_tooltip_message = "Максимальная длина 255 символов"
        got_hint_tooltip_message = audiences_page.get_hint_tooltip_message()

        audiences_page.clear_search()

        assert got_hint_tooltip_message == search_input_error_hint_tooltip_message

    # ========== Тесты меню создания аудитории ==========

    def test_create_audience_menu_ui(self, audiences_page):
        audiences_page.open()

        audiences_page.click_create_audience_button()

        assert (
            audiences_page.is_visible(AudiencesPageLocators.CREATE_AUDIENCE_MENU_TITLE) and
            audiences_page.is_visible(AudiencesPageLocators.CREATE_AUDIENCE_NAME_INPUT) and
            audiences_page.is_visible(AudiencesPageLocators.CREATE_AUDIENCE_ADD_SOURCE_BUTTON) and
            audiences_page.is_visible(AudiencesPageLocators.CREATE_AUDIENCE_EXCLUDE_SOURCE_BUTTON)
        )

    def test_create_audience(self, audiences_page, cleanup_all_audiences):
        audiences_page.open()

        audiences_page.click_create_audience_button()

        audience_name = f"Test Audience {int(time.time())}"
        audiences_page.enter_audience_name(audience_name)

        source = "Категории мобильного приложения"
        category_option = "Бизнес"

        audiences_page.click_add_source_button()
        audiences_page.click_category_link(source)
        audiences_page.select_category_option(category_option)
        audiences_page.confirm_source_selection(source)

        audiences_page.save_audience()

        audience_row = audiences_page.get_audience_row(audience_name)

        assert audience_row

    def test_delete_audience(self, audiences_page, prepare_audience, cleanup_all_audiences):
        audience_row = audiences_page.get_audience_row(prepare_audience)
        audiences_page.select_audience_checkbox(audience_row)

        audiences_page.click_navbar_delete_button()
        audiences_page.confirm_deletion_in_dialog()
        audiences_page.wait_for_audience_disappear(prepare_audience)

        content_layout_text = audiences_page.get_content_layout_text()

        assert "Аудиторий пока нет" in content_layout_text

    def test_audience_name_validation(self, audiences_page):
        audiences_page.open()

        audiences_page.click_create_audience_button()

        audiences_page.input_create_audience_name("a" * 256)

        expected_error_message = "Напишите текст не больше 255 символов"
        got_error_message = audiences_page.get_error_message()

        assert got_error_message == expected_error_message

    def test_same_source_and_excluded_source_error(self, audiences_page):
        audiences_page.open()

        audiences_page.click_create_audience_button()

        source = "Категории мобильного приложения"
        category_option = "Бизнес"

        audiences_page.click_add_source_button()
        audiences_page.click_category_link(source)
        audiences_page.select_category_option(category_option)
        audiences_page.confirm_source_selection(source)

        audiences_page.click_exclude_source_button()
        audiences_page.click_category_link(source)
        audiences_page.select_category_option(category_option)
        audiences_page.confirm_source_selection(source)

        expected_same_source_error_description = "Нельзя исключать выбранный источник. Просто удалите его"
        got_same_source_error_description = audiences_page.get_error_description()

        assert got_same_source_error_description == expected_same_source_error_description

    # ========== Тесты окна настроек шеринга ==========

    def test_share_settings_validation(self, audiences_page, prepare_audience, cleanup_all_audiences):
        audiences_page.open()

        audience_row = audiences_page.get_audience_row(prepare_audience)
        audiences_page.select_audience_checkbox(audience_row)

        audiences_page.click_navbar_share_button()
        audiences_page.select_public_key_radio()
        audiences_page.click_share_settings_save_button()
        audiences_page.wait_for_share_window_to_close()

        expected_sharing_link_text = "https://ads.vk.com/hq/audience?sharingKey="
        got_sharing_link_text = audiences_page.get_sharing_link_text()
        audiences_page.close_share_link_window()
        audiences_page.select_audience_checkbox(audience_row)

        assert expected_sharing_link_text in got_sharing_link_text
