import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from locators.order_page_locators import OrderPageLocators

class OrderPage:
    # Конструктор класса
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Нажать верхнюю кнопку 'Заказать'")
    def click_button_order_up(self):
        button = self.wait.until(EC.element_to_be_clickable(OrderPageLocators.ORDER_BUTTON_UP))
        button.click()

    @allure.step("Нажать нижнюю кнопку 'Заказать'")
    def click_button_order_down(self):
        button = self.wait.until(EC.visibility_of_element_located(OrderPageLocators.ORDER_BUTTON_DOWN))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button)
        button.click()

    @allure.step("Нажать кнопку 'Заказать' на форме заказа")
    def click_button_order_on_form_order(self):
        button = self.wait.until(EC.element_to_be_clickable(OrderPageLocators.ORDER_BUTTON))
        button.click()

    @allure.step("Заполнить поле 'Имя'")
    def fill_name(self, user_name):
        name_input = self.wait.until(EC.visibility_of_element_located(OrderPageLocators.NAME))
        name_input.clear()
        name_input.send_keys(user_name)

    @allure.step("Заполнить поле 'Фамилия'")
    def fill_last_name(self, user_last_name):
        lastname_input = self.wait.until(EC.visibility_of_element_located(OrderPageLocators.LAST_NAME))
        lastname_input.clear()
        lastname_input.send_keys(user_last_name)

    @allure.step("Заполнить поле 'Адрес'")
    def fill_address(self, user_address):
        address_input = self.wait.until(EC.visibility_of_element_located(OrderPageLocators.ADDRESS))
        address_input.clear()
        address_input.send_keys(user_address)

    @allure.step("Выбрать станцию метро")
    def choose_metro_station(self, station_name):
        metro_input = self.wait.until(EC.element_to_be_clickable(OrderPageLocators.METRO))
        metro_input.clear()
        metro_input.click()
        metro_input.send_keys(station_name)
        station = self.wait.until(EC.element_to_be_clickable(OrderPageLocators.METRO_STATION))
        station.click()

    @allure.step("Заполнить поле 'Телефон'")
    def fill_phone_number(self, user_telephone):
        phone_input = self.wait.until(EC.visibility_of_element_located(OrderPageLocators.PHONE_NUMBER))
        phone_input.clear()
        phone_input.send_keys(user_telephone)

    @allure.step("Нажать кнопку 'Далее'")
    def click_next_button(self):
        next_button = self.wait.until(EC.element_to_be_clickable(OrderPageLocators.NEXT_BUTTON))
        next_button.click()

    @allure.step("Выбрать дату")
    def fill_date(self, user_date):
        date_input = self.wait.until(EC.visibility_of_element_located(OrderPageLocators.DATE))
        date_input.send_keys(user_date)
        date_input.send_keys(Keys.ENTER)

    @allure.step("Выбрать срок аренды")
    def select_rental_period(self, period_text):
        period = self.wait.until(EC.element_to_be_clickable(OrderPageLocators.RENTAL_PERIOD))
        period.click()
        self.wait.until(EC.visibility_of_element_located(OrderPageLocators.RENTAL_PERIOD_MENU))
        option = self.wait.until(EC.element_to_be_clickable(OrderPageLocators.rental_period_option(period_text)))
        option.click()


    @allure.step("Выбрать цвет 'Черный'")
    def select_scooter_color_black(self):
        checkbox = self.wait.until(EC.element_to_be_clickable(OrderPageLocators.CHECKBOX_BLACK))
        checkbox.click()

    @allure.step("Выбрать цвет 'Серый'")
    def select_scooter_color_grey(self):
        checkbox = self.wait.until(EC.element_to_be_clickable(OrderPageLocators.CHECKBOX_GREY))
        checkbox.click()

    @allure.step("Заполнить поле 'Комментарий'")
    def fill_comment(self, user_comment):
        comment_input = self.wait.until(EC.visibility_of_element_located(OrderPageLocators.COMMENT_INPUT))
        comment_input.send_keys(user_comment)

    @allure.step("Нажать кнопку 'Назад'")
    def click_button_back(self):
        back_button = self.wait.until(EC.element_to_be_clickable(OrderPageLocators.BACK_BUTTON))
        back_button.click()

    @allure.step("Завершить оформление заказа, нажав кнопку 'Заказать'")
    def complete_order(self):
        confirm_button = self.wait.until(EC.element_to_be_clickable(OrderPageLocators.ORDER_BUTTON))
        confirm_button.click()

    @allure.step("Подтвердить заказ")
    def confirm_order(self):
        try:
            return self.wait.until(EC.visibility_of_element_located(OrderPageLocators.ORDER_CONFIRMATION)).is_displayed()
        except:
            return False
        
    @allure.step("Нажать кнопку 'Да'")
    def click_button_yes(self):
        button = self.wait.until(EC.element_to_be_clickable(OrderPageLocators.BUTTON_YES))
        button.click()

    @allure.step("Окно с сообщением об успешном создании заказа")
    def is_order_successful(self):
        try:
            return "Заказ оформлен" in self.wait.until(
                EC.visibility_of_element_located(OrderPageLocators.ORDER_CONFIRMATION)).text
        except:
            return False