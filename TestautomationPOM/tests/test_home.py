import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from TestautomationPOM.pages.home_page import HomePage
from TestautomationPOM.pages.login_page import LoginPage
from TestautomationPOM.utils.constants import BASE_URL, TEST_EMAIL, TEST_PASSWORD
from TestautomationPOM.pages.store_page import StorePage


def test_search_product(driver):
    """Test searching for a product and selecting it from suggestions."""
    driver.get(BASE_URL)
    home_page = HomePage(driver)
    login_page = LoginPage(driver)
    home_page = login_page.login(TEST_EMAIL, TEST_PASSWORD)
    store_page = home_page.go_to_shop()
    store_page.find_product()

    # Search for suggested item
    result_text = home_page.search_product("Gala Apples")

    # Wait for the search suggestion containing the suggested item to appear
    suggestion_xpath = "//div[@class='suggestion-item']/p/strong[text()='Gala Apples']"
    gala_apples_suggestion = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, suggestion_xpath))
    )

    # Assert that the search suggestion contains suggested item
    assert "Gala Apples" in result_text, "Search suggestion did not return expected product"

    # Click on suggested item using JavaScript (to avoid interaction issues)
    driver.execute_script("arguments[0].click();", gala_apples_suggestion)

    # Wait for the product title inside the description container
    product_title_xpath = "//div[@class='descriptionContainer']/h2"
    product_title = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, product_title_xpath))
    ).text

    assert "Gala Apples" in product_title, f"Failed to navigate to the correct product page. Found: {product_title}"