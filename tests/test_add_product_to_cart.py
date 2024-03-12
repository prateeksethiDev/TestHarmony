import pytest
from pageObjects.ProductPage import ProductPage
from testData.CheckoutPageData import CheckoutPageData
from utilities.BaseClass import BaseClass


@pytest.mark.run(order=2)
class TestAddItemToCart(BaseClass):
    cart_page = None
    checkout_page = None
    product_page = None

    def test_add_product_to_cart(self, get_data):
        log = self.create_logger()
        product_page = ProductPage(self.driver)
        self.is_label_present("Products")
        cart_page = product_page.add_product_to_cart()
        log.info("Clicking on cart icon")
        cart_page.click_on_cart_icon()
        checkout_page = cart_page.click_on_checkout()
        log.info("Providing required details : firstname : " + get_data["firstname"] + " lastname: " + get_data[
            "lastname"] + " zipcode: " + str(get_data["zipcode"]))
        checkout_page.complete_checkout(get_data)

    @pytest.fixture(params=CheckoutPageData.test_checkout_page_data)
    def get_data(self, request):
        return request.param
