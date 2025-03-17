from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from TestautomationPOM.pages.base_page import BasePage


class ProductRatingPage(BasePage):
    """Handles product rating and review"""

    # **Locators**
    RATING_SECTION = (By.CLASS_NAME, "ratingContainer")
    INTERACTIVE_RATING = (By.CLASS_NAME, "interactive-rating")
    STARS = (By.CLASS_NAME, "star")
    REVIEW_TEXTAREA = (By.CLASS_NAME, "new-review-form-control")
    SUBMIT_REVIEW_BUTTON = (By.CLASS_NAME, "new-review-btn-send")
    REVIEW_RESTRICTION = (By.CLASS_NAME, "reviewRestriction")
    MENU_ICON = (By.CLASS_NAME, "menu-icon")  # To open dropdown
    DELETE_BUTTON = (By.XPATH, "//button[text()='Delete']")

    COMMENT_BLOCKS = (By.CSS_SELECTOR, "div.comment")
    COMMENT_FOOTER = (By.CSS_SELECTOR, "div.comment-footer")

    def rate_product(self, rating: int, comment: str) -> bool:
        """Rates a product and submits a review"""

        # Check if user has already rated the product
        try:
            restriction_message = self.find_element(self.REVIEW_RESTRICTION)
            if restriction_message:
                print("User has already reviewed this product. Attempting to delete and re-rate...")
                self.delete_existing_review()
        except NoSuchElementException:
            pass  # No previous review found, proceed with rating

        # Click on the star rating
        stars = self.find_elements(self.STARS)
        if 1 <= rating <= len(stars):
            stars[rating - 1].click()
        else:
            print("Invalid rating value. Should be between 1 and 5.")
            return False

        # Enter review comment
        self.enter_text(self.REVIEW_TEXTAREA, comment)

        # Submit the review
        self.click(self.SUBMIT_REVIEW_BUTTON)

        # Verify submission success
        try:
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(self.REVIEW_RESTRICTION)
            )
            return True  # Successfully submitted
        except TimeoutException:
            print("Review submission might have failed.")
            return False

    def delete_existing_review(self):
        """Deletes an existing review if found"""
        try:
            # Open the menu dropdown
            self.click(self.MENU_ICON)

            # Click delete button
            self.click(self.DELETE_BUTTON)

            # Wait for the review section to update
            WebDriverWait(self.driver, 5).until(
                EC.invisibility_of_element_located(self.REVIEW_RESTRICTION)
            )
            print("Existing review deleted successfully.")
        except (NoSuchElementException, TimeoutException):
            print("Failed to delete existing review.")

    def get_displayed_reviews(self):
        """Returns a list of the text from each review's <div class='comment-footer'>."""
        reviews = []
        try:
            # Wait for at least one comment block to appear
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_all_elements_located(self.COMMENT_BLOCKS)
            )
            comment_divs = self.find_elements(self.COMMENT_BLOCKS)

            for div in comment_divs:
                # Inside each comment block, find the footer text
                footer_div = div.find_element(*self.COMMENT_FOOTER)
                reviews.append(footer_div.text.strip())
        except TimeoutException:
            print("No reviews found or they didn't load in time.")
        return reviews
