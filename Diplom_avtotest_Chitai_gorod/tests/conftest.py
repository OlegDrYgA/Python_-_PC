import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from config.config import Config


@pytest.fixture(scope="function")
def driver():
    # Настройка ChromeOptions
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-extensions")

    # Инициализация драйвера
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options
    )

    # Установка неявного ожидания
    driver.implicitly_wait(Config.DEFAULT_TIMEOUT)

    yield driver

    # Закрытие браузера после теста
    driver.quit()