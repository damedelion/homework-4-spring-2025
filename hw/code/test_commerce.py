from base import BaseCase
from ui.locators.commerce_locators import CommerceLocators
from ui.fixtures import *

from selenium.webdriver.support import expected_conditions as EC

from datetime import datetime
import time


class TestCommerce(BaseCase):
    def test_click_create_catalog(self, commerce_page):
        commerce_page.open()
        commerce_page.click_create_catalog_button()
        assert commerce_page.create_catalog_header_exists()
    
    def test_click_start_onboarding_button(self, commerce_page):
        commerce_page.open()
        commerce_page.click_start_onboarding_button()
        assert commerce_page.select_onboarding_modal_exists()

    def test_default_catalog_name(self, commerce_page):
        commerce_page.open()

        commerce_page.click_create_catalog_button() 
        
        expected_date = datetime.now().strftime('%Y-%m-%d')
        expected_value = f'Каталог {expected_date}'

        catalog_name_input = commerce_page.find_catalog_name_input()
        actual_value = catalog_name_input.get_attribute('value')

        assert actual_value == expected_value
    
    def test_required_catalog_name_error(self, commerce_page):
        commerce_page.open()

        catalog_name_input = commerce_page.find_catalog_name_input()
        catalog_name_input.clear()

        commerce_page.submit_create_catalog_button()

        assert commerce_page.find_required_field_error()
    
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
        time.sleep(0.5)  # wait until url is processing

        commerce_page.submit_create_catalog_button()
        
        catalog_history_tab = commerce_page.find_catalog_tabs_history()
        selected = catalog_history_tab.get_attribute('aria-selected') == 'true'
        assert selected
    
    def test_close_create_catalog_modal(self, commerce_page):
        commerce_page.open()

        commerce_page.click_create_catalog_button()
        commerce_page.close_create_catalog_modal()

        header_is_hidden = commerce_page.wait(5).until(
            EC.invisibility_of_element_located(CommerceLocators.NEW_CATALOG_HEADER)
        )
        assert header_is_hidden
    
    def test_cancel_create_catalog_modal(self, commerce_page):
        commerce_page.open()

        commerce_page.click_create_catalog_button()
        commerce_page.cancel_create_catalog_modal()

        header_is_hidden = commerce_page.wait(5).until(
            EC.invisibility_of_element_located(CommerceLocators.NEW_CATALOG_HEADER)
        )
        assert header_is_hidden

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
        time.sleep(1)  # wait until url is processing

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
