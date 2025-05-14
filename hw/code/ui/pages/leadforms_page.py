from ui.pages.base_url import VKADS_BASE_URL
from ui.pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from ui.locators.leadforms_locators import LeadformsLocators
from _pytest.fixtures import FixtureRequest
import os
import time


class LeadformsPage(BasePage):
    url = f'{VKADS_BASE_URL}/hq/leadads/leadforms'
    locators = LeadformsLocators

    def go_to_decoration(self):
        self.find(self.locators.CREATE_BUTTON).click()
        self.wait().until(EC.presence_of_element_located(self.locators.MODAL_SIDEBAR_PAGE))

    def fill_decoration_required_fields(self, request: FixtureRequest):
        test_company = "Test Company"
        test_header = "Test Header"
        test_description = "Test Description"
        self.find(self.locators.DECORATION_COMPANY_TITLE_INPUT).send_keys(test_company)
        self.find(self.locators.DECORATION_HEADER_INPUT).send_keys(test_header)
        self.find(self.locators.DECORATION_DESCRIPTION_INPUT).send_keys(test_description)
        self.find(self.locators.DECORATION_LOGO_UPLOAD).click()
        self.wait().until(EC.presence_of_element_located(self.locators.MEDIA_UPLOAD_CLOSE))
        if len(self.find_all(self.locators.UPLOADED_IMAGE)) <= 0:
            self.find(self.locators.IMAGE_UPLOAD_INPUT).send_keys(os.path.join(request.config.rootpath, 'images', 'test_image.jpg'))
            self.wait().until(EC.invisibility_of_element(self.locators.LOADING_ICON))
            self.wait(10).until(EC.presence_of_element_located(self.locators.CROPPER_BOX))
            self.find(self.locators.SAVE_UPLOAD).click()
            self.wait().until(EC.element_to_be_clickable(self.locators.UPLOADED_IMAGE)).click()
        else:
            self.find(self.locators.UPLOADED_IMAGE).click()

        self.wait(10).until(EC.invisibility_of_element(self.locators.MEDIA_UPLOAD_CLOSE))
        self.wait().until(EC.presence_of_element_located(self.locators.LOADED_LOGO))

    def go_to_questions_stage(self, request: FixtureRequest):
        self.go_to_decoration()
        self.fill_decoration_required_fields(request)
        self.wait().until(EC.element_to_be_clickable(self.locators.CONTINUE_BUTTON)).click()
        self.wait()
        
    def go_to_result_stage(self, request: FixtureRequest):
        self.go_to_questions_stage(request)
        self.wait().until(EC.element_to_be_clickable(self.locators.CONTINUE_BUTTON)).click()
        self.wait()

    def go_to_settings_stage(self, request: FixtureRequest):
        self.go_to_result_stage(request)
        self.wait().until(EC.element_to_be_clickable(self.locators.CONTINUE_BUTTON)).click()
        self.wait()

    def create_valid_leadform(self, request: FixtureRequest):
        self.go_to_settings_stage(request)
        test_name = "Test Name"
        test_address = "Test Address"
        self.find(self.locators.SETTINGS_NAME_INPUT).send_keys(test_name)
        self.find(self.locators.SETTINGS_ADDRESS_INPUT).send_keys(test_address)
        self.find(self.locators.SAVE_BUTTON).click()
        self.wait()