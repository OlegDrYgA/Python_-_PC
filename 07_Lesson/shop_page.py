from selenium.webdriver.common.by import By
class ShopPage:
    def __init__(self, driver):
        self.driver = driver
        self.add_backpack = (By.ID, "add-to-cart-sauce-labs-backpack")
        self.add_tshirt = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
        self.add_onesie = (By.ID, "add-to-cart-sauce-labs-onesie")
        self.cart_icon = (By.CLASS_NAME, "shopping_cart_link")

    def add_items_to_cart(self):
        self.driver.find_element(*self.add_backpack).click()
        self.driver.find_element(*self.add_tshirt).click()
        self.driver.find_element(*self.add_onesie).click()

    def go_to_cart(self):
        self.driver.find_element(*self.cart_icon).click()