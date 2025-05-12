from ui.pages.base_url import VKADS_BASE_URL

from ui.pages.base_page import BasePage
from ui.locators.commerce_locators import CommerceLocators

from selenium.webdriver.support import expected_conditions as EC


class CommercePage(BasePage):
    url = f'{VKADS_BASE_URL}/hq/ecomm/catalogs'
    locators = CommerceLocators
