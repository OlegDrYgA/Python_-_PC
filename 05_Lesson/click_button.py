from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Инициализация драйвера Chrome
driver = webdriver.Chrome()

try:
    # Открытие страницы
    driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

    # Клик по кнопке "Add Element" 5 раз
    add_button = driver.find_element(By.XPATH, "//button[text()='Add Element']")
    for _ in range(5):
        add_button.click()
        time.sleep(0.5)  # Небольшая пауза между кликами

    # Сбор списка кнопок "Delete"
    delete_buttons = driver.find_elements(By.CLASS_NAME, "added-manually")

    # Вывод размера списка кнопок "Delete"
    print(f"Количество кнопок 'Delete': {len(delete_buttons)}")

finally:
    # Закрытие браузера
    driver.quit()