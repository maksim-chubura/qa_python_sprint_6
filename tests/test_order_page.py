import pytest
from pages.home_page import HomePage
from pages.order_page import OrderPage
from helpers import RandomDataGenerator
import allure

test_data = [
    ("up", "Спортивная", "трое суток", "black"),
    ("down", "Лубянка", "семеро суток", "grey")
]

@allure.title("Параметризированный тест на создание заказа")
@pytest.mark.parametrize("order_button,metro_station,rental_period,scooter_color", test_data)
def test_order_creation(driver, order_button, metro_station, rental_period, scooter_color):
    home = HomePage(driver)
    order = OrderPage(driver)
    home.click_popup_button()
    
    if order_button == "up":
        order.click_button_order_up()
    else:
        order.click_button_order_down()

    order.fill_name(RandomDataGenerator.get_random_name())
    order.fill_last_name(RandomDataGenerator.get_random_last_name())
    order.fill_address(RandomDataGenerator.get_random_address())
    order.choose_metro_station(metro_station)
    order.fill_phone_number(RandomDataGenerator.get_random_phone())
    order.click_next_button()

    order.fill_date(RandomDataGenerator.get_random_date())
    order.select_rental_period(rental_period)
    
    if scooter_color == "black":
        order.select_scooter_color_black()
    else:
        order.select_scooter_color_grey()
        
    order.fill_comment(RandomDataGenerator.get_random_comment())
    order.click_button_back()
    order.click_next_button()

    order.complete_order()
    order.confirm_order()
    order.click_button_yes()
    order.is_order_successful()