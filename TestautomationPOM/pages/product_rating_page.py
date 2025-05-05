from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from TestautomationPOM.pages.base_page import BasePage


class ProductRatingPage(BasePage):
    """Handles product rating and review functionality."""

    # --- Locators ---
    REVIEW_RESTRICTION = (By.CLASS_NAME, "reviewRestriction")
    STAR_FILLED = (By.CSS_SELECTOR, "span.star.filled")
    STARS = (By.CSS_SELECTOR, "span.star")
    COMMENT_INPUT = (By.CLASS_NAME, "new-review-form-control")
    SUBMIT_BUTTON = (By.CLASS_NAME, "new-review-btn-send")
    COMMENT_AUTHOR = (By.CSS_SELECTOR, "div.comment h5")  # Just for you name check
    COMMENT_TEXT = (By.CSS_SELECTOR, "div.comment-footer")
    MENU_ICON = (By.CLASS_NAME, "menu-icon")
    EDIT_BUTTON = (By.XPATH, "//button[text()='Edit']")
    DELETE_BUTTON = (By.XPATH, "//button[text()='Delete']")
    EDIT_INPUT = (By.CSS_SELECTOR, "div.modal textarea")
    SAVE_EDIT_BUTTON = (By.XPATH, "//button[text()='Save Changes']")

    def has_review_restriction(self):
        """Checks if the 'already reviewed' restriction message appears."""
        try:
            return self.find_element(self.REVIEW_RESTRICTION).is_displayed()
        except NoSuchElementException:
            return False

    def click_star_rating(self, rating):
        """Clicks on the given star (1-5) to rate."""
        stars = self.find_elements(self.STARS)
        if 1 <= rating <= len(stars):
            stars[rating - 1].click()
        else:
            print("Invalid rating.")

    def count_filled_stars(self):
        """Returns the number of filled stars after selection."""
        try:
            filled = self.find_elements(self.STAR_FILLED)
            return len(filled)
        except Exception:
            return 0

    def submit_review(self, text):
        """Submits a new review."""
        self.enter_text(self.COMMENT_INPUT, text)
        self.click(self.SUBMIT_BUTTON)

    def get_own_review_name(self):
        """Returns the name attached to the most recent review."""
        try:
            return self.find_element(self.COMMENT_AUTHOR).text.strip()
        except Exception:
            return None

    def get_review_texts(self):
        """Returns all review texts."""
        try:
            comments = self.find_elements(self.COMMENT_TEXT)
            return [c.text.strip() for c in comments]
        except Exception:
            return []

    def edit_review(self, new_text):
        """Edits an existing review."""
        try:
            self.click(self.MENU_ICON)
            self.click(self.EDIT_BUTTON)
            self.enter_text(self.EDIT_INPUT, new_text)
            self.click(self.SAVE_EDIT_BUTTON)
        except Exception as e:
            print(f"Editing review failed: {e}")

    def delete_existing_review(self):
        """Deletes an existing review if restriction is active."""
        try:
            self.click(self.MENU_ICON)
            self.click(self.DELETE_BUTTON)
            WebDriverWait(self.driver, 5).until(
                EC.invisibility_of_element_located(self.REVIEW_RESTRICTION)
            )
            print("✅ Existing review deleted.")
        except (NoSuchElementException, TimeoutException):
            print("⚠️ No review to delete or deletion failed.")
