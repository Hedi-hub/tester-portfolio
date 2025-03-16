from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from TestautomationPOM.pages.base_page import BasePage
from TestautomationPOM.utils.constants import CART_PAGE_URL

class CartPage(BasePage):
    """Handles all cart functionalities like adding, removing, and updating products."""

    # **Locators**
    CART_ITEM_NAME = (By.XPATH, "//div[contains(@class, 'cart-item')]//h3")
    CART_ITEM_QUANTITY = (By.XPATH, "//div[contains(@class, 'cart-item')]//input[contains(@class, 'quantity')]")
    REMOVE_ITEM_BUTTON = (By.CLASS_NAME, "remove-icon")
    CHECKOUT_BUTTON = (By.CLASS_NAME, "btn-buy-now")  # Proceed to checkout button

    def __init__(self, driver):
        super().__init__(driver)

    def is_product_in_cart(self, product_name):
        """Check if a specific product is present in the cart."""
        try:
            WebDriverWait(self.driver, 5).until(
                EC.text_to_be_present_in_element(self.CART_ITEM_NAME, product_name)
            )
            return True
        except TimeoutException:
            return False

    def get_product_quantity(self, product_name):
        """Retrieve the quantity of a specific product in the cart."""
        try:
            quantity_element = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(self.CART_ITEM_QUANTITY)
            )
            return int(quantity_element.get_attribute("value"))
        except (TimeoutException, NoSuchElementException):
            return None

    def update_product_quantity(self, product_name, quantity):
        """Update the quantity of a specific product in the cart."""
        quantity_element = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(self.CART_ITEM_QUANTITY)
        )
        quantity_element.clear()
        quantity_element.send_keys(str(quantity))

    def remove_product(self, product_name):
        """Remove a product from the cart."""
        self.click(self.REMOVE_ITEM_BUTTON)

    def proceed_to_checkout(self):
        """Click the checkout button to proceed."""
        self.click(self.CHECKOUT_BUTTON)
