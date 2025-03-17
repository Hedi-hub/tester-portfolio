import pytest
from TestautomationPOM.pages.store_page import StorePage
from TestautomationPOM.utils.constants import BASE_URL


def test_add_item_to_cart(driver):
    """Verify that an item can be added to the cart."""
    driver.get(BASE_URL)
    store_page = StorePage(driver)
    store_page.go_to_shop()

    store_page.select_product("Oranges")  # Now navigates through pages to find product
    store_page.set_quantity(3)
    store_page.add_to_cart()

    store_page.open_cart()

    assert store_page.is_product_in_cart("Oranges"), "Item was not added to the cart."


def test_update_cart_quantity(driver):
    """Verify that the quantity of an item in the cart can be updated."""
    driver.get(BASE_URL)
    store_page = StorePage(driver)
    store_page.go_to_shop()

    store_page.select_product("Oranges")
    store_page.set_quantity(2)
    store_page.add_to_cart()

    store_page.open_cart()
    store_page.update_product_quantity("Oranges", 5)

    assert store_page.get_product_quantity("Oranges") == 5, "Cart quantity update failed."


def test_remove_item_from_cart(driver):
    """Verify that an item can be removed from the cart."""
    driver.get(BASE_URL)
    store_page = StorePage(driver)
    store_page.go_to_shop()

    store_page.select_product("Oranges")
    store_page.set_quantity(1)
    store_page.add_to_cart()

    store_page.open_cart()
    store_page.remove_product("Oranges")

    assert not store_page.is_product_in_cart("Oranges"), "Item was not removed from the cart."


def test_navigate_to_shop_with_age_verification(driver):
    """Verify that the shop page opens correctly, handling age verification if needed."""
    driver.get(BASE_URL)
    store_page = StorePage(driver)

    store_page.go_to_shop()  # This will automatically handle age verification

    # Check that the shop page loaded successfully by verifying the URL contains 'store'
    assert "store" in driver.current_url, "Shop page did not load correctly after age verification."
