import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from TestautomationPOM.pages.registration_page import RegistrationPage
from TestautomationPOM.utils.constants import BASE_URL

def test_registration_valid_data(driver):
    """ Test successful registration with valid credentials """
    driver.get(BASE_URL)  # Open the login page
    registration_page = RegistrationPage(driver)

    try:
        # Click "Create a new account"
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(@class, 'switch-link') and text()='Create a new account']"))
        ).click()

        # Perform Registration
        registration_page.register("Test Me", "testme@example.com", "1q2w3e4r5t6z")

        # Wait for success message
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'go3958317564') and contains(text(), 'Registration successful')]"))
        )

        # Assert success
        assert registration_page.is_registration_successful(), "Registration failed for valid data."

    except Exception as e:
        print(f"Test failed: {e}")
        registration_page.save_screenshot("registration_error.png")  # Capture a screenshot
        assert False, "Test failed - Screenshot captured!"


# def test_registration_missing_fields(driver):
#     """ Test registration with missing fields """
#     try:
#         driver.get(BASE_URL)
#         registration_page = RegistrationPage(driver)
#         registration_page.click_signup()  # Click "Sign Up" without entering anything
#
#         # Wait for the error message instead of checking for missing success message
#         WebDriverWait(driver, 5).until(
#             EC.presence_of_element_located(ERROR_MESSAGE)
#         )
#
#         assert True  # Test passes because the error message appeared.
#
#     except TimeoutException:
#         assert False, "Timeout: Expected validation message did not appear!"
#     except NoSuchElementException:
#         assert False, "Error: Could not find the expected validation message."
#     except Exception as e:
#         assert False, f"Unexpected error occurred: {str(e)}"
#
#
# def test_registration_existing_email(driver):
#     """ Test registration with an already registered email """
#     try:
#         driver.get(BASE_URL)
#         registration_page = RegistrationPage(driver)
#         registration_page.register("Existing User", "testuser1@example.com", "SecurePass123")
#
#         # Wait for the error message indicating email is already taken
#         try:
#             WebDriverWait(driver, 5).until(
#                 EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'This email is already registered')]"))
#             )
#             assert True
#         except TimeoutException:
#             assert False, "Error message did not appear for existing email."
