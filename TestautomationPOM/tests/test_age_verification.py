import pytest
from TestautomationPOM.utils.helpers import format_date
from TestautomationPOM.pages.home_page import HomePage
from TestautomationPOM.utils.constants import BASE_URL


@pytest.mark.parametrize("day, month, year, expected_message", [
    (1, 1, 2010, "You are underage"),   # Underage access denied
    (1, 1, 2000, "You are of age"),     # Access granted at 18+
    (None, None, None, "You are underage"),  # No birthdate provided
])
def test_age_verification(driver, day, month, year, expected_message):
    driver.get(BASE_URL)
    home_page = HomePage(driver)
    store_page = home_page.go_to_shop()

    if day and month and year:
        date_of_birth = format_date(day, month, year)
    else:
        date_of_birth = ""  # Simulate empty input for Error Guessing case
    status = store_page.handle_age_verification(date_of_birth)
    assert expected_message in status, f"Expected '{expected_message}' in age verification message, but got: '{status}'"


