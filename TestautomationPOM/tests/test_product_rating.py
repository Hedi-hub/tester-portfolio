import time
import pytest
from TestautomationPOM.pages.registration_page import RegistrationPage
from TestautomationPOM.pages.login_page import LoginPage
from TestautomationPOM.pages.store_page import StorePage
from TestautomationPOM.pages.checkout_page import CheckoutPage
from TestautomationPOM.pages.product_rating_page import ProductRatingPage
from TestautomationPOM.utils.constants import BASE_URL


def generate_unique_email():
    """Generates a unique email for test user."""
    timestamp = int(time.time())  # Get current timestamp
    return f"testuser_{timestamp}@example.com"


@pytest.mark.usefixtures("driver")
class TestProductRating:

    def test_rate_product_after_purchase(self, driver):
        """Test that a user can rate a product after purchase using a fresh account."""

        registration_page = RegistrationPage(driver)
        login_page = LoginPage(driver)
        store_page = StorePage(driver)
        checkout_page = CheckoutPage(driver)
        rating_page = ProductRatingPage(driver)

        # Generate a unique email
        email = generate_unique_email()
        password = "Test@123"

        # Register & Login
        driver.get(BASE_URL)
        registration_page.register(email, password)
        login_page.login(email, password)

        # Buy a product
        store_page.go_to_shop()
        store_page.select_product("Oranges")
        store_page.set_quantity(1)
        store_page.add_to_cart()
        store_page.open_cart()
        store_page.proceed_to_checkout()

        checkout_page.fill_shipping_details()
        checkout_page.fill_payment_details()
        checkout_page.complete_purchase()
        assert checkout_page.is_order_successful(), "Order was not completed successfully."

        # Rate the product
        assert rating_page.rate_product(5, "Great product!"), "Failed to rate product."

    def test_profane_review_is_blocked(self, driver):
        """
        Test that a profane review is blocked and does not appear in displayed reviews.
        """
        registration_page = RegistrationPage(driver)
        login_page = LoginPage(driver)
        store_page = StorePage(driver)
        checkout_page = CheckoutPage(driver)
        rating_page = ProductRatingPage(driver)

        # Generate a unique email
        email = generate_unique_email()
        password = "Test@123"

        # Register & Login
        driver.get(BASE_URL)
        registration_page.register(email, password)
        login_page.login(email, password)

        # Buy a product
        store_page.go_to_shop()
        store_page.select_product("Oranges")
        store_page.set_quantity(1)
        store_page.add_to_cart()
        store_page.open_cart()
        store_page.proceed_to_checkout()

        checkout_page.fill_shipping_details()
        checkout_page.fill_payment_details()
        checkout_page.complete_purchase()
        assert checkout_page.is_order_successful(), "Order was not completed successfully."

        # Submit a profane review
        profane_text = "This is f***ing terrible!"
        rating_page.rate_product(1, profane_text)
        time.sleep(2)  # Wait for review processing

        # Verify that the profane text is not displayed
        reviews = rating_page.get_displayed_reviews()
        assert not any(profane_text in review for review in reviews), (
            "Profane text was found in displayed reviews but should have been blocked or removed."
        )
