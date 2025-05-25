from selenium.webdriver.common.by import By


class CampaignLocators:
    CREATE_BTN = (By.XPATH, "//*[@data-testid='create-button']")
    SITE_FIELD = (By.XPATH, '//div[@data-id="site_conversions"]')
    SITE_URL_FIELD = (By.XPATH, '//input[@placeholder="Вставьте ссылку или выберите из списка"]')

    END_DATE_FIELD = (By.XPATH, '//span[@data-testid="end-date"]')
    FIRST_AVAILABLE_DATE = (By.XPATH, '(//div[contains(@class, "vkuiCalendarDay") and @aria-disabled="false"])[1]')

    CHANGE_NAME_BTN = (By.XPATH, "//div[contains(@class, 'EditableTitle_container__')]")
    CHANGE_NAME_FIELD = (By.XPATH, "//div[contains(@class, 'EditableTitle_container__')]//textarea")
    CHANGE_NAME_ACCEPT = (By.XPATH, "//*[contains(@class, 'EditableTitle_doneIcon__')]")

    CONTINUE_BTN = (By.XPATH, "//*[contains(@class, 'vkuiButton__content') and text() = 'Продолжить']")
    SUBMIT_BTN = (By.XPATH, "//*[contains(@class, 'vkuiButton__content') and text() = 'Опубликовать']")
    CANCEL_BTN = (By.XPATH, "//button[contains(@class, 'vkuiButton') and contains(@class, 'vkuiButton--appearance-accent')]")

    ERROR_MESSAGE = (By.XPATH, "//span[contains(@class, 'vkuiFormItem__bottom')]//div")
    SITE_BUDGET = (By.XPATH, "//span[text()='Бюджет']")
    SITE_BUDGET_INPUT = (By.XPATH, '//input[@placeholder="Не задан"]')

    GROUP_REGION = (By.XPATH, "//*[contains(@class, 'vkuiButton__content') and text()='Россия']")

    AD_TITLE_INPUT = (
        By.XPATH,
        "//span[contains(@class, 'vkuiFormField--sizeY-compact')]//div//div[contains(@data-testid, 'заголовок, макс. 40 символов')]"
    )
    AD_SHORT_DESCRIPTION_INPUT = (
        By.XPATH,
        "//span[contains(@class, 'vkuiFormField--sizeY-compact')]//div//div[contains(@data-testid, 'описание, макс. 90 символов')]"
    )

    AD_MEDIA_BTN = (
        By.XPATH,
        "//span[contains(@class, 'MediaFileAutogenSelector_sectionText') and text()='Медиатека']",
    )
    AD_MEDIA_SITES_BTN = (
        By.XPATH,
        "//div[@role='tab' and @data-id='sites']",
    )
    AD_MEDIA_SITES_IMG = (
        By.XPATH,
        "(//div[contains(@class, 'ItemList_item')])[1]",
    )
    AD_MEDIA_ADD_BTN = (By.XPATH, "//*[@data-testid='submit']")

    CAMPAIGNS_TABLE_CHECKBOX = (By.XPATH, "//*[contains(@class, 'BaseTable__header')]//*[contains(@class, 'vkuiCheckbox')]")
    CAMPAIGNS_TABLE_ACTIONS = (By.XPATH, "//*[@data-testid='select-options']")

    NO_ACTIVE_CAMPAIGNS_LABEL = (
        By.XPATH,
        "//h2[contains(@class, 'vkuiTitle--level-2')]//span",
    )

    VIDEO_CONTAINER = (By.XPATH, "//*[contains(@class, 'VideoContainer_container__')]")

    @staticmethod
    def CAMPAIGNS_TABLE_CHOOSE_OPTIONS(option):
        return (By.XPATH, f"//*[text()='{option}']")
