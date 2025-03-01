from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

driver = webdriver.Chrome(service =ChromeService(ChromeDriverManager().install()))
driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
driver.maximize_window()

# Ввод значения 45 в поле задержки
delay_input = driver.find_element(By.CSS_SELECTOR, "#delay")
delay_input.clear()
delay_input.send_keys("45")

# Нажатие кнопок 7 + 8
driver.find_element(By.XPATH, "//span[text()='7']").click()
driver.find_element(By.XPATH, "//span[text()='+']").click()
driver.find_element(By.XPATH, "//span[text()='8']").click()


# Ожидание, пока кнопка "=" станет кликабельной
equals_button = WebDriverWait(driver, 46).until(
    EC.element_to_be_clickable((By.XPATH, "//span[text()='=']"))
)

# Прокрутка страницы до кнопки "="
driver.execute_script("arguments[0].scrollIntoView(true);", equals_button)

# Использование JavaScript для клика
driver.execute_script("arguments[0].click();", equals_button)

# Ожидание появления результата и проверка
result = WebDriverWait(driver, 50).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15")
)
assert result, "Результат не равен 15"

# Закрытие браузера
driver.quit()