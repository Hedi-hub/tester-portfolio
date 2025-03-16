import pytest
from TestautomationPOM.pages.home_page import HomePage
from TestautomationPOM.pages.shop_page import ShopPage
from TestautomationPOM.utils.constants import BASE_URL


def test_search_product(driver):
    """Verify that searching for a product displays correct results."""
    driver.get(BASE_URL)
    home_page = HomePage(driver)

    result_text = home_page.search_product("Oranges")

    assert "Oranges" in result_text, "Search suggestion did not return expected product."
    home_page.select_product_from_suggestions()


def test_add_product_to_cart(driver):
    """Verify that a product can be added to the cart from the shop page."""
    driver.get(BASE_URL)
    home_page = HomePage(driver)
    home_page.go_to_shop()

    shop_page = ShopPage(driver)
    shop_page.add_product_to_cart("Oranges", quantity=3)

    assert shop_page.is_product_added_successfully(), "Product was not added successfully."


def test_select_product(driver):
    """Verify that clicking on a product opens the correct product page."""
    driver.get(BASE_URL)
    home_page = HomePage(driver)
    home_page.go_to_shop()

    shop_page = ShopPage(driver)
    shop_page.select_product("Oranges")

    assert "Oranges" in shop_page.get_product_title(), "Incorrect product page opened."
