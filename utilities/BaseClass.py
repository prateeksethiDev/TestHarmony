import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseClass:

    def verify_link_presence(self, linktext, timeout=10):
        WebDriverWait(self.driver, timeout).until(ec.presence_of_element_located((By.LINK_TEXT, linktext)))

    def is_label_present(self, label_text, timeout=10):
        try:
            label_locator = (By.XPATH, f"//*[contains(text(), '{label_text}')]")
            label_element = WebDriverWait(self.driver, timeout).until(
                ec.presence_of_element_located(label_locator)
            )
            print(f"Label '{label_text}' found on the page.")
            return True
        except Exception as e:
            print(f"Label '{label_text}' not found on the page.")
            return False

    def get_dynamic_locator(self, locator_type, locator_string):
        dynamic_locator = ""
        if locator_type == "css":
            dynamic_locator = (By.CSS_SELECTOR, locator_string)
        elif locator_type == "xpath":
            dynamic_locator = (By.XPATH, locator_string)

        return dynamic_locator
