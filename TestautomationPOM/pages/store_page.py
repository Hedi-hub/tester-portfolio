from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from TestautomationPOM.pages.base_page import BasePage
from TestautomationPOM.utils.constants import SHOP_PAGE_URL


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



    def handle_age_verification(self):
        """Handles the age verification modal if it appears."""
        try:
            print("🔹 Checking for age verification modal...")

            # ✅ Wait up to 5 seconds to check if the modal appears
            modal = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, "//h2[contains(text(), 'Age Verification')]"))
            )
            print("🔹 Age verification required. Entering birthdate...")
            #TODO FIX INPUT FOR AGE, MAKE SURE YOU CAN ENTER ABOVE AND BELOW 16 DONT MAKE IT STATIC
            # ✅ Enter a valid birthdate
            birthdate_input = self.driver.find_element(By.XPATH, "//input[@type='text']")
            birthdate_input.send_keys("01-01-1990")  # Use a valid format

            # ✅ Click the confirm button
            confirm_button = self.driver.find_element(By.XPATH, "//button[text()='Confirm']")
            confirm_button.click()

            # ✅ Wait for the modal to disappear
            WebDriverWait(self.driver, 5).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[contains(text(), 'Age Verification')]"))
            )
            print("✅ Age verification passed!")

        except Exception:
            print("✅ No age verification modal detected, proceeding...")

    def find_product(self, product_name):
        """Finds the product but does NOT click it"""
        print(f"🔍 Searching for product: {product_name}")

        try:
            return WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH,
                     f"//p[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), '{product_name.lower()}')]")
                )
            )
        except TimeoutException:
            print(f"❌ ERROR: Product '{product_name}' NOT found! Taking screenshot...")
            self.driver.save_screenshot(f"product_not_found_{product_name}.png")
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
        return self.find_product(product_name).find_element(By.XPATH, ".//input[@type='number']")

    def get_add_to_cart_button(self, product_name):
        """Finds the Add to Cart button for a specific product"""
        return self.find_product(product_name).find_element(By.XPATH, ".//button[contains(text(), 'Add to Cart')]")

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
