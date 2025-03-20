import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from TestautomationPOM.pages.store_page import StorePage
from TestautomationPOM.pages.checkout_page import CheckoutPage
from TestautomationPOM.pages.home_page import HomePage
from TestautomationPOM.utils.constants import BASE_URL, CHECKOUT_PAGE_URL


def test_checkout_process(driver):
    """Verify that a user can complete the checkout process successfully with dynamic data."""
    store_page = StorePage(driver)
    home_page = HomePage(driver)
    checkout_page = CheckoutPage(driver)

    # Go to shop page
    store_page.go_to_shop()

    # Add product to cart
    store_page.set_quantity("Gala Apples", 3)
    store_page.add_to_cart("Gala Apples")

    # Open cart
    home_page.open_cart()

    # Navigate to checkout page
    driver.get(CHECKOUT_PAGE_URL)

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
