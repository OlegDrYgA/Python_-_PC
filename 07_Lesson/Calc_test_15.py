import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from CalcPage import CalcPage

@pytest.fixture
def browser():
    """Фикстура для инициализации и закрытия браузера."""
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield driver
    driver.quit()

def test_calculator_result_after_delay(browser):
    """Тест проверяет, что результат вычисления 7 + 8 равен 15 после задержки."""
    # Открываем страницу калькулятора
    browser.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    # Создаем объект страницы
    calc_page = CalcPage(browser)

    # Устанавливаем задержку
    calc_page.set_delay("45")

    # Выполняем вычисления: 7 + 8 =
    calc_page.click_button_7()
    calc_page.click_button_plus()
    calc_page.click_button_8()
    calc_page.click_button_equals()

    # Проверяем, что результат равен 15
    assert calc_page.get_result(), "Результат не равен 15"