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

    def fill_shipping_details(self, street, city, postal_code):
        """ Fill in shipping address details dynamically """
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.STREET_ADDRESS)).send_keys(street)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.CITY)).send_keys(city)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.POSTAL_CODE)).send_keys(postal_code)

    def fill_payment_details(self, card_number, name_on_card, expiration, cvv):
        """ Fill in payment details dynamically """
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.CARD_NUMBER)).send_keys(card_number)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.NAME_ON_CARD)).send_keys(name_on_card)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.EXPIRATION)).send_keys(expiration)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.CVV)).send_keys(cvv)

    def complete_purchase(self):
        """ Click the Buy Now button """
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.BUY_NOW_BUTTON)).click()

    def is_order_successful(self):
        """ Check if order was successful by verifying redirection to Home Page """
        try:
            WebDriverWait(self.driver, 5).until(
                EC.url_to_be(BASE_URL)  # Using the constant for homepage URL
            )
            return True
        except (TimeoutException, NoSuchElementException):
            return False