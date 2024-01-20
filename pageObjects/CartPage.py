from selenium.webdriver.common.by import By

from pageObjects.CheckoutPage import CheckoutPage


class CartPage:
    cart_icon = (By.CSS_SELECTOR, "span.shopping_cart_badge")
    checkout_button = (By.XPATH,"//button[text()='Checkout']")

    def __init__(self, driver):
        self.driver = driver

    def click_on_cart_icon(self):
        self.driver.find_element(*CartPage.cart_icon).click()

    def click_on_checkout(self):
        self.driver.find_element(*CartPage.checkout_button).click()
        return CheckoutPage(self.driver)

