from pageObjects.LoginPage import LoginPage
from utilities.BaseClass import BaseClass


class TestAddItem(BaseClass):

    def test_add_item(self):
        loginPage = LoginPage(self.driver)
        loginPage.get_user_name().send_keys("standard_user")
        loginPage.get_password().send_keys("secret_sauce")
        product_page = loginPage.get_clickbtn()
        self.is_label_present("Products")

