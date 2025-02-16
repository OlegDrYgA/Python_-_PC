from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
import time


geckodriver_path = r'D:\CSKY-PRO-учеба\geckodriver-v0.35.0-win32\geckodriver.exe'

# Настройка опций для Firefox
firefox_options = Options()
firefox_options.headless = False  # Если нужно запустить браузер в фоновом режиме, установите True


firefox_options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'


service = Service(geckodriver_path)
driver = webdriver.Firefox(service=service, options=firefox_options)

try:
    # Открываем страницу
    driver.get("http://the-internet.herokuapp.com/login")

    # Находим поле ввода для имени пользователя и вводим значение
    username_field = driver.find_element(By.NAME, "username")
    username_field.send_keys("tomsmith")

    # Находим поле ввода для пароля и вводим значение
    password_field = driver.find_element(By.NAME, "password")
    password_field.send_keys("SuperSecretPassword!")

    # Находим кнопку Login и нажимаем на нее
    login_button = driver.find_element(By.TAG_NAME, "button")
    login_button.click()

    # Небольшая пауза для наглядности
    time.sleep(3)

finally:
    # Закрываем браузер
    driver.quit()