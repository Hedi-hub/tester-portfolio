# pages/base_page.py
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException


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

    def save_screenshot(self, filename="debug_screenshot.png"):
        """ Save a screenshot to the 'screenshots' folder for debugging """
        screenshot_folder = "TestautomationPOM/screenshots"
        os.makedirs(screenshot_folder, exist_ok=True)  # Ensure folder exists

        screenshot_path = os.path.join(screenshot_folder, filename)
        success = self.driver.save_screenshot(screenshot_path)

        if success:
            print(f"Screenshot saved: {screenshot_path}")
        else:
            print("Failed to save screenshot!")

        return success

    def get_element_text(self, locator):
        """Retrieve text from a web element."""
        try:
            element = WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_element_located(locator)
            )
            return element.text
        except (TimeoutException, NoSuchElementException):
            return None  # Or raise an error if needed
