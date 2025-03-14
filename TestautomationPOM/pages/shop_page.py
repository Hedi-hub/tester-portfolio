from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, WebDriverException
from TestautomationPOM.pages.base_page import BasePage


class ShopPage(BasePage):
    """ Shop Page for selecting products and adding to cart """

    # Locators
    SHOP_LINK = (By.XPATH, "//a[@href='/store']")  # Shop navigation link
    PRODUCT_CARD = (By.XPATH, "//p[contains(@class, 'lead')]")  # Product name
    PRODUCT_QUANTITY = (By.XPATH, "//input[contains(@class, 'quantity')]")  # Quantity input field
    ADD_TO_CART_BUTTON = (By.XPATH, "//button[contains(@class, 'btn btn-primary btn-cart')]")  # Add to cart button
    SUCCESS_MESSAGE = (By.CLASS_NAME, "go3958317564")  # Confirmation that item is added

    def __init__(self, driver):
        super().__init__(driver)

    def go_to_shop(self):
        """ Navigate to the shop page """
        self.click(self.SHOP_LINK)

    def select_product(self, product_name):
        """ Select a product by its name """
        try:
            products = self.find_elements(self.PRODUCT_CARD)
            for product in products:
                if product.text == product_name:
                    product.click()
                    break
        except NoSuchElementException:
            print(f"Error: Product '{product_name}' not found.")

    def set_quantity(self, quantity):
        """ Set the quantity of the selected product """
        try:
            quantity_input = self.find_element(self.PRODUCT_QUANTITY)
            quantity_input.clear()
            quantity_input.send_keys(str(quantity))
        except NoSuchElementException:
            print("Error: Quantity input field not found.")

    def add_to_cart(self):
        """ Click the 'Add to Cart' button """
        try:
            self.click(self.ADD_TO_CART_BUTTON)
        except WebDriverException:
            print("Error: Unable to click 'Add to Cart' button.")

    def is_item_added(self):
        """ Check if the success message appears after adding to cart """
        try:
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(self.SUCCESS_MESSAGE)
            )
            return True
        except TimeoutException:
            print("Timeout: Success message did not appear.")
            return False
        except NoSuchElementException:
            print("Error: Success message not found.")
            return False
        except WebDriverException:
            print("Error: WebDriver encountered an issue while checking success message.")
            return False
