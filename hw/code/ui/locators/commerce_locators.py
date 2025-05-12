from selenium.webdriver.common.by import By


class CommerceLocators:    
    START_ONBOARDING_BUTTON = (By.XPATH, '//button[@data-testid="ecomm-onboarding-start"]')
    SELECT_ONBOARDING_MODAL = (By.XPATH, '//div[contains(@class, "SelectOnboardingModal_root")]')
    
    CREATE_CATALOG_BUTTON = (By.XPATH, '//button[@data-testid="create-catalog"]')
    NEW_CATALOG_HEADER = (By.XPATH, '//h2[contains(@class, "ModalSidebarPage_title") and text()="Новый каталог"]')
    CATALOG_NAME_INPUT = (By.XPATH, '//input[@data-testid="catalogName-input"]')
    SUBMIT_CREATE_CATALOG_BUTTON = (By.XPATH, '//button[@data-testid="submit" and @title="Создать каталог"]')
    REQUIRED_FIELD_ERROR = (By.XPATH, '//span[contains(@class, "vkuiFormItem__bottom") and @role="alert" and .//div[text()="Нужно заполнить"]]')
    CLOSE_CREATE_CATALOG_MODAL_BUTTON = (By.XPATH, '//button[@aria-label="Close"]')
    CANCEL_CREATE_CATALOG_MODAL_BUTTON = (By.XPATH, '//button[@data-testid="cancel"]')
    
    CATALOG_FROM_URL_SELECT = (By.XPATH, '//div[@data-testid="catalog-source_type-select" and @data-entityid="url"]')
    CATALOG_URL_INPUT = (By.XPATH, '//input[@data-testid="catalogUrl-input" and @placeholder="Введите ссылку на фид или сообщество с товарами ВКонтакте"]')

    CATALOG_FROM_MARKETPLACE_SELECT = (By.XPATH, '//div[@data-testid="catalog-source_type-select" and @data-entityid="marketplace"]')
    CATALOG_MARKETPLACE_INPUT = (By.XPATH, '//input[@data-testid="catalogUrl-input" and @placeholder="Введите ссылку на страницу магазина на маркетплейсе"]')
    
    CATALOG_FROM_FILE_SELECT = (By.XPATH, '//div[@data-testid="catalog-source_type-select" and @data-entityid="file"]')
    CATALOG_FILE_INPUT = (By.XPATH, '//input[@class="vkuiVisuallyHidden" and @type="file"]')

    CATALOG_TABS_HISTORY = (By.XPATH, '//div[@data-testid="catalog-tabs-history"]')
    
