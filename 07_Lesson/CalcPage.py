from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CalcPage:
    def __init__(self, driver):
        self.driver = driver
        self.delay_input = (By.CSS_SELECTOR, "#delay")  # Поле для ввода задержки
        self.button_7 = (By.XPATH, "//span[text()='7']")  # Кнопка "7"
        self.button_plus = (By.XPATH, "//span[text()='+']")  # Кнопка "+"
        self.button_8 = (By.XPATH, "//span[text()='8']")  # Кнопка "8"
        self.button_equals = (By.XPATH, "//span[text()='=']")  # Кнопка "="
        self.result = (By.CSS_SELECTOR, ".screen")  # Поле с результатом

    def set_delay(self, delay):
        """Устанавливает задержку в поле ввода."""
        self.driver.find_element(*self.delay_input).clear()
        self.driver.find_element(*self.delay_input).send_keys(delay)

    def click_button_7(self):
        """Нажимает кнопку '7'."""
        self.driver.find_element(*self.button_7).click()

    def click_button_plus(self):
        """Нажимает кнопку '+'."""
        self.driver.find_element(*self.button_plus).click()

    def click_button_8(self):
        """Нажимает кнопку '8'."""
        self.driver.find_element(*self.button_8).click()

    def click_button_equals(self):
        """Нажимает кнопку '='."""
        self.driver.find_element(*self.button_equals).click()

    def get_result(self):
        """Ожидает появления результата и возвращает его."""
        return WebDriverWait(self.driver, 46).until(
            EC.text_to_be_present_in_element(self.result, "15")
        )