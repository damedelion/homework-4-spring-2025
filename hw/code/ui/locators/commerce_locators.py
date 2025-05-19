from selenium.webdriver.common.by import By


class CommerceLocators:    
    START_ONBOARDING_BUTTON = (By.XPATH, '//button[@data-testid="ecomm-onboarding-start"]')
    SELECT_ONBOARDING_MODAL = (By.XPATH, '//div[contains(@class, "SelectOnboardingModal_root")]')
    
    CREATE_CATALOG_BUTTON = (By.XPATH, '//button[@data-testid="create-catalog"]')
    NEW_CATALOG_HEADER = (By.XPATH, '//h2[contains(@class, "ModalSidebarPage_title") and text()="Новый каталог"]')
    CATALOG_NAME_INPUT = (By.XPATH, '//input[@data-testid="catalogName-input"]')
    CLOSE_CREATE_CATALOG_MODAL_BUTTON = (By.XPATH, '//button[@aria-label="Close"]')
    CANCEL_CREATE_CATALOG_MODAL_BUTTON = (By.XPATH, '//button[@data-testid="cancel"]')
    
    REQUIRED_FIELD_ERROR = (By.XPATH, '//span[contains(@class, "vkuiFormItem__bottom") and @role="alert" and .//div[text()="Нужно заполнить"]]')
    REQUIRED_HTTP_PROTOCOL_ERROR = (By.XPATH, '//span[contains(@class, "vkuiFormItem__bottom") and @role="alert" and .//div[text()="Необходимо указать протокол http(s)"]]')
    INVALID_URL_ERROR = (By.XPATH, '//span[contains(@class, "vkuiFormItem__bottom") and @role="alert" and .//div[text()="Невалидный url"]]')
    INVALID_FILE_FORMAT_ERROR = (By.XPATH, '//span[contains(@class, "vkuiFormItem__bottom") and @role="alert" and .//div[text()="Неверный формат файла"]]')
    UNSUPPORTED_MARKETPLACE_URL_ERROR = (By.XPATH, '//span[contains(@class, "vkuiFormItem__bottom") and @role="alert" and .//div[text()="Введите корректную ссылку на страницу продавца на поддерживаемом маркетпласе"]]')
    
    CATALOG_FROM_URL_SELECT = (By.XPATH, '//div[@data-testid="catalog-source_type-select" and @data-entityid="url"]')
    CATALOG_URL_INPUT = (By.XPATH, '//input[@data-testid="catalogUrl-input" and @placeholder="Введите ссылку на фид или сообщество с товарами ВКонтакте"]')
    CATALOG_URL_AUTH_BUTTON = (By.XPATH, '//div[contains(@class, "BasicAuthField_authButtonContent")]')
    CATALOG_REMOVE_UTM_TAGS = (By.XPATH, '//span[text()="Автоматически удалять UTM-метки"]')

    CATALOG_FROM_MARKETPLACE_SELECT = (By.XPATH, '//div[@data-testid="catalog-source_type-select" and @data-entityid="marketplace"]')
    CATALOG_MARKETPLACE_INPUT = (By.XPATH, '//input[@data-testid="catalogUrl-input" and @placeholder="Введите ссылку на страницу магазина на маркетплейсе"]')
    
    CATALOG_FROM_FILE_SELECT = (By.XPATH, '//div[@data-testid="catalog-source_type-select" and @data-entityid="file"]')
    CATALOG_FILE_INPUT = (By.XPATH, '//input[@class="vkuiVisuallyHidden" and @type="file"]')

    CATALOG_TABS_HISTORY = (By.XPATH, '//div[@data-testid="catalog-tabs-history"]')

    SEARCH_CATALOG_INPUT = (By.XPATH, '//input[@data-testid="search" and @placeholder="Поиск"]')
    SEARCH_RESULTS_TABLE = (By.XPATH, '//div[@class="BaseTable__table BaseTable__table-main" and @role="table"]')
    SEARCH_NOT_FOUND_MESSAGE = (By.XPATH, '//div[contains(@class, "EmptyView_content") and .//h2[text()="Ничего не нашлось"]]')

    CATALOG_ROW = (By.XPATH, '//a[@data-testid="catalog-item"]')
    CATALOG_NAME = (By.XPATH, '//h4[contains(@class, "CatalogHeader_header")]')
    CATALOG_SETTINGS_BUTTON = (By.XPATH, '//button[contains(@class, "Nav_buttonSettings") and .//span[text()="Настройки"]]')
    CATALOG_SETTINGS_HEADER = (By.XPATH, '//h2[contains(@class, "ModalSidebarPage_title") and text()="Настройки каталога"]')
    CLOSE_CATALOG_SETTINGS_BUTTON = (By.XPATH, '//button[@aria-label="Close"]')
    CATALOG_SETTINGS_NAME_INPUT = (By.XPATH, '//input[@data-testid="catalogName-input"]')

    TABLE_SETTINGS_BUTTON = (By.XPATH, '//button[contains(@class, "TableSettings_settingsButton")]')
    TABLE_SETTINGS_HEADER = (By.XPATH, '//h2[contains(@class, "vkuiPanelHeader__content-in")]')
