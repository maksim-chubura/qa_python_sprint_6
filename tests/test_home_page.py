import allure
from pages.home_page import HomePage
from pages.order_page import OrderPage
from locators.home_page_locators import HomePageLocators
from config import QUESTIONS_AND_ANSWERS

@allure.title("Клик по логотипу Яндекс открывает Дзен")
def test_yandex_logo_redirect(driver):
    home = HomePage(driver)
    home.click_popup_button()
    home.click_yandex_logo()
    home.is_dzen_page_opened()
    
@allure.title("Клик по логотипу Cамокат открывает главную страницу")
def test_scooter_logo_redirect(driver):
    home = HomePage(driver)
    order = OrderPage(driver)
    home.click_popup_button()
    order.click_button_order_up()
    home.click_scooter_logo()
    home.is_main_page_opened()

@allure.title("При нажатии на первый вопрос, открывается соответствующий текст ответа")
def test_question_how_much(driver):
    home = HomePage(driver)
    home.click_popup_button()
    home.scroll_to_faq_section()
    assert home.is_question_visible(HomePageLocators.QUESTION_HOW_MUCH)
    home.click_question_how_much()
    assert home.is_answer_visible(HomePageLocators.ANSWER_HOW_MUCH)
    answer = QUESTIONS_AND_ANSWERS["how_much"]["answer"]
    actual = home.get_answer_to_question_how_much()
    assert actual == answer

@allure.title("При нажатии на второй вопрос, открывается соответствующий текст ответа")
def test_question_and_answer_want_some(driver):
    home = HomePage(driver)
    home.click_popup_button()
    home.scroll_to_faq_section()
    assert home.is_question_visible(HomePageLocators.QUESTION_WANT_SOME)
    home.click_question_want_some()
    assert home.is_answer_visible(HomePageLocators.ANSWER_WANT_SOME)
    answer = QUESTIONS_AND_ANSWERS["want_some"]["answer"]
    actual = home.get_answer_to_question_want_some()
    assert actual == answer

@allure.title("При нажатии на третий вопрос, открывается соответствующий текст ответа")
def test_question_and_answer_rent_time(driver):
    home = HomePage(driver)
    home.click_popup_button()
    home.scroll_to_faq_section()
    assert home.is_question_visible(HomePageLocators.QUESTION_RENT_TIME)
    home.click_question_rent_time()
    assert home.is_answer_visible(HomePageLocators.ANSWER_RENT_TIME)
    answer = QUESTIONS_AND_ANSWERS["rent_time"]["answer"]
    actual = home.get_answer_to_question_rent_time()
    assert actual == answer
                         
@allure.title("При нажатии на четвертый вопрос, открывается соответствующий текст ответа")    
def test_question_and_answer_order_today(driver):
    home = HomePage(driver)
    home.click_popup_button()
    home.scroll_to_faq_section()
    assert home.is_question_visible(HomePageLocators.QUESTION_ORDER_TODAY)
    home.click_question_order_today()
    assert home.is_answer_visible(HomePageLocators.ANSWER_ORDER_TODAY)
    answer = QUESTIONS_AND_ANSWERS["order_today"]["answer"]
    actual = home.get_answer_to_question_order_today()
    assert actual == answer

@allure.title("При нажатии на пятый вопрос, открывается соответствующий текст ответа")   
def test_question_and_answer_extend_or_return(driver):
    home = HomePage(driver)
    home.click_popup_button()
    home.scroll_to_faq_section()
    assert home.is_question_visible(HomePageLocators.QUESTION_EXTEND_OR_RETURN)
    home.click_question_extend_or_return()
    assert home.is_answer_visible(HomePageLocators.ANSWER_EXTEND_OR_RETURN)
    answer = QUESTIONS_AND_ANSWERS["extend_or_return"]["answer"]
    actual = home.get_answer_to_question_extend_or_return()
    assert actual == answer

@allure.title("При нажатии на шестой вопрос, открывается соответствующий текст ответа")
def test_question_and_answer_bring_charger(driver):
    home = HomePage(driver)
    home.click_popup_button()
    home.scroll_to_faq_section()
    assert home.is_question_visible(HomePageLocators.QUESTION_BRING_CHARGER)
    home.click_question_bring_charger()
    assert home.is_answer_visible(HomePageLocators.ANSWER_BRING_CHARGER)
    answer = QUESTIONS_AND_ANSWERS["bring_charger"]["answer"]
    actual = home.get_answer_to_question_bring_charger()
    assert actual == answer

@allure.title("При нажатии на седьмой вопрос, открывается соответствующий текст ответа")
def test_question_and_answer_cancel(driver):
    home = HomePage(driver)
    home.click_popup_button()
    home.scroll_to_faq_section()
    assert home.is_question_visible(HomePageLocators.QUESTION_CANCEL)
    home.click_question_cancel()
    assert home.is_answer_visible(HomePageLocators.ANSWER_CANCEL)
    answer = QUESTIONS_AND_ANSWERS["cancel"]["answer"]
    actual = home.get_answer_to_question_cancel()
    assert actual == answer

@allure.title("При нажатии на восьмой вопрос, открывается соответствующий текст ответа")
def test_question_and_answer_live_outside_mkad(driver):
    home = HomePage(driver)
    home.click_popup_button()
    home.scroll_to_faq_section()
    assert home.is_question_visible(HomePageLocators.QUESTION_LIVE_OUTSIDE_MKAD)
    home.click_question_live_outside_mkad()
    assert home.is_answer_visible(HomePageLocators.ANSWER_LIVE_OUTSIDE_MKAD)
    answer = QUESTIONS_AND_ANSWERS["live_outside_mkad"]["answer"]
    actual = home.get_answer_to_question_live_outside_mkad()
    assert actual == answer