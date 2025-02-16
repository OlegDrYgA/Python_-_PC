from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver_path = r'D:\Старый пенс\chromedriver-win64\chromedriver.exe'

# Создаем экземпляр драйвера
driver = webdriver.Chrome() # Убедитесь, что путь к драйверу корректен

try:
    # Открываем страницу
    driver.get("http://uitestingplayground.com/classattr")

    # Явное ожидание, пока кнопка не станет доступной
    blue_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "btn-primary"))
    )

    # Кликаем на синюю кнопку
    blue_button.click()

    # Небольшая пауза для наглядности
    time.sleep(3)

finally:
    # Закрываем браузер
    driver.quit()