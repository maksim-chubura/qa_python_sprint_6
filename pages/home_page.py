import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.home_page_locators import HomePageLocators
from selenium.common.exceptions import TimeoutException
from config import QUESTIONS_AND_ANSWERS

class HomePage:
    # Конструктор класса
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Закрыть попап с кнопкой 'да все привыкли', если он есть")
    def click_popup_button(self):
        try:
            popup_button = self.wait.until(EC.element_to_be_clickable(HomePageLocators.POPUP_WINDOW))
            popup_button.click()
        except:
            pass

    @allure.step("Нажать на лого 'Яндекс'")
    def click_yandex_logo(self):
        current_window = self.driver.current_window_handle
        logo = self.wait.until(EC.element_to_be_clickable(HomePageLocators.LOGO_YANDEX))
        logo.click()
        WebDriverWait(self.driver, 10).until(lambda d: len(d.window_handles) > 1)
        new_window = [window for window in self.driver.window_handles if window != current_window][0]
        self.driver.switch_to.window(new_window)
        WebDriverWait(self.driver, 10).until(
        lambda d: d.execute_script('return document.readyState') == 'complete'
    )

    @allure.step("Проверка открытия в новом окне через редирект главной страницы Дзена")
    def is_dzen_page_opened(self):
        try:
            WebDriverWait(self.driver, 10).until(lambda d: 'dzen.ru' in d.current_url)
            return True
        except:
            return False

    @allure.step("Нажать на лого 'Самокат'")
    def click_scooter_logo(self):
        current_url = self.driver.current_url
        logo = self.wait.until(EC.element_to_be_clickable(HomePageLocators.LOGO_SCOOTER))
        logo.click()
        WebDriverWait(self.driver, 10).until(lambda d: d.current_url != current_url)

    @allure.step("Проверка попадания на главную страницу 'Самоката'")
    def is_main_page_opened(self):
        try:
            WebDriverWait(self.driver, 5).until(
                lambda d: "qa-scooter.praktikum-services.ru" in d.current_url)
            return True
        except TimeoutException:
            return False
        
    @allure.step("Нажать кнопку 'Статус заказа'")
    def click_order_status_button(self):
        button = self.wait.until(EC.element_to_be_clickable(HomePageLocators.ORDER_STATUS_BUTTON))
        button.click()

    @allure.step("Перейти к 'Вопросы о важном'")
    def scroll_to_faq_section(self):
        element = self.wait.until(EC.visibility_of_element_located(HomePageLocators.FAQ))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    @allure.step("Проверить видимость элемента")
    def is_question_visible(self, question_locator):
        element = self.wait.until(EC.presence_of_element_located(question_locator))
        return element.is_displayed()

    # Нажать на 'Вопросы о важном' по локатору
    def click_question(self, question_locator):
        question = self.wait.until(EC.element_to_be_clickable(question_locator))
        question.click()

    @allure.step("Нажать на первый вопрос")
    def click_question_how_much(self):
        question = self.wait.until(EC.element_to_be_clickable(HomePageLocators.QUESTION_HOW_MUCH))
        question.click()

    @allure.step("Нажать на второй вопрос")
    def click_question_want_some(self):
        self.click_question(HomePageLocators.QUESTION_WANT_SOME)

    @allure.step("Нажать на третий вопрос")
    def click_question_rent_time(self):
        self.click_question(HomePageLocators.QUESTION_RENT_TIME)

    @allure.step("Нажать на четвертый вопрос")
    def click_question_order_today(self):
        self.click_question(HomePageLocators.QUESTION_ORDER_TODAY)

    @allure.step("Нажать на пятый вопрос")
    def click_question_extend_or_return(self):
        self.click_question(HomePageLocators.QUESTION_EXTEND_OR_RETURN)

    @allure.step("Нажать на шестой вопрос")
    def click_question_bring_charger(self):
        self.click_question(HomePageLocators.QUESTION_BRING_CHARGER)

    @allure.step("Нажать на седьмой вопрос")
    def click_question_cancel(self):
        self.click_question(HomePageLocators.QUESTION_CANCEL)

    @allure.step("Нажать на восьмой вопрос")
    def click_question_live_outside_mkad(self):
        self.click_question(HomePageLocators.QUESTION_LIVE_OUTSIDE_MKAD)

    @allure.step("Проверка видимости ответа на вопрос")
    def is_answer_visible(self, answer_locator):
        element = self.wait.until(EC.presence_of_element_located(answer_locator))
        return element.is_displayed()
    
    @allure.step("Получить текст ответа на вопрос")
    def get_answer_text(self, answer_key):
        return QUESTIONS_AND_ANSWERS[answer_key]['answer']
    
    # Методы возвращают ответы для каждого вопроса
    def get_answer(self, answer_locator):
        answer = self.wait.until(EC.visibility_of_element_located(answer_locator))
        return answer.text

    @allure.step("Получить ответ на первый вопрос")
    def get_answer_to_question_how_much(self):
        return self.get_answer(HomePageLocators.ANSWER_HOW_MUCH)

    @allure.step("Получить ответ на второй вопрос")
    def get_answer_to_question_want_some(self):
        return self.get_answer(HomePageLocators.ANSWER_WANT_SOME)

    @allure.step("Получить ответ на третий вопрос")
    def get_answer_to_question_rent_time(self):
        return self.get_answer(HomePageLocators.ANSWER_RENT_TIME)

    @allure.step("Получить ответ на четвертый вопрос")
    def get_answer_to_question_order_today(self):
        return self.get_answer(HomePageLocators.ANSWER_ORDER_TODAY)

    @allure.step("Получить ответ на пятый вопрос")
    def get_answer_to_question_extend_or_return(self):
        return self.get_answer(HomePageLocators.ANSWER_EXTEND_OR_RETURN)

    @allure.step("Получить ответ на шестой вопрос")
    def get_answer_to_question_bring_charger(self):
        return self.get_answer(HomePageLocators.ANSWER_BRING_CHARGER)

    @allure.step("Получить ответ на седьмой вопрос")
    def get_answer_to_question_cancel(self):
        return self.get_answer(HomePageLocators.ANSWER_CANCEL)

    @allure.step("Получить ответ на восьмой вопрос")
    def get_answer_to_question_live_outside_mkad(self):
        return self.get_answer(HomePageLocators.ANSWER_LIVE_OUTSIDE_MKAD)