from ui.pages.base_url import VKADS_BASE_URL
from ui.pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from ui.locators.leadforms_locators import LeadformsLocators
from _pytest.fixtures import FixtureRequest
import os
import time


class LeadformsPage(BasePage):
    url = f'{VKADS_BASE_URL}/hq/leadads/leadforms'

    def go_to_decoration_stage(self):
        self.find(LeadformsLocators.CREATE_BUTTON).click()
        self.wait().until(EC.presence_of_element_located(LeadformsLocators.MODAL_SIDEBAR_PAGE))

    def fill_decoration_required_fields(self, request: FixtureRequest, form_title = "", company = "Test Company", header = "Test Header", description = "Test Description"):
        if form_title != "":
            self.find(LeadformsLocators.DECORATION_FORM_TITLE_INPUT).clear()
            self.find(LeadformsLocators.DECORATION_FORM_TITLE_INPUT).send_keys(form_title)
    
        self.find(LeadformsLocators.DECORATION_COMPANY_TITLE_INPUT).send_keys(company)
        self.find(LeadformsLocators.DECORATION_HEADER_INPUT).send_keys(header)
        self.find(LeadformsLocators.DECORATION_DESCRIPTION_INPUT).send_keys(description)
        self.find(LeadformsLocators.DECORATION_LOGO_UPLOAD).click()
        time.sleep(1) # ждем загрузку медиатеки
        self.wait().until(EC.presence_of_element_located(LeadformsLocators.MEDIA_UPLOAD_CLOSE))
        if len(self.find_all(LeadformsLocators.UPLOADED_IMAGE)) == 0:
            self.find(LeadformsLocators.IMAGE_UPLOAD_INPUT).send_keys(os.path.join(request.config.rootpath, 'images', 'test_image.jpg'))
            self.wait().until(EC.invisibility_of_element(LeadformsLocators.LOADING_ICON))
            self.wait().until(EC.presence_of_element_located(LeadformsLocators.CROPPER_BOX))
            self.find(LeadformsLocators.SAVE_UPLOAD).click()
            
        #self.wait().until(EC.element_to_be_clickable(LeadformsLocators.UPLOADED_IMAGE)).click()
        uploaded_image = self.wait().until(
        EC.element_to_be_clickable(LeadformsLocators.UPLOADED_IMAGE)
        )
        uploaded_image.click()

        self.wait().until(EC.invisibility_of_element(LeadformsLocators.MEDIA_UPLOAD_CLOSE))
        self.wait().until(EC.presence_of_element_located(LeadformsLocators.LOADED_LOGO))

    def go_to_questions_stage(self, request: FixtureRequest):
        self.go_to_decoration_stage()
        self.fill_decoration_required_fields(request)
        self.wait().until(EC.element_to_be_clickable(LeadformsLocators.CONTINUE_BUTTON)).click()
        self.wait()
        
    def go_to_result_stage(self, request: FixtureRequest):
        self.go_to_questions_stage(request)
        self.wait().until(EC.element_to_be_clickable(LeadformsLocators.CONTINUE_BUTTON)).click()
        self.wait()

    def go_to_settings_stage(self, request: FixtureRequest):
        self.go_to_result_stage(request)
        self.wait().until(EC.element_to_be_clickable(LeadformsLocators.CONTINUE_BUTTON)).click()
        self.wait()

    def create_valid_leadform(self, request: FixtureRequest, name = "Test Name", address = "Test Address"):
        self.go_to_settings_stage(request)
        self.find(LeadformsLocators.SETTINGS_NAME_INPUT).send_keys(name)
        self.find(LeadformsLocators.SETTINGS_ADDRESS_INPUT).send_keys(address)
        self.find(LeadformsLocators.SAVE_BUTTON).click()
        self.wait()