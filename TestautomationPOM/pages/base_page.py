# pages/base_page.py
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10

    def find_element(self, locator):
        """ Find a single web element with explicit wait """
        return WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_element_located(locator)
        )

    def find_elements(self, locator):
        """ Find multiple elements with explicit wait """
        return WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_all_elements_located(locator)
        )

    def click(self, locator):
        """ Click an element """
        element = self.find_element(locator)
        element.click()

    def enter_text(self, locator, text):
        """ Enter text information into an element """
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def get_page_url(self, url_to_be):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.url_to_be(url_to_be)
        )
