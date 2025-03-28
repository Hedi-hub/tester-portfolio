import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from TestautomationPOM.pages.login_page import LoginPage
from TestautomationPOM.pages.store_page import StorePage
from TestautomationPOM.pages.checkout_page import CheckoutPage
from TestautomationPOM.pages.home_page import HomePage
from TestautomationPOM.utils.constants import BASE_URL, CHECKOUT_PAGE_URL, TEST_EMAIL, TEST_PASSWORD


def test_checkout_process(driver):
    """Verify that a user can complete the checkout process successfully with dynamic data."""
    # 1. Login
    login_page = LoginPage(driver)
    home_page = login_page.login(TEST_EMAIL, TEST_PASSWORD)

    # 2. Go to the store
    store_page = home_page.go_to_shop()

    # Add product to cart
    store_page.set_quantity("Gala Apples", 3)
    store_page.add_to_cart("Gala Apples")

    # Open cart
    home_page.open_cart()

    # Navigate to checkout page
    driver.get(CHECKOUT_PAGE_URL)
    checkout_page = CheckoutPage(driver)

    # Fill in shipping details dynamically
    checkout_page.fill_shipping_details(
        street="456 Market St",
        city="Munich",
        postal_code="80331"
    )

    # Fill in payment details dynamically
    checkout_page.fill_payment_details(
        card_number="5555555555554444",
        name_on_card="Alice Brown",
        expiration="08/26",
        cvv="987"
    )

    # Complete purchase
    checkout_page.complete_purchase()

    # Verify order success
    assert checkout_page.is_order_successful(), "Order was not completed successfully."
