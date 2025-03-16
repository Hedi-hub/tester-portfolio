import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from TestautomationPOM.pages.home_page import HomePage
from TestautomationPOM.utils.constants import BASE_URL


def test_search_product(driver):
    """Test searching for a product and selecting it from suggestions."""
    driver.get(BASE_URL)
    home_page = HomePage(driver)

    # Search for 'Oranges'
    result_text = home_page.search_product("Oranges")

    # Wait for the search suggestion containing 'Oranges' to appear
    suggestion_xpath = "//div[@class='suggestion-item']/p/strong[text()='Oranges']"
    oranges_suggestion = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, suggestion_xpath))
    )

    # Assert that the search suggestion contains 'Oranges'
    assert "Oranges" in result_text, "Search suggestion did not return expected product"

    # Click on 'Oranges' using JavaScript (to avoid interaction issues)
    driver.execute_script("arguments[0].click();", oranges_suggestion)

    # Wait for the product title inside the description container
    product_title_xpath = "//div[@class='descriptionContainer']/h2"
    product_title = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, product_title_xpath))
    ).text

    assert "Oranges" in product_title, f"Failed to navigate to the correct product page. Found: {product_title}"