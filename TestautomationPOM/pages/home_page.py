from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from TestautomationPOM.pages.base_page import BasePage
from TestautomationPOM.pages.store_page import StorePage
from TestautomationPOM.utils.constants import HOME_PAGE_URL


class HomePage(BasePage):
    """Handles home page functionalities like searching and navigating to cart."""

    CART_ICON = (By.XPATH, "//div[@class='headerIcon'][3]")
    SEARCH_INPUT = (By.XPATH, "//input[@placeholder='Search Products']")

    def __init__(self, driver):
        super().__init__(driver)

    def go_to_shop(self):
        """Navigates to the store page by clicking the Shop button if necessary."""

        try:
            # ✅ If we are NOT already on the store page, click the Shop button
            if "/store" not in self.driver.current_url:
                print("🔹 Clicking on 'Shop' button to go to store...")
                # Handle age verification first
                WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//a[@href='/store']"))
                ).click()

            # ✅ Wait for store page URL
            WebDriverWait(self.driver, 10).until(
                EC.url_contains("/store")
            )

            print("✅ Store page URL loaded.")

            # ✅ Wait for the product grid to appear
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "product-store-container"))
            )
            print("✅ Store page fully loaded.")

            # ✅ NEW: Wait for at least one product to be visible
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, '//p[contains(text(), \'Gala Apples\')]'))
            )
            print("✅ Products are visible.")

            return StorePage(self.driver)

        except TimeoutException:
            print("❌ ERROR: Store page or products did NOT load! Taking screenshot...")
            self.driver.save_screenshot("store_page_error.png")
            raise

    def open_cart(self):
        """Click the cart icon to navigate to the cart page."""
        self.click(self.CART_ICON)

    def search_product(self, product_name):
        """Search for a product and return the suggestion text"""

        SUGGESTION_ITEM = (By.XPATH, f"//div[@class='suggestion-item']/p/strong[text()='{product_name}']")

        self.enter_text(self.SEARCH_INPUT, product_name)

        suggestion = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(SUGGESTION_ITEM)
        )
        return suggestion.text

    def is_product_in_cart(self, product_name):
        """Check if a product name appears in the cart."""
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH,
                     f"//h5[@class='checkout-product-title' and contains(text(), '{product_name}')]")
                )
            )
            return True
        except (TimeoutException, NoSuchElementException):
            print(f"Product '{product_name}' not in cart!")
            return False
