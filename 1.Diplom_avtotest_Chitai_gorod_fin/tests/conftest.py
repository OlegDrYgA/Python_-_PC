import pytest
from selenium import webdriver
from pages.main_page import MainPage
from config.config import Config


@pytest.fixture(scope="function")
def browser():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


@pytest.fixture
def main_page(browser):
    page = MainPage(browser)
    page.open()
    page.close_popups()
    return page


# Добавляем фикстуру driver для совместимости со старыми тестами
@pytest.fixture
def driver(browser):
    return browser