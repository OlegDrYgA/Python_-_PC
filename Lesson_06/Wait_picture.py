from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service =ChromeService(ChromeDriverManager().install()))

try:
    # Переход на сайт
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

    # Ожидание появления текста "Done" в элементе <body>
    WebDriverWait(driver, 15).until(
        EC.text_to_be_present_in_element((By.TAG_NAME, "body"), "Done")
    )

    # Получение значения атрибута src у 3-й картинки
    images = driver.find_elements(By.TAG_NAME, "img")
    if len(images) >= 3:
        third_image_src = images[2].get_attribute("src")
        print("SRC третьей картинки:", third_image_src)
    else:
        print("Третья картинка не найдена")

finally:
    # Закрытие браузера
    driver.quit()