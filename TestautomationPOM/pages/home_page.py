from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.search_bar = (By.XPATH, "//input[@placeholder='Search Products']")
        self.search_result = (By.XPATH, "//div[@class='suggestion-item']//strong")

    def search_product(self, product_name):
        """Enter a product name in the search bar and wait for suggestions."""
        self.enter_text(self.search_bar, product_name)
        return WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_element_located(self.search_result)
        ).text

    def select_product_from_suggestions(self):
        """Click the first product suggestion in the dropdown."""
        self.click(self.search_result)






















# from selenium.webdriver.common.by import By
# from .base_page import BasePage
#
#
# class HomePage(BasePage):
#     def __init__(self, driver):
#         super().__init__(driver)
#         self.search_bar = (By.ID, "searchBox")  # Update with actual ID/XPath
#         self.search_button = (By.ID, "searchButton")  # Update with actual ID/XPath
#         self.featured_product = (By.CLASS_NAME, "featured-product")  # Example locator
#
#     def search_product(self, product_name):
#         """Enter a product name in the search bar and click search."""
#         self.enter_text(self.search_bar, product_name)
#         self.click(self.search_button)
#
#     def click_featured_product(self):
#         """Click on the first featured product on the homepage."""
#         self.click(self.featured_product)
