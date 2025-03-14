from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from TestautomationPOM.pages.base_page import BasePage
from selenium.common.exceptions import TimeoutException, NoSuchElementException, WebDriverException


class CartPage(BasePage):
    """ Cart Page for managing items in the cart """

    # Locators
    CART_ICON = (By.CLASS_NAME, "headerIcon")  # Cart icon in the header
    CART_ITEM_NAME = (By.XPATH, "//div[contains(@class, 'cart-item')]//h3")  # Item in the cart
    CART_ITEM_QUANTITY = (By.XPATH, "//input[contains(@class, 'quantity')]")  # Quantity field in cart
    REMOVE_ITEM_BUTTON = (By.CLASS_NAME, "remove-icon")  # Remove item from cart
    CHECKOUT_BUTTON = (By.CLASS_NAME, "btn-buy-now")  # Proceed to checkout button

    def __init__(self, driver):
        super().__init__(driver)

    def open_cart(self):
        """ Clicks on the cart icon to open the cart page """
        try:
            self.click(self.CART_ICON)
        except WebDriverException:
            print("Error: Unable to click on cart icon.")

    def is_cart_empty(self):
        """ Check if the cart is empty """
        try:
            self.find_element(self.CART_ITEM_NAME)
            return False  # Items are present
        except NoSuchElementException:
            return True  # No items in the cart

    def get_cart_item_quantity(self):
        """ Get the quantity of the item in the cart """
        try:
            return self.find_element(self.CART_ITEM_QUANTITY).get_attribute("value")
        except NoSuchElementException:
            print("Error: Quantity field not found in cart.")
            return None

    def remove_item(self):
        """ Click on the remove item button """
        try:
            self.click(self.REMOVE_ITEM_BUTTON)
        except WebDriverException:
            print("Error: Unable to click on remove item button.")


