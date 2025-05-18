from base import BaseCase
from ui.fixtures import *
from _pytest.fixtures import FixtureRequest
from selenium.webdriver.support import expected_conditions as EC
from ui.locators.leadforms_locators import LeadformsLocators
import os

# class TestLeadforms(BaseCase):
#     def open_page(self, request: FixtureRequest):
#         page = request.getfixturevalue('leadforms_page')
#         page.open()
#         page.wait().until(EC.presence_of_element_located(LeadformsLocators.FOOTER))
#         return page
#
#     def test_leadforms(self, request: FixtureRequest):
#         page = self.open_page(request)
#         if len(page.find_all(LeadformsLocators.BASETABLE_HEADER)) > 0:
#             assert len(page.find_all(LeadformsLocators.BASETABLE_ROW)) > 0
#             assert "Активна" in page.driver.page_source
#         else:
#             assert len(page.find_all(LeadformsLocators.BASETABLE_ROW)) == 0
#
#     def test_create_leadform(self, request: FixtureRequest):
#         page = self.open_page(request)
#         page.go_to_decoration_stage()
#         assert "Новая лид-форма" in page.driver.page_source
#         step_list = page.find(LeadformsLocators.STEPLIST)
#         assert "Оформление" in step_list.text
#         assert "Вопросы" in step_list.text
#         assert "Результат" in step_list.text
#         assert "Настройки" in step_list.text
#         assert len(page.find_all(LeadformsLocators.MODAL_SIDEBAR_PAGE_CONTENT)) > 0
#         assert len(page.find_all(LeadformsLocators.PREVIEW)) > 0
#
#     def test_decoration_main(self, request: FixtureRequest):
#         page = self.open_page(request)
#         page.go_to_decoration_stage()
#         assert len(page.find_all(LeadformsLocators.DECORATION_FORM_TITLE_INPUT)) > 0
#         assert len(page.find_all(LeadformsLocators.DECORATION_LOGO_UPLOAD)) > 0
#         assert len(page.find_all(LeadformsLocators.DECORATION_COMPANY_TITLE_INPUT)) > 0
#         assert len(page.find_all(LeadformsLocators.DECORATION_HEADER_INPUT)) > 0
#         assert len(page.find_all(LeadformsLocators.DECORATION_DESCRIPTION_INPUT)) > 0
#
#     def test_decoration_company_name_length(self, request: FixtureRequest):
#         page = self.open_page(request)
#         page.go_to_decoration_stage()
#         page.find(LeadformsLocators.DECORATION_COMPANY_TITLE_INPUT).send_keys('a'*31)
#         page.find(LeadformsLocators.CONTINUE_BUTTON).click()
#         assert "Сократите текст" in page.driver.page_source
#
#     def test_decoration_header_length(self, request: FixtureRequest):
#         page = self.open_page(request)
#         page.go_to_decoration_stage()
#         page.find(LeadformsLocators.DECORATION_HEADER_INPUT).send_keys('a'*51)
#         page.find(LeadformsLocators.CONTINUE_BUTTON).click()
#         assert "Сократите текст" in page.driver.page_source
#
#     def test_decoration_description_length(self, request: FixtureRequest):
#         page = self.open_page(request)
#         page.go_to_decoration_stage()
#         page.find(LeadformsLocators.DECORATION_DESCRIPTION_INPUT).send_keys('a'*36)
#         page.find(LeadformsLocators.CONTINUE_BUTTON).click()
#         assert "Сократите текст" in page.driver.page_source
#
#     def test_decoration_required_fields(self, request: FixtureRequest):
#         page = self.open_page(request)
#         page.go_to_decoration_stage()
#         page.find(LeadformsLocators.CONTINUE_BUTTON).click()
#         assert "Нужно заполнить" in page.driver.page_source
#         assert not "Вопросы" in page.find(LeadformsLocators.ACTIVE_STEP).text
#
#     def test_decoration_required_fields_valid(self, request: FixtureRequest):
#         page = self.open_page(request)
#         page.go_to_decoration_stage()
#         page.fill_decoration_required_fields(request)
#         page.wait().until(EC.element_to_be_clickable(LeadformsLocators.CONTINUE_BUTTON)).click()
#         page.wait()
#         assert "Вопросы" in page.find(LeadformsLocators.ACTIVE_STEP).text
#
#     def test_decoration_preview_updates(self, request: FixtureRequest):
#         page = self.open_page(request)
#         page.go_to_decoration_stage()
#         test_company = "Test Company"
#         test_header = "Test Header"
#         test_description = "Test Description"
#         page.find(LeadformsLocators.DECORATION_COMPANY_TITLE_INPUT).send_keys(test_company)
#         page.find(LeadformsLocators.DECORATION_HEADER_INPUT).send_keys(test_header)
#         page.find(LeadformsLocators.DECORATION_DESCRIPTION_INPUT).send_keys(test_description)
#         page.find(LeadformsLocators.DECORATION_LOGO_UPLOAD).click()
#         page.find(LeadformsLocators.IMAGE_UPLOAD_INPUT).send_keys(os.path.join(request.config.rootpath, 'images', 'test_image.jpg'))
#         page.wait(10).until(EC.presence_of_element_located(LeadformsLocators.UPLOADED_IMAGE))
#         page.wait(10).until(EC.element_to_be_clickable(LeadformsLocators.SAVE_UPLOAD)).click()
#         assert test_company in page.find(LeadformsLocators.PREVIEW_COMPANY_TITLE).text
#         assert test_header in page.find(LeadformsLocators.PREVIEW_HEADER).text
#         assert test_description in page.find(LeadformsLocators.PREVIEW_DESCRIPTION).text
#
#     def test_questions_stage_default(self, request: FixtureRequest):
#         page = self.open_page(request)
#         page.go_to_questions_stage(request)
#         assert "Вопросы" in page.driver.page_source
#         assert "Контактная информация" in page.driver.page_source
#         assert len(page.find_all(LeadformsLocators.QUESTION_CONTACT)) >= 2
#
#     def test_questions_min_contact_fields(self, request: FixtureRequest):
#         page = self.open_page(request)
#         page.go_to_questions_stage(request)
#         page.find(LeadformsLocators.DELETE_BUTTON).click()
#         page.find(LeadformsLocators.DELETE_BUTTON).click()
#         page.wait()
#         assert "Минимальное количество полей: 1" in page.driver.page_source
#         page.find(LeadformsLocators.CONTINUE_BUTTON).click()
#         assert not "Результат" in page.find(LeadformsLocators.ACTIVE_STEP).text
#
#     def test_questions_add_question_validation(self, request: FixtureRequest):
#         page = self.open_page(request)
#         page.go_to_questions_stage(request)
#         page.find(LeadformsLocators.ADD_QUESTION_BUTTON).click()
#         page.find(LeadformsLocators.CONTINUE_BUTTON).click()
#         assert len(page.find_all(LeadformsLocators.INVALID_QUESTION)) > 0
#         assert not "Результат" in page.find(LeadformsLocators.ACTIVE_STEP).text
#
#     def test_question_preview_updates_and_pass(self, request: FixtureRequest):
#         page = self.open_page(request)
#         page.go_to_questions_stage(request)
#         page.find(LeadformsLocators.ADD_QUESTION_BUTTON).click()
#         test_question = "Test Question"
#         test_answer1 = "Test Answer 1"
#         test_answer2 = "Test Answer 2"
#         page.find(LeadformsLocators.QUESTION_QUESTION_INPUT).send_keys(test_question)
#         answers = page.find_all(LeadformsLocators.QUESTION_ANSWER_INPUT)
#         answers[0].send_keys(test_answer1)
#         answers[1].send_keys(test_answer2)
#         assert test_question in page.find(LeadformsLocators.PREVIEW_MODAL).text
#         assert test_answer1 in page.find(LeadformsLocators.PREVIEW_MODAL).text
#         assert test_answer2 in page.find(LeadformsLocators.PREVIEW_MODAL).text
#         page.find(LeadformsLocators.CONTINUE_BUTTON).click()
#         page.wait()
#         assert "Результат" in page.find(LeadformsLocators.ACTIVE_STEP).text
#
#     # BUG!
#     """ def test_result_stage_empty(self, request: FixtureRequest):
#         page = self.open_page(request)
#         page.go_to_result_stage(request)
#         page.find(LeadformsLocators.HEADER_RESULT_INPUT).clear()
#         page.find(LeadformsLocators.HEADER_RESULT_INPUT).send_keys("a")
#         time.sleep(5)
#         page.find(LeadformsLocators.CONTINUE_BUTTON).click()
#         time.sleep(5)
#         assert "Нужно заполнить" in page.driver.page_source
#         assert not "Настройки" in page.find(LeadformsLocators.ACTIVE_STEP).text """
#
#     def test_result_stage_invalid(self, request: FixtureRequest):
#         page = self.open_page(request)
#         page.go_to_result_stage(request)
#         page.find(LeadformsLocators.HEADER_RESULT_INPUT).send_keys("a"*26)
#         page.find(LeadformsLocators.CONTINUE_BUTTON).click()
#         assert "Сократите текст" in page.driver.page_source
#         assert not "Настройки" in page.find(LeadformsLocators.ACTIVE_STEP).text
#
#     def test_result_preview_update(self, request: FixtureRequest):
#         page = self.open_page(request)
#         page.go_to_result_stage(request)
#         test_result_header = "Test Result Header"
#         page.find(LeadformsLocators.HEADER_RESULT_INPUT).send_keys(test_result_header)
#         page.find(LeadformsLocators.CONTINUE_BUTTON).click()
#         assert test_result_header in page.find(LeadformsLocators.PREVIEW_MODAL).text
#
#     def test_settings_stage_invalid(self, request: FixtureRequest):
#         page = self.open_page(request)
#         page.go_to_settings_stage(request)
#         page.find(LeadformsLocators.SAVE_BUTTON).click()
#         assert "Нужно заполнить" in page.driver.page_source
#
#     def test_settings_stage_valid_and_leadform_creation(self, request: FixtureRequest):
#         page = self.open_page(request)
#         form_title = "New Form"
#         page.go_to_decoration_stage()
#         page.fill_decoration_required_fields(request, form_title)
#         page.wait().until(EC.element_to_be_clickable(LeadformsLocators.CONTINUE_BUTTON)).click() # go_to_questions_stage
#         page.wait()
#         page.wait().until(EC.element_to_be_clickable(LeadformsLocators.CONTINUE_BUTTON)).click() # go_to_result_stage
#         page.wait()
#         page.wait().until(EC.element_to_be_clickable(LeadformsLocators.CONTINUE_BUTTON)).click() # go_to_settings_stage
#         page.wait()
#         test_name = "Test Name"
#         test_address = "Test Address"
#         page.find(LeadformsLocators.SETTINGS_NAME_INPUT).send_keys(test_name)
#         page.find(LeadformsLocators.SETTINGS_ADDRESS_INPUT).send_keys(test_address)
#         page.find(LeadformsLocators.SAVE_BUTTON).click()
#         page.wait()
#         assert form_title in page.driver.page_source