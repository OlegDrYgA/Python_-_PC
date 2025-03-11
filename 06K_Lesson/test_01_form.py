from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import pytest

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()

def test_form_validation(driver):
    # 1. Открытие страницы
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    # 2. Заполнение полей формы
    fields = {
        "first-name": "Иван",
        "last-name": "Петров",
        "address": "Ленина, 55-3",
        "e-mail": "test@skypro.com",
        "phone": "+7985899998787",
        "city": "Москва",
        "country": "Россия",
        "job-position": "QA",
        "company": "SkyPro"
    }

    for field_name, value in fields.items():
        field = driver.find_element(By.NAME, field_name)
        field.send_keys(value)

    # 3. Нажатие кнопки Submit с обработкой перехвата клика
    submit_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
    ActionChains(driver).move_to_element(submit_button).click().perform()

    # 4. Проверка подсветки Zip code
    zip_code = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "zip-code"))
    )
    assert "alert-danger" in zip_code.get_attribute("class")

    # 5. Проверка подсветки остальных полей
    success_fields = [
        "first-name", "last-name", "address", "e-mail",
        "phone", "city", "country", "job-position", "company"
    ]

    for field_id in success_fields:
        field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, field_id))
        )
        assert "alert-success" in field.get_attribute("class"), \
            f"Поле {field_id} не подсвечено зеленым"