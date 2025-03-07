import pytest
from TestautomationPOM.pages.login_page import LoginPage

@pytest.fixture
def login_page(driver):
    """ Return the login page instance """
    driver.get("https://grocerymate.masterschool.com/auth")
    return LoginPage(driver)


def test_valid_login(login_page, driver):
    # Arrange
    username = "johndoe@example.com"
    password = "admin123"

    # Act
    login_page.login(username, password)

    # Assert
    login_page.get_page_url("https://grocerymate.masterschool.com/")
    assert driver.current_url == "https://grocerymate.masterschool.com/"


def test_invalid_login(login_page):
    # Arrange
    username = "aa@m.sdv"
    password = "abc123"

    # Act
    login_page.login(username, password)

    # Assert
    assert login_page.get_error_message() == "Invalid username or password"
