from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from TestautomationPOM.pages.base_page import BasePage
from TestautomationPOM.utils.constants import SHOP_PAGE_URL
from datetime import datetime, timedelta


class StorePage(BasePage):
    """Handles interactions with the store page"""

    # **Age Verification Locators**
    AGE_VERIFICATION_POPUP = (By.CLASS_NAME, "modal-content")
    BIRTHDATE_INPUT = (By.XPATH, "//input[@placeholder='DD-MM-YYYY']")
    CONFIRM_BUTTON = (By.XPATH, "//button[text()='Confirm']")
    AGE_VERIFICATION_SUCCESS = (By.CLASS_NAME, "go3958317564")

    # **Navigation Locators**
    SHOP_BUTTON = (By.XPATH, "//a[@href='/store']")  # XPath for the Shop button
    PRODUCT_CONTAINER = (By.CLASS_NAME, "product-store-container")  # A store-specific element

    def handle_age_verification(self, age: int = 18):
        """Handles the age verification modal and ensures dynamic input for different ages."""
        try:
            print("age verification modal checked!")

            # Checking if the modal appears
            modal = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, "//h2[contains(text(), 'Age Verification')]"))
            )
            print(f"🔹 Age verification required. Entering birthdate for age: {age}")

            # Dynamic birthdate based on the given age (Format: DD-MM-YYYY)
            today = datetime.today()
            birthdate = today - timedelta(days=(age * 365))  # Approximate age calculation
            birthdate_str = birthdate.strftime("%d-%m-%Y")  # Format: DD-MM-YYYY
            print(f"🔹 Using birthdate: {birthdate_str}")

            # ✅ Locate the birthdate input field
            birthdate_input = self.driver.find_element(By.XPATH, "//input[@type='text' and @placeholder='DD-MM-YYYY']")
            birthdate_input.clear()  # Clear any existing input
            birthdate_input.send_keys(birthdate_str)  # Enter the dynamically generated birthdate

            # ✅ Click the confirm button
            confirm_button = self.driver.find_element(By.XPATH, "//button[text()='Confirm']")
            confirm_button.click()

            # ✅ Wait for the modal to disappear (indicating successful verification)
            WebDriverWait(self.driver, 5).until(
                EC.invisibility_of_element_located((By.XPATH, "//h2[contains(text(), 'Age Verification')]"))
            )
            print("✅ Age verification passed!")

        except Exception:
            print("✅ No age verification modal detected, proceeding...")

    def find_product(self, product_name: str):
        """Finds the product but does NOT click it"""
        print(f"🔍 Searching for product: {product_name}")

        try:
            product_title = self.find_elements((By.XPATH, "//p[@class='lead']"))
            print("Product title: ", product_title)

        except TimeoutException:
            print(f"ERROR: Product '{product_name}' NOT found!")
            raise

    def select_product(self, product_name):
        """Clicks the product (if needed)"""
        product = self.find_product(product_name)
        product.click()

    def find_and_click_product(self, product_name):
        """Finds and clicks the product (if necessary)"""
        self.find_product(product_name)
        self.select_product(product_name)

    def get_quantity_input(self, product_name):
        """Finds the quantity input field for a specific product"""
        return self.find_product(product_name).find_element(By.XPATH, "//input[@type='number']")

    def get_add_to_cart_button(self, product_name):
        """Finds the Add to Cart button for a specific product"""
        return self.find_product(product_name).find_element(By.XPATH, "//button[@class='btn btn-primary btn-cart' and "
                                                                      "contains(text(), 'Add to Cart')]")

    def set_quantity(self, product_name, quantity):
        """Sets the quantity for a specific product"""
        quantity_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,
                                        f"//p[contains(text(), '{product_name}')]/ancestor::div[contains(@class, 'product-card')]//input[@type='number']"))
        )
        quantity_input.clear()
        quantity_input.send_keys(str(quantity))

    def add_to_cart(self, product_name):
        """Clicks the Add to Cart button for a specific product"""
        add_to_cart_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,
                                        f"//p[contains(text(), '{product_name}')]/ancestor::div[contains(@class, 'product-card')]//button[contains(text(), 'Add to Cart')]"))
        )
        add_to_cart_button.click()

    def verify_item_added_message(self):
        """Wait for 'Item added to cart!' message to appear after adding an item."""
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[@role='status' and contains(text(), 'Item added to cart!')]"))
        )
        print("Item is there!")
