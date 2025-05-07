import pytest
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from TestautomationPOM.pages.login_page import LoginPage
from TestautomationPOM.pages.home_page import HomePage
from TestautomationPOM.pages.store_page import StorePage
from TestautomationPOM.pages.product_rating_page import ProductRatingPage
from TestautomationPOM.utils.constants import BASE_URL, TEST_EMAIL, TEST_PASSWORD, TEST_USERNAME


@pytest.mark.parametrize("product_name, rating, comment", [
    ("Gala Apples", 5, "Very juicy for a good price!!"),
])
def test_product_rating_flow(driver, product_name, rating, comment):
    """Test full product rating flow for a previously purchased item."""

    # Step 1: Login
    driver.get(BASE_URL)
    login_page = LoginPage(driver)
    home_page = login_page.login(TEST_EMAIL, TEST_PASSWORD)

    # Step 2: Navigate to store and click product
    store_page = home_page.go_to_shop()

    ####### Click on confirm button to get rid of age verification
    store_page.handle_age_verification("01-01-1990")

    store_page.find_and_click_product(product_name)

    # Step 3: Load product rating page
    rating_page = ProductRatingPage(driver)

    # Step 4: If already reviewed, delete first
    if rating_page.has_review_restriction():
        print("Already reviewed product")
        rating_page.delete_existing_review()

    # Step 5: Rate the product
    rating_page.click_star_rating(rating)
    assert rating_page.count_filled_stars() == rating, "Expected star count doesn't match after click."

    # Step 6: Submit review
    rating_page.submit_review(comment)
    time.sleep(4)
    # Step 7: Check name appears under review
    name = rating_page.get_own_review_name()
    assert name == TEST_USERNAME, f"Unexpected review name. Expected {TEST_USERNAME} but found '{name}'"

    # # Step 8: Check if comment appears
    # review_texts = rating_page.get_review_texts()
    # if comment not in review_texts:
    #     print("Initial review missing, editing...")
    #     rating_page.edit_review(comment)
    #     review_texts = rating_page.get_review_texts()
    #     assert comment in review_texts, "Edited review still not found."
    # else:
    #     print("Review appeared correctly after first submission.")