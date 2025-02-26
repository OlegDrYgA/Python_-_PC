from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
import time

# Укажите правильный путь к geckodriver.exe
geckodriver_path = r'D:\CSKY-PRO-учеба\geckodriver-v0.35.0-win32\geckodriver.exe'

# Настройка опций для Firefox
firefox_options = Options()
firefox_options.headless = False  # Если нужно запустить браузер в фоновом режиме, установите True

# Укажите путь к Firefox, если он установлен в нестандартное место
firefox_options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'

# Инициализация драйвера
service = Service(geckodriver_path)
driver = webdriver.Firefox(service=service, options=firefox_options)

try:
    # Открываем страницу
    driver.get("http://the-internet.herokuapp.com/inputs")

    # Находим поле ввода
    input_field = driver.find_element(By.TAG_NAME, "input")

    # Вводим текст '1000'
    input_field.send_keys("1000")
    time.sleep(1)  # Небольшая пауза для наглядности

    # Очищаем поле
    input_field.clear()
    time.sleep(1)  # Небольшая пауза для наглядности

    # Вводим текст '999'
    input_field.send_keys("999")
    time.sleep(1)  # Небольшая пауза для наглядности

finally:
    # Закрываем браузер
    driver.quit()