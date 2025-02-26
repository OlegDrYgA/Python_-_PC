from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep #импортировали метод из пакета
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service =ChromeService(ChromeDriverManager().install()))

try:
    # Переход на сайт
    driver.get("http://uitestingplayground.com/textinput")

    # Нахождение поля ввода по ID и ввод текста "SkyPro"
    input_field = driver.find_element(By.ID, "newButtonName")
    input_field.clear()
    input_field.send_keys("SkyPro")

    # Нахождение кнопки по ID и нажатие на нее
    button = driver.find_element(By.ID, "updatingButton")
    button.click()

    # Получение текста кнопки и вывод в консоль
    button_text = button.text
    print(button_text)

finally:
    # Закрытие браузера
    driver.quit()