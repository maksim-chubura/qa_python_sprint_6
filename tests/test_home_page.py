import pytest
import allure
from pages.home_page import HomePage
from config import QUESTIONS_AND_ANSWERS

class TestYandexLogo:
    @allure.title("Клик по логотипу Яндекс открывает Дзен")
    def test_yandex_logo_redirect(self, driver):
        home = HomePage(driver)
        home.click_popup_button()
        home.click_yandex_logo()
        home.is_dzen_page_opened()

class TestScooterLogo:
    @allure.title("Клик по логотипу Cамокат открывает главную страницу")
    def test_scooter_logo_redirect(self, driver):
        home = HomePage(driver)
        home.click_popup_button()
        home.click_button_order_up()
        home.click_scooter_logo()
        home.is_main_page_opened()

class TestFaqSection:

    @pytest.mark.parametrize("question_key", [
        "how_much",
        "want_some",
        "rent_time",
        "order_today",
        "extend_or_return",
        "bring_charger",
        "cancel",
        "live_outside_mkad"
    ])
    @allure.title("Проверка вопросов и ответов в секции FAQ")
    def test_faq_questions_and_answers(self, driver, question_key):
        home = HomePage(driver)
        home.click_popup_button()
        home.scroll_to_faq_section()

        expected_answer = QUESTIONS_AND_ANSWERS[question_key]["answer"]
        actual_answer = home.check_faq_answer(question_key)
        assert actual_answer == expected_answer, f"Вопрос: {question_key}"