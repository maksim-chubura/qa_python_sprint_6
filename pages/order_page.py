import allure
from selenium.webdriver.common.keys import Keys
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage

class OrderPage(BasePage):
    # Конструктор класса
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Нажать кнопку 'Заказать' на форме заказа")
    def click_button_order_on_form_order(self):
        self.click(OrderPageLocators.ORDER_BUTTON)

    @allure.step("Заполнить поле 'Имя'")
    def fill_name(self, user_name):
        self.send_keys(OrderPageLocators.NAME, user_name)

    @allure.step("Заполнить поле 'Фамилия'")
    def fill_last_name(self, user_last_name):
        self.send_keys(OrderPageLocators.LAST_NAME, user_last_name)

    @allure.step("Заполнить поле 'Адрес'")
    def fill_address(self, user_address):
        self.send_keys(OrderPageLocators.ADDRESS, user_address)

    @allure.step("Выбрать станцию метро")
    def choose_metro_station(self, station_name):
        self.click(OrderPageLocators.METRO)
        self.send_keys(OrderPageLocators.METRO, station_name)
        self.click(OrderPageLocators.METRO_STATION)

    @allure.step("Заполнить поле 'Телефон'")
    def fill_phone_number(self, user_telephone):
        self.send_keys(OrderPageLocators.PHONE_NUMBER, user_telephone)

    @allure.step("Нажать кнопку 'Далее'")
    def click_next_button(self):
        self.click(OrderPageLocators.NEXT_BUTTON)

    @allure.step("Выбрать дату")
    def fill_date(self, user_date):
        self.send_keys(OrderPageLocators.DATE, user_date)
        self.send_keys(OrderPageLocators.DATE, Keys.ENTER)

    @allure.step("Выбрать срок аренды")
    def select_rental_period(self, period_text):
        self.click(OrderPageLocators.RENTAL_PERIOD)
        self.wait_for_visibility(OrderPageLocators.RENTAL_PERIOD_MENU)
        self.click(OrderPageLocators.rental_period_option(period_text))


    @allure.step("Выбрать цвет 'Черный'")
    def select_scooter_color_black(self):
        self.click(OrderPageLocators.CHECKBOX_BLACK)

    @allure.step("Выбрать цвет 'Серый'")
    def select_scooter_color_grey(self):
        self.click(OrderPageLocators.CHECKBOX_GREY)

    @allure.step("Метод для выбора цвета")
    def select_scooter_color(self, color):
        if color == "black":
            self.select_scooter_color_black()
        else:
            self.select_scooter_color_grey()

    @allure.step("Заполнить поле 'Комментарий'")
    def fill_comment(self, user_comment):
        self.send_keys(OrderPageLocators.COMMENT_INPUT, user_comment)

    @allure.step("Нажать кнопку 'Назад'")
    def click_button_back(self):
        self.click(OrderPageLocators.BACK_BUTTON)

    @allure.step("Завершить оформление заказа, нажав кнопку 'Заказать'")
    def complete_order(self):
        self.click(OrderPageLocators.ORDER_BUTTON)

    @allure.step("Подтвердить заказ")
    def confirm_order(self):
        try:
            return self.wait_for_visibility(OrderPageLocators.ORDER_CONFIRMATION).is_displayed()
        except:
            return False
        
    @allure.step("Нажать кнопку 'Да'")
    def click_button_yes(self):
        self.click(OrderPageLocators.BUTTON_YES)

    @allure.step("Окно с сообщением об успешном создании заказа")
    def is_order_successful(self):
        try:
            return "Заказ оформлен" in self.wait_for_visibility(OrderPageLocators.ORDER_PLACED).text
        except:
            return False