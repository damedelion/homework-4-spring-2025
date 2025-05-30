from selenium.webdriver.common.by import By

class BasePageLocators:
    @staticmethod
    def testid(id):
        return (By.XPATH, f'//*[@data-testid="{id}"]')
