import pytest
from TestautomationPOM.pages.login_page import LoginPage
from TestautomationPOM.pages.store_page import StorePage
from TestautomationPOM.pages.home_page import HomePage
from TestautomationPOM.utils.constants import BASE_URL, TEST_EMAIL, TEST_PASSWORD
import time

from TestautomationPOM.utils.helpers import format_date


@pytest.mark.parametrize("product_name, quantity, day, month, year", [
    ("Gala Apples", 2,  2, 1, 1993),
    ("Gala Apples", 2,  1, 1, 2016),
])
def test_add_item_to_cart(driver, product_name, quantity, day, month, year):
    """Verify that an item can be added to the cart dynamically, handling age verification."""

    login_page = LoginPage(driver)
    home_page = login_page.login(TEST_EMAIL, TEST_PASSWORD)
    store_page = home_page.go_to_shop()
    date_of_birth = format_date(day, month, year)
    store_page.handle_age_verification(date_of_birth)
    time.sleep(3)  # Short sleep to ensure all products are rendered

    # Find and interact with the product
    store_page.find_product(product_name)
    store_page.set_quantity(product_name, quantity)
    store_page.add_to_cart(product_name)
    time.sleep(2)
    store_page.verify_item_added_message()

    # Verify the confirmation message appears
    store_page.verify_item_added_message()

    # Open cart & verify
    home_page.open_cart()
    print(f"Checking if '{product_name}' exists in the cart...")
    assert home_page.is_product_in_cart(product_name), f"Item {product_name} was not added to the cart."
