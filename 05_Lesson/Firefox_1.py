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
    driver.get("http://the-internet.herokuapp.com/entry_ad")

    # Ждем, пока модальное окно загрузится
    time.sleep(2)

    # Находим кнопку "Close" в модальном окне и нажимаем ее
    close_button = driver.find_element(By.CSS_SELECTOR, "div.modal-footer p")
    close_button.click()

    # Ждем немного, чтобы увидеть результат
    time.sleep(2)

finally:
    # Закрываем браузер
    driver.quit()