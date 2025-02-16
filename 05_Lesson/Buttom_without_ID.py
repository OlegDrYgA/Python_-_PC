from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver_path = r'D:\Старый пенс\chromedriver-win64\chromedriver.exe'  #
url = 'http://uitestingplayground.com/dynamicid'

# Создаем экземпляр веб-драйвера
driver = webdriver.Chrome()

# Открываем страницу
driver.get(url)

# Ждем, чтобы страница полностью загрузилась
time.sleep(2)

# Находим синюю кнопку и кликаем по ней
blue_button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
blue_button.click()

# Ждем, чтобы увидеть результат клика
time.sleep(2)

# Закрываем браузер
driver.quit()