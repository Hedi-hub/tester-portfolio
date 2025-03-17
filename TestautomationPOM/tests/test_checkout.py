import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from TestautomationPOM.pages.checkout_page import CheckoutPage
from TestautomationPOM.utils.constants import BASE_URL


def test_checkout_process(driver):
    """Verify that a user can complete the checkout process successfully."""
    checkout_page = CheckoutPage(driver)

    # Fill shipping details
    checkout_page.fill_shipping_details()

    # Fill payment details
    checkout_page.fill_payment_details()

    # Click Buy Now to complete purchase
    checkout_page.complete_purchase()

    # Wait for order confirmation and homepage redirection
    WebDriverWait(driver, 10).until(
        EC.url_to_be(BASE_URL)
    )

    assert checkout_page.is_order_successful(), "Order was not completed successfully."
