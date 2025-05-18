from selenium.webdriver.common.by import By

class AudiencesPageLocators:
    # Элементы вкладки "Аудитории"
    EMPTY_STATE_MESSAGE = (By.XPATH, '//h2[contains(@class, "vkuiPlaceholder__header") and text()="Аудиторий пока нет"]')
    CREATE_AUDIENCE_BUTTON = (By.XPATH, '//span[contains(@class, "vkuiButton__content") and text()="Создать аудиторию"]')
    KEBAB_MENU = (By.XPATH, '//span[contains(@class, "vkuiButton__content")]/*[name()="svg" and contains(@class, "more_horizontal")]')
    AUDIENCE_ROW = (By.XPATH, "//div[@role='row' and contains(@class, 'BaseTable__row')]")
    ALL_AUDIENCES_CHECKBOX = (By.XPATH, "//div[contains(@class, 'BaseTable__header-cell')]//label[contains(@class, 'vkuiCheckbox')]")
    AUDIENCE_IN_LIST_CHECKBOX_LOCATOR = (By.XPATH, './/label[contains(@class, "vkuiCheckbox")]')
    AUDIENCE_IN_LIST_CHECKBOX_LOCATOR_ON = (By.XPATH, './/svg[contains(@class, "vkuiIcon--check_box_on")]')
    @staticmethod
    def ABS_AUDIENCE_NAME_IN_ROW(name):
        return (By.XPATH, f'//h5[contains(@class, "NameCell_name") and text()="{name}"]')
    @staticmethod
    def REL_AUDIENCE_NAME_IN_ROW(name):
        return (By.XPATH, f'.//h5[contains(@class, "NameCell_name") and text()="{name}"]')
    CONFIRM_DELETE_AUDIENCE_BUTTON = (By.XPATH, '//button[contains(@class, "vkuiButton") and .//span[text()="Удалить"]]')
    CONTENT_LAYOUT = (By.CSS_SELECTOR, 'div[class*="tableLayout_table"]')
    
    # Навбар (при наличии аудиторий)
    NAVBAR = (By.XPATH, '//div[contains(@class, "tableLayout_toolbar")]')
    NAVBAR_KEBAB_MENU = (By.XPATH, '//button[@data-testid="other-buttons"]')
    NAVBAR_FILTER_BUTTON = (By.XPATH, '//span[contains(@class, "vkuiButton__content") and text()="Фильтр"]')
    NAVBAR_SHARE_BUTTON = (By.XPATH, '//button[@data-testid="share-button"]')
    NAVBAR_DELETE_BUTTON = (By.XPATH, '//button[@data-testid="remove-items-button"]')
    NAVBAR_SEARCH_INPUT = (By.XPATH, '//input[@data-testid="search-input"]')
    
    # Фильтры (при наличии аудиторий)
    @staticmethod
    def FILTER_OPTION(option):
        return (By.XPATH, f'//label[contains(@class, "FiltersCheckbox_checkbox")]//span[contains(@class, "vkuiText") and contains(text(), "{option}")]')
    APPLY_FILTER_BUTTON = (By.XPATH, '//span[contains(@class, "vkuiButton__content") and text()="Применить"]')
    FILTER_CLEAR_BUTTON = (By.CSS_SELECTOR, 'button[data-testid="filters-clear"]')

    # Поиск (при наличии аудиторий)
    SEARCH_RESULTS = (By.XPATH, '//div[contains(@class, "Loading_loading")]')
    SEARCH_CLEAR_BUTTON = (By.XPATH, '//button[@aria-label="Очистить"]')

    # Список аудиторий (при наличии аудиторий)
    AUDIENCE_ITEM = (By.XPATH, '//div[contains(@class, "NameCell_wrapper")]')
    AUDIENCE_LIST = (By.XPATH, '//div[contains(@class, "BaseTable__body")]')
    AUDIENCE_NAME_COLUMN = (By.XPATH, '//div[@data-key="name" and contains(text(), "Название")]')
    AUDIENCE_REACH_COLUMN = (By.XPATH, '//div[@data-key="coverage" and contains(text(), "Охват")]')
    
    # Меню создания аудитории
    CREATE_AUDIENCE_MENU_TITLE = (By.XPATH, '//h2[contains(@class, "ModalSidebarPage_title") and text()="Создание аудитории"]')
    CREATE_AUDIENCE_NAME_INPUT = (By.XPATH, '//input[contains(@class, "vkuiInput__el")]')
    CREATE_AUDIENCE_ADD_SOURCE_BUTTON = (By.XPATH, '//span[contains(@class, "vkuiButton__content") and text()="Добавить источник"]')
    CREATE_AUDIENCE_EXCLUDE_SOURCE_BUTTON = (By.XPATH, '//span[contains(@class, "vkuiButton__content") and text()="Исключить источник"]')
    CREATE_AUDIENCE_SAVE_BUTTON = (By.XPATH, '//form[contains(@class, "ModalSidebarPage_container") and .//h2[text()="Создание аудитории"]]//button[@type="submit" and descendant::span[text()="Сохранить"]]')
    CREATE_AUDIENCE_MODAL_OVERLAY = (By.XPATH, '//div[contains(@class, "vkui__root") and .//h2[text()="Создание аудитории"]]')

    # Добавление источника
    CATEGORY_SELECTOR = (By.CSS_SELECTOR, '[data-testid="sources.app_category.category_selector"]')
    @staticmethod
    def CATEGORY_OPTION(option):
        return (By.XPATH, f'//div[@role="option" and @title="{option}"]')
    @staticmethod
    def SELECT_SOURCE_BUTTON(source):
        return (By.XPATH, f'//div[contains(@class, "ModalSidebarPage_container") and .//h2[text()="{source}"]]//button[@type="submit" and descendant::span[text()="Сохранить"]]')
    @staticmethod
    def CATEGORY_LINK(source):
        return (By.XPATH, f'//div[contains(@class, "SourceType_button")]//span[contains(text(), "{source}")]')
    @staticmethod
    def SOURCE_MODAL_OVERLAY(source):
        return (By.XPATH, f'//div[contains(@class, "vkui__root") and .//h2[text()="{source}"]]')

    # Меню исключения источника
    EXCLUDE_SOURCE_MENU_TITLE = (By.XPATH, '//h2[contains(@class, "ModalSidebarPage_title") and text()="Исключить источник"]')
    
    # Меню источника
    SOURCE_MENU_TITLE = (By.XPATH, '//h2[contains(@class, "ModalSidebarPage_title") and contains(text(), "События в мобильном приложении")]')
    
    # Окно шеринга
    SHARE_SETTINGS_WINDOW = (By.XPATH, '//div[contains(@class, "vkuiModalPage__in-wrap") and contains(text(), "Поделиться")]')
    SHARE_PUBLIC_KEY_RADIO = (By.XPATH, '//label[contains(@class, "sharingAuditoryForm_radio")]//span[contains(@class, "vkuiText") and contains(text(), "Публичный ключ")]')
    SHARE_SETTINGS_SAVE_BUTTON = (By.XPATH, '//span[contains(@class, "vkuiButton__content") and text()="Сохранить"]')
    SHARING_LINK = (By.XPATH, '//span[contains(@class, "sharingSuccessModal_sharingLink")]')
    SHARE_LINK_WINDOW_CLOSE_BUTTON = (By.XPATH, '//button[.//span[text()="Закрыть"]]')
    
    #Общие
    HINT_TOOLTIP = (By.XPATH, '//div[contains(@class, "Tooltip_tooltip")]')
    ERROR_MESSAGE = (By.XPATH, '//span[contains(@class, "vkuiFormItem__bottom")]')
    ERROR_DESCRIPTION = (By.CSS_SELECTOR, 'div[class*="RichBanner_content"]')
    ACTION_BUTTON = (By.CSS_SELECTOR, 'div[class*="EmptyViewActionButton_cell"]')
    @staticmethod
    def LINK(content):
        return (By.XPATH, f"//span[@class='vkuiButton__in']//span[text()='{content}']")
    @staticmethod
    def HEADER(content):
        return (By.XPATH, f'//h2[contains(@class, "vkuiPlaceholder__header") and text()="{content}"]')