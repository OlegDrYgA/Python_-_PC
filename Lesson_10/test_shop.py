import allure
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException, TimeoutException

class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.delay_input = (By.CSS_SELECTOR, "#delay")
        self.result_field = (By.CSS_SELECTOR, ".screen")

    def set_delay(self, delay: int) -> None:
        """Установка задержки вычислений"""
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.delay_input)
        )
        element.clear()
        element.send_keys(str(delay))

    def click_button(self, button_text: str) -> None:
        """Нажатие кнопки с обработкой исключений"""
        locator = (By.XPATH, f"//span[text()='{button_text}']")
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(locator)
            )
            # Прокрутка к элементу перед кликом
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            element.click()
        except ElementClickInterceptedException:
            # Альтернативный способ клика через JavaScript
            element = self.driver.find_element(*locator)
            self.driver.execute_script("arguments[0].click();", element)

    def get_result(self, timeout: int = 60) -> str:
        """Получение результата с увеличенным таймаутом"""
        try:
            WebDriverWait(self.driver, timeout).until(
                lambda d: d.find_element(*self.result_field).text not in ["", "7+8"]
            )
            return self.driver.find_element(*self.result_field).text
        except TimeoutException:
            return self.driver.find_element(*self.result_field).text

@allure.feature("Калькулятор")
class TestCalculator:
    @allure.title("Проверка работы калькулятора с задержкой")
    def test_calculator_with_delay(self, browser):
        with allure.step("Открытие страницы калькулятора"):
            browser.maximize_window()
            browser.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
            calculator = CalculatorPage(browser)

        with allure.step("Установка задержки 45 секунд"):
            calculator.set_delay(45)

        with allure.step("Вычисление 7 + 8"):
            calculator.click_button("7")
            calculator.click_button("+")
            calculator.click_button("8")
            calculator.click_button("=")

        with allure.step("Проверка результата"):
            result = calculator.get_result()
            assert result == "15", f"Ожидаемый результат 15, получен {result}"