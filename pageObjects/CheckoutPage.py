from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class CheckoutPage:
    checkout_label = (By.XPATH, "//span[text()='Checkout: Your Information']")
    name_text = (By.NAME, "firstName")
    last_name_text = (By.NAME, "lastName")
    zip_postal_code_text = (By.NAME, "postalCode")
    continue_button = (By.CSS_SELECTOR, "#continue")
    finish_button = (By.XPATH, "//button[text()='Finish']")
    thankyou_label = (By.XPATH, "//h2[text()='Thank you for your order!']")
    back_to_home_button = (By.XPATH,"//button[text()='Back Home']")


    def __init__(self, driver):
        self.driver = driver

    def complete_checkout(self, get_data):
        wait = WebDriverWait(self.driver, 10)
        wait.until(
            expected_conditions.presence_of_element_located((By.XPATH, "//span[text()='Checkout: Your Information']")))
        self.driver.find_element(*CheckoutPage.name_text).send_keys(get_data["firstname"])
        self.driver.find_element(*CheckoutPage.last_name_text).send_keys(get_data["lastname"])
        self.driver.find_element(*CheckoutPage.zip_postal_code_text).send_keys(get_data["zipcode"])
        self.driver.find_element(*CheckoutPage.continue_button).click()
        self.driver.find_element(*CheckoutPage.finish_button).click()
        wait.until(
            expected_conditions.presence_of_element_located((By.XPATH, "//h2[text()='Thank you for your order!']")))
        self.driver.find_element(*CheckoutPage.back_to_home_button).click()
