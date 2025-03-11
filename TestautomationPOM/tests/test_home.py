import pytest
from TestautomationPOM.pages.home_page import HomePage
from TestautomationPOM.utils.constants import BASE_URL


def test_search_product(driver):
    driver.get(BASE_URL)
    home_page = HomePage(driver)
    result_text = home_page.search_product("Oranges")
    assert "Oranges" in result_text, "Search suggestion did not return expected product"
    home_page.select_product_from_suggestions()
