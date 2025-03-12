import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from Page_found import FormPage

@pytest.fixture(scope="function")
def driver():
    """Фикстура для инициализации и закрытия драйвера."""
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()

def test_form_validation(driver):
    # Инициализация страницы
    page = FormPage(driver)
    page.open()

    # Заполнение полей
    fields_values = {
        'first_name': 'Иван',
        'last_name': 'Петров',
        'address': 'Ленина, 55-3',
        'email': 'test@skypro.com',
        'phone': '+7985899998787',
        'city': 'Москва',
        'country': 'Россия',
        'job_position': 'QA',
        'company': 'SkyPro'
    }

    for field, value in fields_values.items():
        page.fill_field(field, value)

    # Нажатие кнопки Submit
    page.submit()

    # Проверка подсветки полей
    assert "alert-danger" in page.get_field_class('zip_code'), "Поле Zip code не подсвечено красным"

    valid_fields = ['first_name', 'last_name', 'address', 'email', 'phone', 'city', 'country', 'job_position', 'company']
    for field in valid_fields:
        assert "alert-success" in page.get_field_class(field), f"Поле {field} не подсвечено зеленым"