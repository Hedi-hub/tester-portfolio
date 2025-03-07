import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def driver():
    """ Set up and tear down the WebDriver """
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()