from selenium.webdriver.common.by import By
from TestautomationPOM.pages.base_page import BasePage
from TestautomationPOM.utils.constants import LOGIN_URL


class LoginPage(BasePage):
    """ Page Object Model for the Login Page """

    # Updated Locators using `placeholder` and `class`
    EMAIL_INPUT = (By.XPATH, "//input[@type='email' and @placeholder='Email address']")
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password' and @placeholder='Password']")
    LOGIN_BUTTON = (By.CLASS_NAME, "submit-btn")  # Class name for login button

    def __init__(self, driver):
        """ Initialize LoginPage with driver and open login URL """
        super().__init__(driver)
        self.driver.get(LOGIN_URL)

    def enter_email(self, email):
        """ Enter email into the input field """
        self.enter_text(self.EMAIL_INPUT, email)

    def enter_password(self, password):
        """ Enter password into the input field """
        self.enter_text(self.PASSWORD_INPUT, password)

    def click_login(self):
        """ Click the login button """
        self.click(self.LOGIN_BUTTON)

    def login(self, email, password):
        """ Perform login with given credentials """
        self.enter_email(email)
        self.enter_password(password)
        self.click_login()

    def is_logged_in(self):
        """ Check if login was successful by verifying the presence of the profile icon """
        return self.find_element((By.CLASS_NAME, "headerIcon"))
