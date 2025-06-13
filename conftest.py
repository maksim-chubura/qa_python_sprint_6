import pytest
from urls import Urls
from selenium import webdriver


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.get(Urls.MAIN_PAGE)
    yield driver
    driver.quit()