# lesson_10/test_saucedemo.py
import allure
from selenium.webdriver.common.by import By


class LoginPage:
    """Page Object для страницы авторизации"""

    def __init__(self, driver):
        self.driver = driver
        self.username_field = (By.ID, "user-name")
        self.password_field = (By.ID, "password")
        self.login_button = (By.ID, "login-button")

    def login(self, username: str, password: str) -> None:
        """Выполнить вход в систему

        Args:
            username: имя пользователя
            password: пароль
        """
        self.driver.find_element(*self.username_field).send_keys(username)
        self.driver.find_element(*self.password_field).send_keys(password)
        self.driver.find_element(*self.login_button).click()


class InventoryPage:
    """Page Object для страницы товаров"""

    def __init__(self, driver):
        self.driver = driver
        self.item_add_buttons = {
            "backpack": (By.ID, "add-to-cart-sauce-labs-backpack"),
            "bolt-t-shirt": (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"),
            "onesie": (By.ID, "add-to-cart-sauce-labs-onesie")
        }
        self.cart_button = (By.CLASS_NAME, "shopping_cart_link")

    def add_item_to_cart(self, item_name: str) -> None:
        """Добавить товар в корзину

        Args:
            item_name: название товара (backpack, bolt-t-shirt, onesie)
        """
        self.driver.find_element(*self.item_add_buttons[item_name]).click()

    def go_to_cart(self) -> None:
        """Перейти в корзину"""
        self.driver.find_element(*self.cart_button).click()


class CartPage:
    """Page Object для страницы корзины"""

    def __init__(self, driver):
        self.driver = driver
        self.checkout_button = (By.ID, "checkout")

    def checkout(self) -> None:
        """Начать оформление заказа"""
        self.driver.find_element(*self.checkout_button).click()


class CheckoutPage:
    """Page Object для страницы оформления заказа"""

    def __init__(self, driver):
        self.driver = driver
        self.first_name_field = (By.ID, "first-name")
        self.last_name_field = (By.ID, "last-name")
        self.zip_code_field = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.total_label = (By.CLASS_NAME, "summary_total_label")

    def fill_info(self, first_name: str, last_name: str, zip_code: str) -> None:
        """Заполнить информацию для оформления заказа

        Args:
            first_name: имя
            last_name: фамилия
            zip_code: почтовый индекс
        """
        self.driver.find_element(*self.first_name_field).send_keys(first_name)
        self.driver.find_element(*self.last_name_field).send_keys(last_name)
        self.driver.find_element(*self.zip_code_field).send_keys(zip_code)
        self.driver.find_element(*self.continue_button).click()

    def get_total(self) -> str:
        """Получить итоговую сумму

        Returns:
            Текст с итоговой суммой
        """
        return self.driver.find_element(*self.total_label).text


@allure.feature("Интернет-магазин")
@allure.severity(allure.severity_level.BLOCKER)
class TestSauceDemo:
    """Тесты для интернет-магазина"""

    @allure.title("Проверка оформления заказа")
    @allure.description("Тест проверяет корректность расчета итоговой суммы при оформлении заказа")
    def test_checkout_total(self, browser):
        with allure.step("Открыть сайт и авторизоваться"):
            browser.get("https://www.saucedemo.com/")
            login_page = LoginPage(browser)
            login_page.login("standard_user", "secret_sauce")

        with allure.step("Добавить товары в корзину"):
            inventory_page = InventoryPage(browser)
            inventory_page.add_item_to_cart("backpack")
            inventory_page.add_item_to_cart("bolt-t-shirt")
            inventory_page.add_item_to_cart("onesie")

        with allure.step("Перейти в корзину и начать оформление"):
            inventory_page.go_to_cart()
            cart_page = CartPage(browser)
            cart_page.checkout()

        with allure.step("Заполнить информацию для оформления"):
            checkout_page = CheckoutPage(browser)
            checkout_page.fill_info("John", "Doe", "12345")

        with allure.step("Проверить итоговую сумму"):
            total_text = checkout_page.get_total()
            assert total_text == "Total: $58.29", f"Ожидаемая сумма $58.29, получено {total_text}"