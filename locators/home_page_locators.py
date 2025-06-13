from selenium.webdriver.common.by import By

class HomePageLocators:

    POPUP_WINDOW = (By.XPATH, "//button[text()='да все привыкли']")
    LOGO_YANDEX = (By.XPATH, "//*[contains(@class, 'Header_LogoYandex')]")
    LOGO_SCOOTER = (By.XPATH, "//*[contains(@class, 'Header_LogoScooter')]")
    ORDER_STATUS_BUTTON = (By.XPATH, "//button[text()='Статус заказа']")
    ORDER_BUTTON_UP = (By.CSS_SELECTOR, "div.Header_Nav__AGCXC button.Button_Button__ra12g")
    ORDER_BUTTON_DOWN = (By.CSS_SELECTOR, "div.Home_FinishButton__1_cWm button.Button_Button__ra12g")
    FAQ = (By.XPATH, "//div[text()='Вопросы о важном']")

    QUESTION_HOW_MUCH = (By.ID, "accordion__heading-0")
    QUESTION_WANT_SOME = (By.ID, "accordion__heading-1")
    QUESTION_RENT_TIME = (By.ID, "accordion__heading-2")
    QUESTION_ORDER_TODAY = (By.ID, "accordion__heading-3")
    QUESTION_EXTEND_OR_RETURN = (By.ID, "accordion__heading-4")
    QUESTION_BRING_CHARGER = (By.ID, "accordion__heading-5")
    QUESTION_CANCEL = (By.ID, "accordion__heading-6")
    QUESTION_LIVE_OUTSIDE_MKAD = (By.ID, "accordion__heading-7")

    ANSWER_HOW_MUCH = (By.ID, "accordion__panel-0")
    ANSWER_WANT_SOME = (By.ID, "accordion__panel-1")
    ANSWER_RENT_TIME = (By.ID, "accordion__panel-2")
    ANSWER_ORDER_TODAY = (By.ID, "accordion__panel-3")
    ANSWER_EXTEND_OR_RETURN = (By.ID, "accordion__panel-4")
    ANSWER_BRING_CHARGER = (By.ID, "accordion__panel-5")
    ANSWER_CANCEL = (By.ID, "accordion__panel-6")
    ANSWER_LIVE_OUTSIDE_MKAD = (By.ID, "accordion__panel-7")
    