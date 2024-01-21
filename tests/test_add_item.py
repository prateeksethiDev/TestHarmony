import pytest
from pageObjects.LoginPage import LoginPage
from testData.CheckoutPageData import CheckoutPageData
from utilities.BaseClass import BaseClass


class TestAddItem(BaseClass):
    product_page = None
    cart_page = None
    checkout_page = None

    def test_add_item(self):
        loginPage = LoginPage(self.driver)
        loginPage.get_user_name().send_keys("standard_user")
        loginPage.get_password().send_keys("secret_sauce")
        TestAddItem.product_page = loginPage.get_clickbtn()
        self.is_label_present("Products")

    def test_add_product_to_cart(self, get_data):
        log=self.create_logger()
        TestAddItem.cart_page = self.product_page.add_product_to_cart()
        log.info("Clicking on cart icon")
        TestAddItem.cart_page.click_on_cart_icon()
        checkout_page = TestAddItem.cart_page.click_on_checkout()
        log.info("Providing required details : firstname : "+get_data["firstname"]+" lastname: "+get_data["lastname"]+ " zipcode: "+str(get_data["zipcode"]))
        checkout_page.complete_checkout(get_data)

    @pytest.fixture(params=CheckoutPageData.test_checkout_page_data)
    def get_data(self, request):
        return request.param
