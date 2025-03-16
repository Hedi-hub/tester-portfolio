import pytest
from TestautomationPOM.pages.cart_page import CartPage
from TestautomationPOM.pages.home_page import HomePage
from TestautomationPOM.pages.shop_page import ShopPage
from TestautomationPOM.utils.constants import BASE_URL


def test_add_item_to_cart(driver):
    """Verify that an item can be added to the cart."""
    driver.get(BASE_URL)
    home_page = HomePage(driver)
    home_page.go_to_shop()

    shop_page = ShopPage(driver)
    shop_page.add_product_to_cart("Oranges", quantity=3)

    cart_page = CartPage(driver)
    cart_page.open_cart()

    assert cart_page.is_product_in_cart("Oranges"), "Item was not added to the cart."

def test_update_cart_quantity(driver):
    """Verify that the quantity of an item in the cart can be updated."""
    driver.get(BASE_URL)
    home_page = HomePage(driver)
    home_page.go_to_shop()

    shop_page = ShopPage(driver)
    shop_page.add_product_to_cart("Oranges", quantity=2)

    cart_page = CartPage(driver)
    cart_page.open_cart()
    cart_page.update_product_quantity("Oranges", 5)

    assert cart_page.get_product_quantity("Oranges") == 5, "Cart quantity update failed."

def test_remove_item_from_cart(driver):
    """Verify that an item can be removed from the cart."""
    driver.get(BASE_URL)
    home_page = HomePage(driver)
    home_page.go_to_shop()

    shop_page = ShopPage(driver)
    shop_page.add_product_to_cart("Oranges", quantity=1)

    cart_page = CartPage(driver)
    cart_page.open_cart()
    cart_page.remove_product("Oranges")

    assert not cart_page.is_product_in_cart("Oranges"), "Item was not removed from the cart."

def test_proceed_to_checkout(driver):
    """Verify that clicking 'Checkout' redirects to the checkout page."""
    driver.get(BASE_URL)
    home_page = HomePage(driver)
    home_page.go_to_shop()

    shop_page = ShopPage(driver)
    shop_page.add_product_to_cart("Oranges", quantity=2)

    cart_page = CartPage(driver)
    cart_page.open_cart()
    cart_page.proceed_to_checkout()

    assert "checkout" in driver.current_url, "Checkout page did not open."
