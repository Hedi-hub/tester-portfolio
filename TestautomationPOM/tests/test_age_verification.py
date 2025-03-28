import pytest
from TestautomationPOM.utils.helpers import format_date
from TestautomationPOM.pages.home_page import HomePage
from TestautomationPOM.utils.constants import BASE_URL


@pytest.mark.parametrize("day, month, year, expected_output", [
    (2, 1, 2010, "You are underage")
])
def test_age_verification(driver, day, month, year, expected_output):
    date_of_birth = format_date(day, month, year)
    driver.get(BASE_URL)
    home_page = HomePage(driver)
    store_page = home_page.go_to_shop()
    status = store_page.handle_age_verification(date_of_birth)
    assert expected_output in status

