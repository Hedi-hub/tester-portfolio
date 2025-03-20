import pytest
from TestautomationPOM.pages.store_page import StorePage
from TestautomationPOM.pages.home_page import HomePage
from TestautomationPOM.utils.constants import BASE_URL
import time


@pytest.mark.parametrize("product_name, quantity", [
    ("Gala Apples", 2),
    ("Celery", 5),
    ("Ginger", 3)
])
def test_add_item_to_cart(driver, product_name, quantity):
    """Verify that an item can be added to the cart dynamically, handling age verification."""

    driver.get(BASE_URL)
    store_page = StorePage(driver)
    home_page = HomePage(driver)

    # Navigate & handle age verification
    store_page.go_to_shop()

    # FIX: Wait a moment before searching for products
    time.sleep(1)  # Short sleep to ensure all products are rendered

    # Find product dynamically
    store_page.find_product(product_name)

    # Set quantity & add to cart
    store_page.set_quantity(product_name, quantity)
    store_page.add_to_cart(product_name)

    # Open cart & verify
    home_page.open_cart()
    assert home_page.is_product_in_cart(product_name), f"Item {product_name} was not added to the cart."
