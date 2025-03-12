from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from TestautomationPOM.pages.base_page import BasePage
from TestautomationPOM.utils.constants import REGISTER_URL


class RegistrationPage(BasePage):

    # Locators
    FULLNAME_INPUT = (By.XPATH, "//input[@placeholder='Full Name']")
    EMAIL_INPUT = (By.XPATH, "//input[@placeholder='Email address']")
    PASSWORD_INPUT = (By.XPATH, "//input[@placeholder='Password']")
    SIGNUP_BUTTON = (By.XPATH, "//button[contains(@class, 'submit-btn') and contains(text(), 'Sign Up')]")
    SUCCESS_MESSAGE = (By.XPATH, "//div[contains(@class, 'go3958317564') and contains(text(), 'Registration "
                                 "successful')]")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(REGISTER_URL)

    def enter_fullname(self, fullname):
        """ Enter full name in the registration form """
        self.enter_text(self.FULLNAME_INPUT, fullname)

    def enter_email(self, email):
        """ Enter email address """
        self.enter_text(self.EMAIL_INPUT, email)

    def enter_password(self, password):
        """ Enter password """
        self.enter_text(self.PASSWORD_INPUT, password)

    def click_signup(self):
        """ Click the Sign Up button """
        self.click(self.SIGNUP_BUTTON)

    from selenium.common.exceptions import NoSuchElementException

    def is_registration_successful(self):
        """ Check if the registration success message is present. """
        try:
            self.find_element(self.SUCCESS_MESSAGE)
            return True
        except NoSuchElementException:
            print("Success message not found. Registration may have failed.")
        except TimeoutException:
            print("⏳ Timeout while waiting for the success message.")
        return False

    def register(self, fullname, email, password):
        """ Perform the full registration process """
        self.enter_fullname(fullname)
        self.enter_email(email)
        self.enter_password(password)
        self.click_signup()
