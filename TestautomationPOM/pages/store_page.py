from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from TestautomationPOM.pages.base_page import BasePage
from TestautomationPOM.utils.constants import SHOP_PAGE_URL, CART_PAGE_URL


class StorePage(BasePage):
    """Handles shopping, cart management, pagination, and navigation to checkout."""

    # **Locators for ShopPage Functionality**
    SHOP_LINK = (By.XPATH, "//a[@href='/store']")
    PRODUCT_CARD = (By.XPATH, "//p[contains(@class, 'lead')]")  # Product name
    PRODUCT_QUANTITY = (By.XPATH, "//input[contains(@class, 'quantity')]")  # Quantity input field
    ADD_TO_CART_BUTTON = (By.XPATH, "//button[contains(@class, 'btn btn-primary btn-cart')]")  # Add to cart button
    SUCCESS_MESSAGE = (By.CLASS_NAME, "go3958317564")  # Confirmation that item is added

    # **Pagination Locator (Fixed)**
    PAGINATION_BUTTON = (By.XPATH, "//li[@class='pagination-item ']/button[text()='{}']")

    # **Locators for Cart Functionality**
    CART_ITEM_NAME = (By.XPATH, "//div[contains(@class, 'cart-item')]//h3")
    CART_ITEM_QUANTITY = (By.XPATH, "//div[contains(@class, 'cart-item')]//input[contains(@class, 'quantity')]")
    REMOVE_ITEM_BUTTON = (By.CLASS_NAME, "remove-icon")
    CHECKOUT_BUTTON = (By.CLASS_NAME, "btn-buy-now")  # Proceed to checkout button

    # Age Verification Modal Locators
    AGE_VERIFICATION_INPUT = (By.XPATH, "//input[@placeholder='DD-MM-YYYY']")
    AGE_CONFIRM_BUTTON = (By.XPATH, "//button[text()='Confirm']")

    def __init__(self, driver):
        super().__init__(driver)

    def go_to_shop(self):
        """Navigate to the shop page and handle age verification if needed."""
        self.driver.get(SHOP_PAGE_URL)
        self.handle_age_verification()

    def navigate_to_page(self, page_number: int):
        """Navigate to a specific page using pagination."""
        try:
            pagination_locator = (By.XPATH, f"//li[@class='pagination-item ']/button[text()='{page_number}']")

            # Ensure pagination button is visible and clickable
            pagination_button = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(pagination_locator)
            )
            pagination_button.click()

            # Wait for new products to load (ensuring a page update)
            WebDriverWait(self.driver, 5).until(
                EC.staleness_of(self.find_element(self.PRODUCT_CARD))  # Wait for old products to disappear
            )
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(self.PRODUCT_CARD)  # Wait for new products
            )
            print(f"✅ Successfully navigated to page {page_number}")

        except TimeoutException:
            print(f"❌ Page {page_number} did not load in time.")
        except NoSuchElementException:
            print(f"❌ Page {page_number} button not found.")

    def set_quantity(self, quantity):
        """Set the quantity of the selected product."""
        try:
            quantity_input = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.PRODUCT_QUANTITY)
            )
            quantity_input.clear()
            quantity_input.send_keys(str(quantity))
            print(f"✅ Quantity set to {quantity}")
        except TimeoutException:
            print("❌ Timeout: Quantity input field not found.")

    def add_to_cart(self):
        """Click the 'Add to Cart' button."""
        try:
            self.click(self.ADD_TO_CART_BUTTON)
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(self.SUCCESS_MESSAGE)
            )
            print("✅ Item successfully added to cart.")
        except Exception as e:
            print("❌ Error: Unable to click 'Add to Cart' button.", e)

    # **Cart Methods**
    def open_cart(self):
        """Navigate to the cart page using the absolute URL."""
        self.driver.get(CART_PAGE_URL)

    def is_product_in_cart(self, product_name):
        """Check if a specific product is present in the cart."""
        try:
            WebDriverWait(self.driver, 10).until(
                EC.text_to_be_present_in_element(self.CART_ITEM_NAME, product_name)
            )
            print(f"'{product_name}' is in the cart.")
            return True
        except TimeoutException:
            print(f"'{product_name}' not found in the cart.")
            return False

    def select_product(self, product_name):
        """Select a product by its name after navigating through pagination."""
        found = False
        for page in range(1, 6):  # Assuming there are max 5 pages
            self.navigate_to_page(page)
            try:
                products = self.find_elements(self.PRODUCT_CARD)
                for product in products:
                    if product.text.strip().lower() == product_name.lower():
                        product.click()
                        found = True
                        print(f"✅ Found and selected {product_name} on page {page}")
                        break
                if found:
                    break
            except NoSuchElementException:
                print(f"❌ Product '{product_name}' not found on page {page}.")
        if not found:
            raise Exception(f"Product '{product_name}' not found after checking all pages.")

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

    def handle_age_verification(self, birthdate="01-01-1990"):
        """Handle the age verification modal by entering a birthdate and confirming."""
        try:
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(self.AGE_VERIFICATION_INPUT)
            )
            self.enter_text(self.AGE_VERIFICATION_INPUT, birthdate)
            self.click(self.AGE_CONFIRM_BUTTON)
        except TimeoutException:
            print("No age verification needed.")
