import pytest

from TestautomationPOM.pages.login_page import LoginPage
from TestautomationPOM.pages.store_page import StorePage
from TestautomationPOM.pages.home_page import HomePage
from TestautomationPOM.utils.constants import BASE_URL, TEST_EMAIL, TEST_PASSWORD
import time


@pytest.mark.parametrize("product_name, quantity", [
    ("Gala Apples", 2)
])
def test_add_item_to_cart(driver, product_name, quantity):
    """Verify that an item can be added to the cart dynamically, handling age verification."""

    login_page = LoginPage(driver)
    home_page = login_page.login(TEST_EMAIL, TEST_PASSWORD)
    store_page = home_page.go_to_shop()
    store_page.handle_age_verification()

    # FIX: Wait a moment before searching for products
    time.sleep(3)  # Short sleep to ensure all products are rendered

    print(driver.page_source)

    # Find product dynamically
    store_page.find_product(product_name)

    # Set quantity & add to cart
    store_page.set_quantity(product_name, quantity)
    store_page.add_to_cart(product_name)
    time.sleep(2)

    # Verify the confirmation message appears
    store_page.verify_item_added_message()

    #TODO MAKE SURE CART OPENS

    # Open cart & verify
    home_page.open_cart()

    print(f"Checking if '{product_name}' exists in the cart...")

    assert home_page.is_product_in_cart(product_name), f"Item {product_name} was not added to the cart."
