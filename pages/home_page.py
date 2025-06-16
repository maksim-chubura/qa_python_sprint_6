import allure
from locators.home_page_locators import HomePageLocators
from selenium.common.exceptions import TimeoutException
from pages.base_page import BasePage

class HomePage(BasePage):
    # Конструктор класса
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Закрыть попап с кнопкой 'да все привыкли', если он есть")
    def click_popup_button(self):
        try:
            popup_button = self.wait_for_clickable(HomePageLocators.POPUP_WINDOW)
            popup_button.click()
        except:
            pass

    @allure.step("Нажать на лого 'Яндекс'")
    def click_yandex_logo(self):
        current_window = self.get_current_window_handle()
        self.click(HomePageLocators.LOGO_YANDEX)
        self.wait_for_new_window(current_window)
        new_window = [w for w in self.driver.window_handles if w != current_window][0]
        self.switch_to_window(new_window)
        self.wait.until(lambda d: d.execute_script('return document.readyState') == 'complete')


    @allure.step("Проверка открытия в новом окне через редирект главной страницы Дзена")
    def is_dzen_page_opened(self):
        try:
            self.wait.until(lambda d: 'dzen.ru' in d.current_url)
            return True
        except:
            return False

    @allure.step("Нажать на лого 'Самокат'")
    def click_scooter_logo(self):
        current_url = self.get_current_url()
        logo = self.wait_for_clickable(HomePageLocators.LOGO_SCOOTER)
        logo.click()
        self.wait.until(lambda d: d.current_url != current_url)

    @allure.step("Проверка попадания на главную страницу 'Самоката'")
    def is_main_page_opened(self):
        try:
            self.wait.until(lambda d: "qa-scooter.praktikum-services.ru" in d.current_url)
            return True
        except TimeoutException:
            return False
        
    @allure.step("Нажать кнопку 'Статус заказа'")
    def click_order_status_button(self):
        button = self.wait_for_clickable(HomePageLocators.ORDER_STATUS_BUTTON)
        button.click()

    @allure.step("Нажать верхнюю кнопку 'Заказать'")
    def click_button_order_up(self):
        self.click(HomePageLocators.ORDER_BUTTON_UP)

    @allure.step("Нажать нижнюю кнопку 'Заказать'")
    def click_button_order_down(self):
        self.scroll_into_view(HomePageLocators.ORDER_BUTTON_DOWN)
        self.click(HomePageLocators.ORDER_BUTTON_DOWN)

    @allure.step("Метод определяет какую кнопку нажать")
    def click_button_order(self, order_button):
        if order_button == "up":
            self.click_button_order_up()
        else:
            self.click_button_order_down()

    @allure.step("Перейти к 'Вопросы о важном'")
    def scroll_to_faq_section(self):
        self.scroll_into_view(HomePageLocators.FAQ)

    @allure.step("Проверить видимость элемента")
    def is_question_visible(self, question_locator):
        self.is_element_visible(question_locator)

    @allure.step("Проверка видимости ответа на вопрос")
    def is_answer_visible(self, answer_locator):
        element = self.wait_for_element(answer_locator)
        return element.is_displayed()
    
    @allure.step("Кликает на вопрос в секции FAQ и возвращает текст ответа")
    def check_faq_answer(self, question_key):
        question_locator = getattr(HomePageLocators, f"QUESTION_{question_key.upper()}")
        answer_locator = getattr(HomePageLocators, f"ANSWER_{question_key.upper()}")
        self.is_question_visible(question_locator)
        self.click(question_locator)
        self.is_answer_visible(answer_locator)
        return self.get_element_text(answer_locator)