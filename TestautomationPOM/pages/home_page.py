from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from TestautomationPOM.pages.base_page import BasePage
from TestautomationPOM.utils.constants import HOME_PAGE_URL


class HomePage(BasePage):
    """Handles home page functionalities like searching and navigating to cart."""

    # **Locators**
    SEARCH_BAR = (By.XPATH, "//input[@placeholder='Search Products']")
    SEARCH_RESULT = (By.XPATH, "//div[@class='suggestion-item']/p/strong[text()='Oranges']")  # Fixed
    CART_ICON = (By.CLASS_NAME, "headerIcon")
    PRODUCT_TITLE = (By.XPATH, "//h2")  # Locator for product title on product page

    def __init__(self, driver):
        super().__init__(driver)

    def search_product(self, product_name):
        """Enter a product name in the search bar and return first result."""
        self.enter_text(self.SEARCH_BAR, product_name)
        return WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(self.SEARCH_RESULT)
        ).text

    def select_product_from_suggestions(self):
        """Click the first product suggestion in the dropdown."""
        self.click(self.SEARCH_RESULT)

    def get_product_title(self):
        """Get the product title from the product page."""
        return self.get_element_text(self.PRODUCT_TITLE)

    def open_cart(self):
        """Click the cart icon to navigate to the cart page."""
        self.click(self.CART_ICON)
