import pytest
import time

from base import BaseCase

class TestAudiences(BaseCase):

    @pytest.fixture(scope="function", autouse=True)
    def setup_teardown_audience(self, request, audiences_page):
        """Фикстура для создания/удаления аудитории только для тестов с маркером needs_audience"""
        audiences_page.open()

        if 'needs_audience' in request.keywords:
            self.audience_name = f"Test Audience {int(time.time())}"
            audiences_page.create_audience(self.audience_name)
            yield
            audiences_page.delete_audience(self.audience_name)
        else:
            yield

    # ========== Вкладка "Аудитории": пустое состояние ==========

    def test_empty_state_ui_elements(self, audiences_page):
        audiences_page.open()

        assert audiences_page.is_empty_state_ui_correct()

    def test_create_audience_button_click(self, audiences_page):
        audiences_page.open()

        audiences_page.click_create_audience_button()

        assert audiences_page.is_create_audience_menu_opened()

    def test_kebab_menu_options_empty_state(self, audiences_page):
        audiences_page.open()

        assert audiences_page.check_kebab_menu_options_empty_state()

    # ========== Вкладка "Аудитории": при наличии аудиторий ==========

    @pytest.mark.needs_audience
    def test_navbar_ui_with_audiences(self, audiences_page):
        audiences_page.open()

        assert audiences_page.is_navbar_ui_correct()

    @pytest.mark.needs_audience
    def test_audience_list_ui(self, audiences_page):
        audiences_page.open()

        assert audiences_page.is_audience_list_ui_correct()

    @pytest.mark.needs_audience
    def test_filter_functionality(self, audiences_page):
        audiences_page.open()

        check_result =  audiences_page.check_filter_functionality()
        audiences_page.clear_filters()

        assert check_result

    @pytest.mark.needs_audience
    def test_share_button_tooltip_without_selection(self, audiences_page):
        audiences_page.open()

        audiences_page.hover_navbar_share_button()

        assert audiences_page.is_visible_share_hint()

    @pytest.mark.needs_audience
    def test_delete_button_tooltip_without_selection(self, audiences_page):
        audiences_page.open()

        audiences_page.hover_navbar_delete_button()

        assert audiences_page.is_visible_delete_hint()

    @pytest.mark.needs_audience
    def test_search_functionality(self, audiences_page):
        audiences_page.open()

        check_result = audiences_page.check_search_functionality(self.audience_name)
        audiences_page.clear_search()

        assert check_result

    @pytest.mark.needs_audience
    def test_search_empty_results(self, audiences_page):
        audiences_page.open()

        check_result = audiences_page.check_search_empty_result(int(time.time()))
        audiences_page.clear_search()

        assert check_result

    @pytest.mark.needs_audience
    def test_search_max_length_validation(self, audiences_page):
        audiences_page.open()

        assert audiences_page.check_search_validation()

    # ========== Тесты меню создания аудитории ==========

    def test_create_audience_menu_ui(self, audiences_page):
        audiences_page.open()

        audiences_page.open_create_audience_menu()

        assert audiences_page.is_create_audience_menu_ui_correct()

    def test_audience_name_validation(self, audiences_page):
        audiences_page.open()

        audiences_page.open_create_audience_menu()

        assert audiences_page.check_name_validation()

    def test_add_source_button(self, audiences_page):
        audiences_page.open()

        audiences_page.open_create_audience_menu()
        audiences_page.click_add_source_button()

        assert audiences_page.is_add_source_menu_opened()

    def test_exclude_source_button(self, audiences_page):
        audiences_page.open()

        audiences_page.open_create_audience_menu()
        audiences_page.click_exclude_source_button()

        assert audiences_page.is_exclude_source_menu_opened()

    def test_source_edit_button(self, audiences_page):
        audiences_page.open()

        audiences_page.open_create_audience_menu()
        audiences_page.add_test_source()
        audiences_page.click_edit_source_button()

        assert audiences_page.is_source_menu_opened()

    def test_excluded_source_edit_button(self, audiences_page):
        audiences_page.open()

        audiences_page.open_create_audience_menu()
        audiences_page.add_test_excluded_source()

        assert audiences_page.is_source_menu_opened()

    def test_same_source_and_excluded_source_error(self, audiences_page):
        audiences_page.open()

        audiences_page.open_create_audience_menu()
        audiences_page.add_test_source()
        audiences_page.add_same_excluded_source()

        assert audiences_page.is_same_source_error_visible()

    def test_successful_audience_creation(self, audiences_page):
        audiences_page.open()

        audience_name = f"Test Audience {int(time.time())}"
        audiences_page.create_audience(audience_name)

        is_audience_present = audiences_page.is_audience_present(audience_name)
        audiences_page.delete_audience(audience_name)

        assert is_audience_present

    # ========== Тесты меню добавления источника ==========

    def test_add_source_menu_ui(self, audiences_page):
        audiences_page.open()

        audiences_page.open_add_source_menu()

        assert audiences_page.is_add_source_menu_ui_correct()

    def test_source_category_link(self, audiences_page):
        audiences_page.open()

        audiences_page.open_add_source_menu()
        audiences_page.click_mobile_app_category_link()

        assert audiences_page.is_source_menu_opened()

    # ========== Тесты меню исключения источника ==========

    def test_exclude_source_menu_ui(self, audiences_page):
        audiences_page.open()

        audiences_page.open_exclude_source_menu()

        assert audiences_page.is_exclude_source_menu_ui_correct()

    # ========== Тесты окна настроек шеринга ==========

    @pytest.mark.needs_audience
    def test_share_settings_validation(self, audiences_page):
        audiences_page.open()

        audiences_page.share_audience()
        is_share_link_present = audiences_page.is_share_link_present()
        audiences_page.close_share_link_window()

        assert is_share_link_present
