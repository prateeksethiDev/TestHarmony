from utilities.BaseClass import BaseClass


class ProductPage():

    def __init__(self, driver):
        self.driver = driver


    def select_Product(self, product_text):
        locator = self.get_dynamic_locator("xpath",
                                                "//div[@class='inventory_list']/div[@class='inventory_item']//div[text()='{}']".format(
                                                    product_text))
        self.driver.find_element(locator).click()
