import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from login_page import LoginPage
from shop_page import ShopPage
from cart_page import CartPage
from checkout_page import CheckoutPage

class ShopTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("https://www.saucedemo.com/")

    def test_shop(self):
        # Авторизация
        login_page = LoginPage(self.driver)
        login_page.enter_username("standard_user")
        login_page.enter_password("secret_sauce")
        login_page.click_login()

        # Добавление товаров в корзину
        shop_page = ShopPage(self.driver)
        shop_page.add_items_to_cart()
        shop_page.go_to_cart()

        # Переход к оформлению заказа
        cart_page = CartPage(self.driver)
        cart_page.click_checkout()

        # Заполнение формы
        checkout_page = CheckoutPage(self.driver)
        checkout_page.fill_form("John", "Doe", "12345")
        checkout_page.click_continue()

        # Проверка итоговой стоимости
        total_price = checkout_page.get_total_price()
        self.assertEqual(total_price, "Total: $58.29")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()