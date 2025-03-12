from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FormPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"

        # Локаторы для полей ввода
        self.input_locators = {
            'first_name': (By.NAME, 'first-name'),
            'last_name': (By.NAME, 'last-name'),
            'address': (By.NAME, 'address'),
            'email': (By.NAME, 'e-mail'),
            'phone': (By.NAME, 'phone'),
            'city': (By.NAME, 'city'),
            'country': (By.NAME, 'country'),
            'job_position': (By.NAME, 'job-position'),
            'company': (By.NAME, 'company'),
            'submit_button': (By.CSS_SELECTOR, 'button[type="submit"]')
        }

        # Локаторы для подсвеченных полей после отправки формы
        self.alert_locators = {
            'first_name': (By.ID, 'first-name'),  # Пример: <div id="first-name" class="alert alert-success">
            'last_name': (By.ID, 'last-name'),
            'address': (By.ID, 'address'),
            'email': (By.ID, 'e-mail'),
            'phone': (By.ID, 'phone'),
            'city': (By.ID, 'city'),
            'country': (By.ID, 'country'),
            'job_position': (By.ID, 'job-position'),
            'company': (By.ID, 'company'),
            'zip_code': (By.ID, 'zip-code')  # Поле Zip code
        }

    def open(self):
        """Открывает страницу формы."""
        self.driver.get(self.url)

    def fill_field(self, field, value):
        """Заполняет поле формы."""
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.input_locators[field])
        )
        element.clear()
        element.send_keys(value)

    def submit(self):
        """Нажимает кнопку Submit с прокруткой и ожиданием."""
        submit_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.input_locators['submit_button'])
        )
        # Прокрутка до элемента
        self.driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
        # Клик через JavaScript
        self.driver.execute_script("arguments[0].click();", submit_button)

    def get_field_class(self, field):
        """Возвращает класс поля для проверки подсветки."""
        element = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(self.alert_locators[field])
        )
        return element.get_attribute('class')