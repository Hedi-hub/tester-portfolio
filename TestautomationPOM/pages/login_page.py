from selenium.webdriver.common.by import By
from .base_page import BasePage


class LoginPage(BasePage):

    # Locators
    USERNAME_FIELD = (By.XPATH, "//input[@type='email']")
    PASSWORD_FIELD = (By.XPATH, "//input[@type='password']")
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")
    ERROR_ALERT = (By.XPATH, "//div[@role='status']")

    def __init__(self, driver):
        super().__init__(driver)

    def set_username(self, username):
        """ Enter the username """
        self.enter_text(self.USERNAME_FIELD, username)

    def set_password(self, password):
        """ Enter the password """
        self.enter_text(self.PASSWORD_FIELD, password)

    def click_login(self):
        """ Click the login button """
        self.click(self.LOGIN_BUTTON)

    def login(self, username, password):
        self.set_username(username)
        self.set_password(password)
        self.click_login()

    def get_error_message(self):
        element = self.find_element(self.ERROR_ALERT)
        return element.text
