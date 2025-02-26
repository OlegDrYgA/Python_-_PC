from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep #импортировали метод из пакета
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service =ChromeService(ChromeDriverManager().install()))

try:
    # Переход на страницу
    driver.get("http://uitestingplayground.com/ajax")

    ajax_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "ajaxButton"))
    )
    ajax_button.click()

    # Ожидание появления зеленой плашки и получение текста
    green_banner = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CLASS_NAME, "bg-success"))
    )
    banner_text = green_banner.text

    # Вывод текста в консоль
    print(banner_text)

finally:
    # Закрытие браузера
    driver.quit()