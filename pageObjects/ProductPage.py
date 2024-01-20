from selenium.webdriver.common.by import By

from pageObjects.CartPage import CartPage


class ProductPage:
    product_link = (
        By.XPATH, "//div[@class='inventory_list']/div[@class='inventory_item']//div[text()='Sauce Labs Bike Light']")
    add_to_cart_button = (By.XPATH, "//button[text()='Add to cart']")

    def __init__(self, driver):
        self.driver = driver

    def add_product_to_cart(self):
        self.driver.find_element(*ProductPage.product_link).click()
        self.driver.find_element(*ProductPage.add_to_cart_button).click()
        return CartPage(self.driver)
