from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, NoAlertPresentException
from TestautomationPOM.pages.base_page import BasePage


class ProductRatingPage(BasePage):
    """Handles product rating and review functionality."""

    # --- Locators ---
    REVIEW_RESTRICTION = (By.XPATH, "//p[text()='You have already reviewed this product.']")
    STAR_FILLED = (By.CSS_SELECTOR, "span.star.filled")
    STARS = (By.XPATH, "//div[@class='interactive-rating']//span")
    COMMENT_INPUT = (By.CLASS_NAME, "new-review-form-control")
    SUBMIT_BUTTON = (By.CLASS_NAME, "new-review-btn-send")
    COMMENT_AUTHOR = (By.XPATH, "//div[@class='comments-container']//div[@class='comment'][1]//strong")  # Just for you name check
    COMMENT_TEXT = (By.CSS_SELECTOR, "div.comment-footer")
    MENU_ICON = (By.XPATH, "//div[@class='menu-icon']")
    EDIT_BUTTON = (By.XPATH, "//div[@class='dropdown-menu']/button[text()='Edit']")
    DELETE_BUTTON = (By.XPATH, "//div[@class='dropdown-menu']/button[text()='Delete']")
    EDIT_INPUT = (By.CSS_SELECTOR, "div.modal textarea")
    SAVE_EDIT_BUTTON = (By.XPATH, "//button[text()='Save Changes']")
    DROPDOWN_MENU = (By.XPATH, "//div[@class='dropdown-menu']")

    def has_review_restriction(self):
        """Checks if the 'already reviewed' restriction message appears."""
        try:
            # Wait until the element is visible
            element = WebDriverWait(self.driver, self.timeout).until(
                EC.visibility_of_element_located(self.REVIEW_RESTRICTION)
            )
            return element.is_displayed()
        except TimeoutException:
            # If element is not found, return False, meaning no restriction
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
            dropdown_menu = self.find_element(self.DROPDOWN_MENU)
            if dropdown_menu.is_displayed():
                print("✅ Dropdown Menu is displayed")
                self.click(self.DELETE_BUTTON)
                # Handle the confirmation alert
                try:
                    WebDriverWait(self.driver, 5).until(EC.alert_is_present())
                    alert = self.driver.switch_to.alert
                    print(f"⚠️ Alert Text: {alert.text}")
                    alert.accept()  # Accept the alert (click "OK")
                    print("✅ Alert accepted.")
                except NoAlertPresentException:
                    print("⚠️ No alert present when expected.")

            WebDriverWait(self.driver, 10).until(
                        EC.invisibility_of_element_located(self.REVIEW_RESTRICTION)
            )
            print("✅ Existing review deleted.")
        except (NoSuchElementException, TimeoutException):
            print("⚠️ No review to delete or deletion failed.")