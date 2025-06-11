from selenium.webdriver.common.by import By

class OrderPageLocators:

    ORDER_BUTTON_UP = (By.CSS_SELECTOR, "div.Header_Nav__AGCXC button.Button_Button__ra12g")
    ORDER_BUTTON_DOWN = (By.CSS_SELECTOR, "div.Home_FinishButton__1_cWm button.Button_Button__ra12g")
    NAME = (By.XPATH, "//input[@placeholder='* Имя']")
    LAST_NAME = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO = (By.CSS_SELECTOR, "input.select-search__input")
    METRO_STATION = (By.XPATH, "//div[contains(@class, 'select-search__select')]")
    PHONE_NUMBER = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")
    DATE = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENTAL_PERIOD = (By.XPATH, "//div[contains(@class, 'Dropdown-control')]")
    RENTAL_PERIOD_MENU = (By.XPATH, "//div[contains(@class, 'Dropdown-menu')]")
    CHECKBOX_BLACK = (By.XPATH, "//label[@for='black']")
    CHECKBOX_GREY = (By.XPATH, "//label[@for='grey']")
    COMMENT_INPUT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    BACK_BUTTON = (By.CSS_SELECTOR, "div.Order_Buttons__1xGrp > button.Button_Button__ra12g.Button_Middle__1CSJM.Button_Inverted__3IF-i")
    ORDER_BUTTON = (By.CSS_SELECTOR, "div.Order_Buttons__1xGrp > button.Button_Button__ra12g.Button_Middle__1CSJM:not(.Button_Inverted__3IF-i)")
    ORDER_CONFIRMATION = (By.XPATH, "//div[@class='Order_ModalHeader__3FDaJ' and contains(text(), 'Хотите оформить заказ?')]")
    BUTTON_YES = (By.XPATH, "//button[contains(text(), 'Да')]")
    BUTTON_NO = (By.XPATH, "//button[contains(text(), 'Нет')]")
    ORDER_PLACED = (By.CLASS_NAME, "Order_ModalHeader__3FDaJ")

    @staticmethod
    def rental_period_option(period_text):
        return (By.XPATH, f"//div[contains(@class, 'Dropdown-option') and contains(text(), '{period_text}')]")


 
