import pytest
import time
from selenium import webdriver
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()


@pytest.mark.parametrize("username,password,pass_test", [
    ("standard_user", "secret_sauce", True),
    ("locked_out_user", "secret_sauce", False),
    ("problem_user", "secret_sauce", True),
    ("performance_glitch_user", "secret_sauce", True),
    ("error_user", "secret_sauce", True),
    ("visual_user", "secret_sauce", True)
])
def test_login(driver, username, password, pass_test):
    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()

    # Verify login
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "title"))
        )
        login_success = True
    except (NoSuchElementException, TimeoutException):
        login_success = False

    assert login_success == pass_test, f"Test failed for user: {username}"
    time.sleep(4)
