import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )

    parser.addoption(
        "--environment",
        action="store",
        default="qa",
        help="Specify the environment (e.g., dev, staging, qa)"
    )


# factory design pattern for creation of different driver instance abstracted behing webdriver.
@pytest.fixture(scope="session")
def setup(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name.lower() == "chrome":
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif browser_name.lower() == "firefox":
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    elif browser_name.lower() == "edge":
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    else:
        raise ValueError("Unsupported browser name: {}".format(browser_name))

    driver.maximize_window()

    # dependency injection design pattern
    # request.cls.driver = driver
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()
