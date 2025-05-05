import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from TestautomationPOM.pages.base_page import BasePage
from TestautomationPOM.utils.constants import SHOP_PAGE_URL


class StorePage(BasePage):
    """Handles interactions with the store page"""

    # **Age Verification Locators**
    AGE_VERIFICATION_POPUP = (By.XPATH, "//h2[contains(text(), 'Age Verification')]")
    BIRTHDATE_INPUT = (By.XPATH, "//input[@type='text' and @placeholder='DD-MM-YYYY']")
    CONFIRM_BUTTON = (By.XPATH, "//button[text()='Confirm']")
    AGE_VERIFICATION_SUCCESS = (By.XPATH, "//div[@class='go3958317564' and contains(text(), 'You are of age')]")
    AGE_VERIFICATION_DENIED = (By.XPATH, "//div[@class='go3958317564' and contains(text(), 'You are underage')]")
    AGE_VERIFICATION_STATUS = (By.XPATH, "//div[@role='status']")

    # **Product Interaction Locators (Generic)**
    QUANTITY_BUTTON = (By.XPATH, "//input[@type='number']")
    ADD_TO_CART_BUTTON_TEMPLATE = (By.XPATH,"//p[contains(text(), '{product_name}')]/ancestor::div[contains(@class, "
                                            "'product-card')]//button[contains(@class, 'btn-cart')]")

    SET_QUANTITY_INPUT = (By.XPATH,
                          "//p[contains(text(), '{product_name}')]/ancestor::div[contains(@class, "
                          "'product-card')]//input[@type='number']"
                          )

    # **Navigation Locators**
    SHOP_BUTTON = (By.XPATH, "//a[@href='/store']")  # XPath for the Shop button
    PRODUCT_CONTAINER = (By.CLASS_NAME, "product-store-container")  # A store-specific element

    def handle_age_verification(self, birth_date):
        """Handles the age verification modal and ensures dynamic input for different ages."""
        try:
            print("age verification modal checked!")

            # Checking if the modal appears
            modal = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(self.AGE_VERIFICATION_POPUP)
            )
            print(f"🔹 Age verification required. Entering birthdate")

            # Locate the birthdate input field
            birthdate_input = self.find_element(self.BIRTHDATE_INPUT)
            birthdate_input.clear()  # Clear any existing input
            birthdate_input.send_keys(birth_date)  # Enter the dynamically generated birthdate

            # Click the confirm button
            confirm_button = self.driver.find_element(*self.CONFIRM_BUTTON)
            confirm_button.click()

            # Get the text from div with role status
            status = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.AGE_VERIFICATION_STATUS)
            )

            # Wait for the modal to disappear (indicating successful verification)
            WebDriverWait(self.driver, 5).until(
                EC.invisibility_of_element_located(self.AGE_VERIFICATION_POPUP)
            )
            print("Age verification passed!")
            return status.text
        except Exception:
            print("No age verification modal detected!")
            return status.text

    def find_product(self, product_name: str):
        """Finds the product element by its name but does NOT click it"""
        try:
            product = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(
                    (By.XPATH, f"//p[@class='lead' and contains(text(), '{product_name}')]")
                )
            )
            print(f"Product found: {product.text}")
            return product
        except TimeoutException:
            print(f"ERROR: Product '{product_name}' NOT found!")
            raise

    def select_product(self, product_name):
        """Clicks the product (if needed)"""
        product = self.find_product(product_name)
        product.click()

    def find_and_click_product(self, product_name):
        """Finds and clicks the product (if necessary)"""
        product = self.find_product(product_name)
        time.sleep(2)
        product.click()

    def get_quantity_input(self, product_name):
        """Finds the quantity input field for a specific product"""
        return self.find_product(product_name).find_element(*self.QUANTITY_BUTTON)

    def get_add_to_cart_button(self, product_name):
        """Finds the Add to Cart button for a specific product"""
        locator = (By.XPATH, self.ADD_TO_CART_BUTTON_TEMPLATE.format(product_name=product_name))
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))

    def set_quantity(self, product_name, quantity):
        """Sets the quantity for a specific product"""

        # Replace {product_name} in the XPath with the actual name
        dynamic_xpath = (
            self.SET_QUANTITY_INPUT[0],
            self.SET_QUANTITY_INPUT[1].format(product_name=product_name)
        )

        # Wait until the quantity input is clickable
        quantity_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(dynamic_xpath)
        )

        quantity_input.clear()
        quantity_input.send_keys(str(quantity))

    def add_to_cart(self, product_name):
        locator = (By.XPATH, self.ADD_TO_CART_BUTTON_TEMPLATE[1].format(product_name=product_name))
        add_to_cart_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        )
        add_to_cart_button.click()

    def verify_item_added_message(self):
        """Wait for 'Item added to cart!' message to appear after adding an item."""
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[@role='status' and contains(text(), 'Item added to cart!')]"))
        )
        print("Item is there!")

    def is_access_granted(self):
        try:
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(self.AGE_VERIFICATION_SUCCESS)
            )
            print("User is of age.")
            return True
        except TimeoutException:
            print("Underage or modal failed.")
            return False
        except Exception as e:
            print(f"Error: {e}")
            return False

    def is_access_denied(self):
        try:
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(self.AGE_VERIFICATION_DENIED)
            )
            print("User is underage.")
            return True
        except TimeoutException:
            print("No denial message found — user might be of age.")
            return False
        except Exception as e:
            print(f"Unexpected error while checking access denied: {e}")
            return False
