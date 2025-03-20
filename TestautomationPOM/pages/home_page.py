from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from TestautomationPOM.pages.base_page import BasePage
from TestautomationPOM.utils.constants import HOME_PAGE_URL


class HomePage(BasePage):
    """Handles home page functionalities like searching and navigating to cart."""

    CART_ICON = (By.CLASS_NAME, "headerIcon")

    def open_cart(self):
        """Click the cart icon to navigate to the cart page."""
        self.click(self.CART_ICON)

    def is_product_in_cart(self, product_name):
        """Check if a product is in the cart by verifying its name appears in the cart page."""
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, f"//td[contains(text(), '{product_name}')]"))
            )
            return True
        except (TimeoutException, NoSuchElementException):
            print(f"Product '{product_name}' was NOT found in the cart.")
            return False
