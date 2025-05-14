from selenium.webdriver.common.by import By

from ui.locators.basic_locators import BasePageLocators

class AudiencesPageLocators(BasePageLocators):
    # Общие элементы (пустое состояние)
    EMPTY_STATE_MESSAGE = (By.XPATH, '//h2[contains(@class, "vkuiPlaceholder__header") and text()="Аудиторий пока нет"]')
    CREATE_AUDIENCE_BUTTON = (By.XPATH, '//span[contains(@class, "vkuiButton__content") and text()="Создать аудиторию"]')
    KEBAB_MENU = (By.XPATH, '//span[contains(@class, "vkuiButton__content")]/*[name()="svg" and contains(@class, "more_horizontal_24")]')
    HOW_AUDIENCES_WORK_LINK = (By.XPATH, "//span[@class='vkuiButton__in']//span[text()='Как работают аудитории']")
    AUDIENCE_ROW = (By.XPATH, "//div[@role='row' and contains(@class, 'BaseTable__row')]")
    AUDIENCE_IN_LIST_CHECKBOX_LOCATOR = (By.XPATH, './/label[contains(@class, "vkuiCheckbox")]')
    AUDIENCE_IN_LIST_CHECKBOX_LOCATOR_ON = (By.CLASS_NAME, "vkuiIcon--check_box_on_20")
    @staticmethod
    def ABS_AUDIENCE_NAME_IN_ROW(name):
        return (By.XPATH, f'//h5[contains(@class, "NameCell_name") and text()="{name}"]')
    @staticmethod
    def REL_AUDIENCE_NAME_IN_ROW(name):
        return (By.XPATH, f'.//h5[contains(@class, "NameCell_name") and text()="{name}"]')
    CONFIRM_DELETE_AUDIENCE_BUTTON = (By.XPATH, '//button[contains(@class, "vkuiButton") and .//span[text()="Удалить"]]')
    SHARE_HINT_TOOLTIP = (By.XPATH,'//div[contains(@class, "Tooltip_tooltip__") and contains(text(), "Выберите аудитории, которыми хотите поделиться")]')
    DELETE_HINT_TOOLTIP = (By.XPATH, '//div[contains(@class, "Tooltip_tooltip__") and contains(text(), "Выберите аудитории, которые хотите удалить")]')

    # Кебаб-меню опции
    ACTIVATE_EXTERNAL_AUDIENCE_OPTION = (By.XPATH, '//div[@data-testid="Активировать внешнюю аудиторию-others"]')
    TRANSFER_VK_AUDIENCE_OPTION = (By.XPATH, '//div[@data-testid="Перенести аудитории из кабинета ВКонтакте-others"]')
    
    # Навбар (при наличии аудиторий)
    NAVBAR = (By.XPATH, '//div[contains(@class, "tableLayout_toolbar__GPCLD")]')
    NAVBAR_KEBAB_MENU = (By.XPATH, '//button[@data-testid="other-buttons"]')
    NAVBAR_FILTER_BUTTON = (By.XPATH, '//span[contains(@class, "vkuiButton__content") and text()="Фильтр"]')
    NAVBAR_SHARE_BUTTON = (By.XPATH, '//button[@data-testid="share-button"]')
    NAVBAR_DELETE_BUTTON = (By.XPATH, '//button[@data-testid="remove-items-button"]')
    NAVBAR_SEARCH_INPUT = (By.XPATH, '//input[@data-testid="search-input"]')
    
    # Фильтры
    FIRST_FILTER_OPTION = (By.XPATH, '//label[contains(@class, "FiltersCheckbox_checkbox__xZ-5Y")]//span[contains(@class, "vkuiText") and contains(text(), "Уже созданная аудитория")]')
    APPLY_FILTER_BUTTON = (By.XPATH, '//span[contains(@class, "vkuiButton__content") and text()="Применить"]')
    ACTIVE_FILTER_TAG = ACTIVE_FILTER_TAG = (By.XPATH, '//div[contains(@class, "ToolbarButton_after__")]/span[contains(@class, "vkuiCounter") and text()="1"]')
    FILTER_CLEAR_BUTTON = (By.CSS_SELECTOR, 'button[data-testid="filters-clear"]')

    # Поиск
    SEARCH_RESULTS = (By.XPATH, '//div[contains(@class, "Loading_loading__o-t1B")]')
    EMPTY_SEARCH_RESULT = (By.XPATH, '//h2[contains(@class, "vkuiTypography") and contains(text(), "Ничего не нашлось")]')
    SEARCH_CLEAR_BUTTON = (By.XPATH, '//button[@aria-label="Очистить"]')
    SEARCH_INPUT_ERROR_HINT_TOOLTIP = (By.XPATH, '//div[contains(@class, "Tooltip_tooltipContainer__P1b-O") and contains(text(), "Максимальная длина 255 символов")]')

    # Список аудиторий
    AUDIENCE_ITEM = (By.XPATH, '//div[contains(@class, "NameCell_wrapper__hxqrL")]')
    AUDIENCE_LIST = (By.XPATH, '//div[contains(@class, "BaseTable__body")]')
    AUDIENCE_NAME_COLUMN = (By.XPATH, '//div[@data-key="name" and contains(text(), "Название")]')
    AUDIENCE_REACH_COLUMN = (By.XPATH, '//div[@data-key="coverage" and contains(text(), "Охват")]')
    
    # Меню создания аудитории
    CREATE_AUDIENCE_MENU_TITLE = (By.XPATH, '//h2[contains(@class, "ModalSidebarPage_title__Uu-FC") and text()="Создание аудитории"]')
    CREATE_AUDIENCE_NAME_INPUT = (By.XPATH, '//input[contains(@class, "vkuiInput__el")]')
    CREATE_AUDIENCE_ADD_SOURCE_BUTTON = (By.XPATH, '//span[contains(@class, "vkuiButton__content") and text()="Добавить источник"]')
    CREATE_AUDIENCE_EXCLUDE_SOURCE_BUTTON = (By.XPATH, '//span[contains(@class, "vkuiButton__content") and text()="Исключить источник"]')
    CREATE_AUDIENCE_NAME_ERROR = (By.XPATH, '//span[contains(@class, "vkuiFormItem__bottom") and contains(text(), "Напишите текст не больше 255 символов")]')
    CREATE_AUDIENCE_SAVE_BUTTON = (By.XPATH, '//form[contains(@class, "ModalSidebarPage_container__Zopae") and .//h2[text()="Создание аудитории"]]//button[@type="submit" and descendant::span[text()="Сохранить"]]')
    CREATE_AUDIENCE_MODAL_OVERLAY = (By.XPATH, '//div[contains(@class, "vkui__root") and .//h2[text()="Создание аудитории"]]')
    CREATE_AUDIENCE_ADDED_SOURCE_HEADER = (By.XPATH, "//h4[text()='Категории мобильного приложения']")

    # Создание источника
    CATEGORY_SELECTOR = (By.CSS_SELECTOR, '[data-testid="sources.app_category.category_selector"]')
    BUSINESS_CATEGORY_OPTION = (By.XPATH, '//div[@role="option" and @title="Бизнес"]')
    SELECT_SOURCE_BUTTON = (By.XPATH, '//div[contains(@class, "ModalSidebarPage_container__Zopae") and .//h2[text()="Категории мобильного приложения"]]//button[@type="submit" and descendant::span[text()="Сохранить"]]')
    EDIT_SOURCE_BUTTON = (By.CSS_SELECTOR, "svg.vkuiIcon--write_outline_20")
    DELETE_SOURCE_BUTTON = (By.CSS_SELECTOR, "svg.vkuiIcon--delete_outline_20")
    EDIT_EXCLUDED_SOURCE_BUTTON = (By.CSS_SELECTOR, "svg.vkuiIcon--write_outline_20") 
    DELETE_EXCLUDED_SOURCE_BUTTON = (By.CSS_SELECTOR, "svg.vkuiIcon--delete_outline_20")
    SAME_SOURCE_ERROR = (By.CSS_SELECTOR, 'svg.SourceListItem_errorIcon__skhww')

    # Меню добавления источника
    ADD_SOURCE_MENU_TITLE = (By.XPATH, '//h2[contains(@class, "ModalSidebarPage_title__Uu-FC") and text()="Добавить источник"]')
    MY_AUDIENCES_SECTION = (By.XPATH, '//span[contains(@class, "SourceType_groupHeader__VNiec") and text()="Мои аудитории"]')
    MOBILE_APP_CATEGORY_LINK = (By.XPATH, '//div[contains(@class, "SourceType_button__c4PpZ")]//span[contains(text(), "Категории мобильного приложения")]')
    SOURCE_MODAL_OVERLAY = (By.XPATH, '//div[contains(@class, "vkui__root") and .//h2[text()="Категории мобильного приложения"]]')

    # Меню исключения источника
    EXCLUDE_SOURCE_MENU_TITLE = (By.XPATH, '//h2[contains(@class, "ModalSidebarPage_title__Uu-FC") and text()="Исключить источник"]')
    
    # Меню источника
    SOURCE_MENU_TITLE = (By.XPATH, '//h2[contains(@class, "ModalSidebarPage_title__Uu-FC") and contains(text(), "События в мобильном приложении")]')
    
    # Окно шеринга
    SHARE_SETTINGS_WINDOW = (By.XPATH, '//div[contains(@class, "vkuiModalPage__in-wrap") and contains(text(), "Поделиться")]')
    SHARE_PUBLIC_KEY_RADIO = (By.XPATH, '//label[contains(@class, "sharingAuditoryForm_radio__CNgkd")]//span[contains(@class, "vkuiText") and contains(text(), "Публичный ключ")]')
    SHARE_SETTINGS_SAVE_BUTTON = (By.XPATH, '//span[contains(@class, "vkuiButton__content") and text()="Сохранить"]')
    SHARING_LINK = (By.XPATH, '//span[contains(@class, "sharingSuccessModal_sharingLink__lcRwA") and contains(text(), "https://ads.vk.com/hq/audience?sharingKey=")]')
    SHARE_LINK_WINDOW_CLOSE_BUTTON = (By.XPATH, '//button[.//span[text()="Закрыть"]]')
    
