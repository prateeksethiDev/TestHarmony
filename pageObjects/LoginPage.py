from selenium.webdriver.common.by import By
from pageObjects.ProductPage import ProductPage
from utilities.BaseClass import BaseClass


class LoginPage():

    username = (By.ID, "user-name")
    password = (By.ID, "password")
    login_button = (By.ID, "login-button")

    def __init__(self, driver):
        self.driver = driver

    def get_user_name(self):
        return self.driver.find_element(*LoginPage.username)

    def get_password(self):
        return self.driver.find_element(*LoginPage.password)

    def get_clickbtn(self):
        self.driver.find_element(*LoginPage.login_button).click()
        return ProductPage(self.driver)
