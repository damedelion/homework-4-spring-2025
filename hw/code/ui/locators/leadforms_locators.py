from selenium.webdriver.common.by import By


class LeadformsLocators:
    FOOTER = (By.ID, 'footer')
    BASETABLE_HEADER = (By.CLASS_NAME, "BaseTable__header")
    BASETABLE_ROW = (By.CLASS_NAME, "BaseTable__row")
    CREATE_BUTTON = (By.XPATH, "//button[contains(., 'Создать лид-форму')]")
    MODAL_SIDEBAR_PAGE = (By.XPATH, "//form[contains(@class, 'ModalSidebarPage_container')]")
    STEPLIST = (By.XPATH, "//div[contains(@class, 'CreateLeadFormModal_stepList')]")
    MODAL_SIDEBAR_PAGE_CONTENT = (By.XPATH, "//div[contains(@class, 'ModalSidebarPage_content')]")
    PREVIEW = (By.XPATH, "//div[contains(@class, 'CreateLeadFormModal_previewContainer')]")
    DECORATION_FORM_TITLE_INPUT = (By.XPATH, "//input[contains(@placeholder, 'Название лид-формы')]")
    DECORATION_LOGO_UPLOAD = (By.XPATH, "//span[contains(., 'Загрузить логотип')]")
    DECORATION_COMPANY_TITLE_INPUT = (By.XPATH, "//input[contains(@placeholder, 'Название компании')]")
    DECORATION_HEADER_INPUT = (By.XPATH, "//input[contains(@placeholder, 'Текст заголовка')]")
    DECORATION_DESCRIPTION_INPUT = (By.XPATH, "//input[contains(@placeholder, 'Введите описание')]")
    CONTINUE_BUTTON = (By.XPATH, "//button[contains(@title, 'Продолжить')]")
    ACTIVE_STEP = (By.XPATH, "//div[contains(@class, 'CreateLeadFormModal_activeStep')]")
    IMAGE_UPLOAD_INPUT = (By.CSS_SELECTOR, "input.vkuiVisuallyHidden[type='file']")
    LOADING_ICON = (By.XPATH, "//svg[contains(@class, 'vkuiIcon--duration')]")
    UPLOADED_IMAGE = (By.XPATH, "//div[contains(@class, 'ImageItem_image')]")
    MEDIA_UPLOAD_CLOSE = (By.XPATH, "//div[contains(@class, 'ModalSidebarPage_container') and .//h2[contains(text(), 'Медиатека')]]//button[@aria-label='Close']")
    PREVIEW_COMPANY_TITLE = (By.XPATH, "//span[contains(@class, 'TitleBlock-module_companyTitle')]")
    PREVIEW_HEADER = (By.XPATH, "//h2[contains(@class, 'TitleBlock-module_title')]")
    PREVIEW_DESCRIPTION = (By.XPATH, "//h4[contains(@class, 'TitleBlock-module_description')]")
    SAVE_UPLOAD = (By.XPATH, "//span[contains(., 'Сохранить')]")
    LOADED_LOGO = (By.XPATH, "//div[contains(@class, 'Preview_logo')]")
    BACKLEVEL_MODAL = (By.XPATH, "//div[contains(@class, 'ModalRoot_sidebarBackLevel')]")
    ZOOM_IMAGE = (By.XPATH, "//div[contains(., 'Увеличение изображения')]")
    CROPPER_CONTAINER = (By.XPATH, "//div[contains(@class, 'ImageCropper_container')]")
    CROPPER_BOX = (By.XPATH, "//div[contains(@class, 'cropper-crop-box')]")
    QUESTION_CONTACT = (By.XPATH, "//div[contains(@class, 'Questions_contact')]")
    DELETE_BUTTON = (By.XPATH, "//button[@aria-label='Delete']")
    ADD_QUESTION_BUTTON = (By.XPATH, "//button[contains(., 'Добавить вопрос')]")
    INVALID_QUESTION = (By.XPATH, "//div[contains(@class, 'Question_questionInvalid')]")
    QUESTION_QUESTION_INPUT = (By.XPATH, "//textarea[contains(@placeholder, 'Напишите вопрос')]")
    QUESTION_ANSWER_INPUT = (By.XPATH, "//input[contains(@placeholder, 'Введите ответ')]")
    QUESTION_PREVIEW = (By.XPATH, "//div[contains(@class, 'OnePageContentBlock-module_wrap')]")
    HEADER_RESULT_INPUT = (By.XPATH, "//div[contains(@class, 'vkuiFormItem')][.//h5[contains(text(), 'Заголовок')]]//input")
    RESULT_PREVIEW = (By.XPATH, "//div[contains(@class, 'FormPanel-module_success')]")
    SETTINGS_NAME_INPUT = (By.XPATH, "//input[contains(@placeholder, 'Введите фамилию, имя и отчество')]")
    SETTINGS_ADDRESS_INPUT = (By.XPATH, "//input[contains(@placeholder, 'Введите адрес')]")
    SAVE_BUTTON = (By.XPATH, "//button[contains(@title, 'Сохранить')]")
    PREVIEW_MODAL = (By. XPATH, "//div[contains(@class, 'CreateLeadFormModal_previewComponentWrap')]")