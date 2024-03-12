import pytest

from pageObjects.LoginPage import LoginPage
from tests.test_add_product_to_cart import TestAddItemToCart
from utilities.BaseClass import BaseClass


@pytest.mark.run(order=1)
class TestAddItem(BaseClass):
    product_page = None

    def test_add_item(self):
        loginPage = LoginPage(self.driver)
        loginPage.get_user_name().send_keys("standard_user")
        loginPage.get_password().send_keys("secret_sauce")
        loginPage.get_clickbtn()


