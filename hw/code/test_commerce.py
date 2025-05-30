from base import BaseCase
from ui.fixtures import *

from datetime import datetime


class TestCommerce(BaseCase):
    def test_click_create_catalog(self, commerce_page):
        commerce_page.open()
        commerce_page.click_create_catalog_button()
        assert commerce_page.find_create_catalog_header()
    
    def test_click_start_onboarding_button(self, commerce_page):
        commerce_page.open()
        commerce_page.click_start_onboarding_button()
        assert commerce_page.find_select_onboarding_modal()

    def test_default_catalog_name(self, commerce_page):
        commerce_page.open()

        commerce_page.click_create_catalog_button() 
        
        expected_date = datetime.now().strftime('%Y-%m-%d')
        expected_value = f'Каталог {expected_date}'

        catalog_name_input = commerce_page.find_catalog_name_input()
        actual_value = catalog_name_input.get_attribute('value')

        assert actual_value == expected_value
    
    def test_required_http_protocol_error(self, commerce_page):
        commerce_page.open()

        commerce_page.click_create_catalog_button()
        commerce_page.select_catalog_from_url()
        
        catalog_url_input = commerce_page.find_catalog_from_url_input()
        catalog_url_input.send_keys('abc')

        commerce_page.submit_create_catalog_button()

        assert commerce_page.find_required_http_protocol_error()
    
    def test_invalid_url_error(self, commerce_page):
        commerce_page.open()

        commerce_page.click_create_catalog_button()
        commerce_page.select_catalog_from_url()
        
        catalog_url_input = commerce_page.find_catalog_from_url_input()
        catalog_url_input.send_keys('https://')
        commerce_page.submit_create_catalog_button()

        assert commerce_page.find_invalid_url_error()
    
    def test_select_catalog_from_url(self, commerce_page):
        commerce_page.open()

        commerce_page.click_create_catalog_button()
        commerce_page.select_catalog_from_url()

        select = commerce_page.find_catalog_from_url_select()
        box_shadow = select.value_of_css_property('box-shadow')

        assert 'rgb(38, 136, 235)' in box_shadow

    def test_selector_changing_form_inputs(self, commerce_page):
        commerce_page.open()

        commerce_page.click_create_catalog_button()
        
        commerce_page.select_catalog_from_url()
        assert commerce_page.find_catalog_from_url_input()

        commerce_page.select_catalog_from_marketplace()
        assert commerce_page.find_catalog_from_marketplace_input()

        commerce_page.select_catalog_from_file()
        assert commerce_page.find_catalog_from_file_input()

    def test_create_catalog(self, commerce_page):
        commerce_page.open()

        commerce_page.click_create_catalog_button()
        commerce_page.select_catalog_from_url()
        
        url_input = commerce_page.find_catalog_from_url_input()
        url_input.send_keys('https://vk.com/vk_ads')
        commerce_page.wait_until_utm_checkbox_disappeared()

        commerce_page.submit_create_catalog_button()
        
        catalog_history_tab = commerce_page.find_catalog_tabs_history()
        assert catalog_history_tab.get_attribute('aria-selected') == 'true'
    
    def test_close_create_catalog_modal(self, commerce_page):
        commerce_page.open()

        commerce_page.click_create_catalog_button()
        commerce_page.close_create_catalog_modal()
        commerce_page.wait_closing_create_catalog_modal()
    
    def test_cancel_create_catalog_modal(self, commerce_page):
        commerce_page.open()

        commerce_page.click_create_catalog_button()
        commerce_page.cancel_create_catalog_modal()
        commerce_page.wait_closing_create_catalog_modal()

    def test_required_catalog_url_error(self, commerce_page):
        commerce_page.open()

        commerce_page.click_create_catalog_button()
        commerce_page.select_catalog_from_url()
        
        commerce_page.submit_create_catalog_button()

        assert commerce_page.find_required_field_error()

    def test_catalog_url_auth_button_appears(self, commerce_page):
        commerce_page.open()

        commerce_page.click_create_catalog_button()
        commerce_page.select_catalog_from_url() 

        url_input = commerce_page.find_catalog_from_url_input()
        url_input.send_keys('https://education.vk.company/')

        assert commerce_page.find_catalog_url_auth_button()
    
    def test_invalid_file_format_error(self, commerce_page):
        commerce_page.open()

        commerce_page.click_create_catalog_button()
        commerce_page.select_catalog_from_url()
        
        url_input = commerce_page.find_catalog_from_url_input()
        url_input.send_keys('https://education.vk.company/')

        commerce_page.submit_create_catalog_button()

        assert commerce_page.find_invalid_file_format_error()
    
    def test_required_marketplace_catalog_url_error(self, commerce_page):
        commerce_page.open()

        commerce_page.click_create_catalog_button()
        commerce_page.select_catalog_from_marketplace()
        
        commerce_page.submit_create_catalog_button()

        assert commerce_page.find_required_field_error()
    
    def test_required_marketplace_http_protocol_error(self, commerce_page):
        commerce_page.open()

        commerce_page.click_create_catalog_button()
        commerce_page.select_catalog_from_marketplace()
        
        catalog_url_input = commerce_page.find_catalog_from_marketplace_input()
        catalog_url_input.send_keys('abc')

        commerce_page.submit_create_catalog_button()

        assert commerce_page.find_required_http_protocol_error()
    
    def test_invalid_marketplace_url_error(self, commerce_page):
        commerce_page.open()

        commerce_page.click_create_catalog_button()
        commerce_page.select_catalog_from_marketplace()
        
        catalog_url_input = commerce_page.find_catalog_from_marketplace_input()
        catalog_url_input.send_keys('https://')

        commerce_page.submit_create_catalog_button()

        assert commerce_page.find_invalid_url_error()
    
    def test_unsupported_marketplace_url_error(self, commerce_page):
        commerce_page.open()

        commerce_page.click_create_catalog_button()
        commerce_page.select_catalog_from_marketplace()
        
        catalog_url_input = commerce_page.find_catalog_from_marketplace_input()
        catalog_url_input.send_keys('https://education.vk.company/')

        commerce_page.submit_create_catalog_button()

        assert commerce_page.find_unsupported_marketplace_url_error()
    
    def test_search_catalog(self, commerce_page):
        commerce_page.open()

        commerce_page.search_for_catalog('каталог')
        assert commerce_page.find_search_results_table()
    
    def test_search_not_found(self, commerce_page):
        commerce_page.open()

        commerce_page.search_for_catalog('abc123')
        assert commerce_page.find_search_not_found_message()
    
    def test_open_catalog_from_list(self, commerce_page):
        commerce_page.open()

        commerce_page.open_catalog(0)
        assert '/hq/ecomm/catalogs/' in self.driver.current_url

    def test_open_catalog_settings_button(self, commerce_page):
        commerce_page.open()

        commerce_page.open_catalog(0)
        commerce_page.open_catalog_settings()
        
        assert commerce_page.find_catalog_settings_header()
    
    def test_submit_catalog_settings(self, commerce_page):
        commerce_page.open()

        commerce_page.open_catalog(0)
        commerce_page.open_catalog_settings()

        new_name = 'Товары - Каталог foobar'

        commerce_page.fill_settings_catalog_name(new_name)
        commerce_page.submit_catalog_settings()
    
        assert commerce_page.wait_catalog_name(new_name)
    
    def test_close_catalog_settings(self, commerce_page):
        commerce_page.open()

        commerce_page.open_catalog(0)
        commerce_page.open_catalog_settings()

        commerce_page.close_catalog_settings()
        commerce_page.wait_closing_catalog_settings()

    def test_cancel_catalog_settings(self, commerce_page):
        commerce_page.open()

        commerce_page.open_catalog(0)
        commerce_page.open_catalog_settings()

        commerce_page.cancel_catalog_settings()
        commerce_page.wait_closing_catalog_settings()
    
    def test_open_table_settings(self, commerce_page):
        commerce_page.open()

        commerce_page.open_catalog(0)
        commerce_page.open_catalog_table_settings()
        
        assert commerce_page.find_table_settings_header()