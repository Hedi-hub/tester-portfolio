import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.get("http://automationexercise.com")
    driver.maximize_window()
    yield driver
    driver.quit()


def test_user_registration(driver):
    wait = WebDriverWait(driver, 30)

    # Click on "Signup/Login"
    # wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Signup')]"))).click()

    # Handle Cookie Popup
    try:
        cookie_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@class='fc-button fc-cta-consent fc-primary-button']")))
        cookie_button.click()
        print("Cookie consent accepted.")
    except:
        print("No cookie popup found, continuing...")

        # Scroll and click "Signup/Login"
    signup_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/login']")))
    driver.execute_script("arguments[0].scrollIntoView();", signup_button)
    signup_button.click()
    print("Clicked 'Signup/Login' button.")

    # Verify "New User Signup!" is visible
    assert "New User Signup!" in driver.page_source

    # Enter name and email
    wait.until(EC.presence_of_element_located((By.NAME, "name"))).send_keys("Hello World")
    wait.until(EC.presence_of_element_located((By.XPATH, "//input[@data-qa='signup-email']"))).send_keys("helloworld2022@example.com")
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@data-qa='signup-button']"))).click()

    # Verify "ENTER ACCOUNT INFORMATION" is visible
    assert "Enter Account Information" in driver.page_source

    # Fill in account details
    wait.until(EC.presence_of_element_located((By.ID, "password"))).send_keys("TestPass123")
    wait.until(EC.element_to_be_clickable((By.ID, "newsletter"))).click()
    wait.until(EC.element_to_be_clickable((By.ID, "optin"))).click()

    # Verify "ADDRESS INFORMATION" is visible
    assert driver.find_element(By.XPATH, "//b[contains(text(), 'Address Information')]").is_displayed()

    # Fill in personal details
    driver.find_element(By.ID, "first_name").send_keys("Hello ")
    driver.find_element(By.ID, "last_name").send_keys("World")
    driver.find_element(By.ID, "address1").send_keys("Wöhlertstrasse")
    driver.find_element(By.ID, "city").send_keys("Berlin")
    driver.find_element(By.ID, "state").send_keys("Berlin")
    driver.find_element(By.ID, "zipcode").send_keys("10115")
    driver.find_element(By.ID, "mobile_number").send_keys("123456789")

    # Click "Create Account"
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@data-qa='create-account']"))).click()

    # Verify "ACCOUNT CREATED!" is visible
    assert "Account Created!" in driver.page_source

    # Click "Continue"
    wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@data-qa='continue-button']"))).click()

    # Delete the account
    wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/delete_account']"))).click()

    # Verify "ACCOUNT DELETED!" is visible
    assert "Account Deleted!" in driver.page_source

    print("User Registration Test Passed!")