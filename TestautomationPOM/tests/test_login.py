import pytest
from TestautomationPOM.pages.login_page import LoginPage
from TestautomationPOM.utils.constants import BASE_URL, TEST_USERNAME, TEST_PASSWORD, TEST_EMAIL


def test_login_valid_credentials(driver):
    """ Test valid login credentials """
    driver.get(BASE_URL)
    login_page = LoginPage(driver)
    login_page.login(TEST_EMAIL, TEST_PASSWORD)
    assert login_page.is_logged_in(), "Login failed with valid credentials"
