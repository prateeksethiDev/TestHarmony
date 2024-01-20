from pageObjects.LoginPage import LoginPage
from utilities.BaseClass import BaseClass


class TestAddItem(BaseClass):
    product_page=None
    cart_page=None
    checkout_page=None

    def test_add_item(self):
        loginPage = LoginPage(self.driver)
        loginPage.get_user_name().send_keys("standard_user")
        loginPage.get_password().send_keys("secret_sauce")
        TestAddItem.product_page = loginPage.get_clickbtn()
        self.is_label_present("Products")

    def test_add_product_to_cart(self):
        TestAddItem.cart_page = self.product_page.add_product_to_cart()
        TestAddItem.cart_page.click_on_cart_icon()
        checkout_page = TestAddItem.cart_page.click_on_checkout()
        checkout_page.complete_checkout()
