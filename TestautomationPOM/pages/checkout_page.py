from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from TestautomationPOM.pages.base_page import BasePage
from TestautomationPOM.utils.constants import (
    CHECKOUT_PAGE_URL,
    DEFAULT_STREET_ADDRESS,
    DEFAULT_CITY,
    DEFAULT_POSTAL_CODE,
    DEFAULT_CARD_NUMBER,
    DEFAULT_NAME_ON_CARD,
    DEFAULT_EXPIRATION,
    DEFAULT_CVV,
    BASE_URL
)


class CheckoutPage(BasePage):
    """ Checkout Page - Handles shipping details, payment, and confirming order """

    # Locators
    STREET_ADDRESS = (By.NAME, "street")
    CITY = (By.NAME, "city")
    POSTAL_CODE = (By.NAME, "postalCode")
    CARD_NUMBER = (By.NAME, "cardNumber")
    NAME_ON_CARD = (By.NAME, "nameOnCard")
    EXPIRATION = (By.NAME, "expiration")
    CVV = (By.NAME, "cvv")
    BUY_NOW_BUTTON = (By.CLASS_NAME, "btn-buy-now")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(CHECKOUT_PAGE_URL)

    def fill_shipping_details(self):
        """ Fill in shipping address details using constants """
        self.enter_text(self.STREET_ADDRESS, DEFAULT_STREET_ADDRESS)
        self.enter_text(self.CITY, DEFAULT_CITY)
        self.enter_text(self.POSTAL_CODE, DEFAULT_POSTAL_CODE)

    def fill_payment_details(self):
        """ Fill in payment details using constants """
        self.enter_text(self.CARD_NUMBER, DEFAULT_CARD_NUMBER)
        self.enter_text(self.NAME_ON_CARD, DEFAULT_NAME_ON_CARD)
        self.enter_text(self.EXPIRATION, DEFAULT_EXPIRATION)
        self.enter_text(self.CVV, DEFAULT_CVV)

    def complete_purchase(self):
        """ Click the Buy Now button """
        self.click(self.BUY_NOW_BUTTON)

    def is_order_successful(self):
        """ Check if order was successful by verifying redirection to Home Page """
        try:
            WebDriverWait(self.driver, 5).until(
                EC.url_to_be(BASE_URL)  # Using the constant for homepage URL
            )
            return True
        except (TimeoutException, NoSuchElementException):
            return False