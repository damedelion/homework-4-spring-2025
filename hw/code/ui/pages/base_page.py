import time

from selenium.webdriver.remote.webelement import WebElement
from ui.locators import basic_locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from ui.locators.basic_locators import BasePageLocators

from ui.pages.base_url import VKADS_BASE_URL

from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains

class PageNotOpenedExeption(Exception):
    pass


class BasePage(object):
    url = VKADS_BASE_URL

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.url)
        self.is_opened()

    def is_opened(self, timeout=15):
        started = time.time()
        while time.time() - started < timeout:
            if self.driver.current_url == self.url:
                return True
        raise PageNotOpenedExeption(f'{self.url} did not open in {timeout} sec, current url {self.driver.current_url}')

    def wait(self, timeout=None):
        if timeout is None:
            timeout = 5
        return WebDriverWait(self.driver, timeout=timeout)

    def find(self, locator, timeout=None):
        return self.wait(timeout).until(EC.presence_of_element_located(locator))
    
    def find_elements(self, locator, timeout=10):
        def _elements_present(driver):
            elements = driver.find_elements(*locator)
            return elements if elements else False
        return self.wait(timeout).until(_elements_present)

    def is_present(self, locator, timeout=5):
        try:
            self.wait(timeout).until(EC.presence_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def search(self, query):
        elem = self.find(BasePageLocators.QUERY_LOCATOR_ID)
        elem.send_keys(query)
        go_button = self.find(BasePageLocators.GO_BUTTON_LOCATOR)
        go_button.click()
        self.my_assert()

    def my_assert(self):
        assert 1 == 1

    def click(self, locator, timeout=None) -> WebElement:
        elem = self.find(locator, timeout=timeout)
        elem = self.wait(timeout).until(EC.element_to_be_clickable(locator))
        elem.click()

    def click_element(self, locator, timeout=10):
        element = self.wait(timeout).until(EC.element_to_be_clickable(locator))
        element.click()

    def hover(self, locator):
        elem = self.find(locator)
        ActionChains(self.driver).move_to_element(elem).perform()

    def is_visible(self, locator, timeout=10):
        try:
            return self.wait(timeout).until(EC.visibility_of_element_located(locator)) is not None
        except:
            return False

    def wait_to_disappear(self, locator, timeout=10):
        self.wait(timeout).until(EC.invisibility_of_element_located(locator))

    def wait_until_visible(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def wait_until_invisible(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    def find_all(self, locator):
        return self.driver.find_elements(*locator)
