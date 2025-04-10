import allure
import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.delay_input = (By.CSS_SELECTOR, "#delay")
        self.result_field = (By.CSS_SELECTOR, ".screen")

    def set_delay(self, delay: int) -> None:
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.delay_input)
        )
        element.clear()
        element.send_keys(str(delay))

    def click_button(self, button_text: str) -> None:
        locator = (By.XPATH, f"//span[text()='{button_text}']")
        for attempt in range(3):
            try:
                element = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable(locator)
                )
                self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
                self.driver.execute_script("arguments[0].click();", element)
                return
            except Exception as e:
                if attempt == 2:
                    raise e
                time.sleep(1)

    def get_result(self, timeout: int = 60) -> str:
        try:
            WebDriverWait(self.driver, timeout).until(
                lambda d: d.find_element(*self.result_field).text not in ["", "7", "7+", "7+8"]
            )
            return self.driver.find_element(*self.result_field).text
        except TimeoutException:
            return self.driver.find_element(*self.result_field).text


@allure.feature("Калькулятор")
class TestCalculator:
    @allure.title("Проверка работы калькулятора с задержкой")
    def test_calculator_with_delay(self, browser):
        browser.maximize_window()
        browser.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        calculator = CalculatorPage(browser)

        calculator.set_delay(45)

        calculator.click_button("7")
        calculator.click_button("+")
        calculator.click_button("8")
        calculator.click_button("=")

        result = calculator.get_result()
        assert result == "15", f"Ожидаемый результат 15, получен {result}"
