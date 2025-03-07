from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.select import Select


def test_checkbox():
    driver = webdriver.Chrome()
    driver.get("https://www.selenium.dev/selenium/web/web-form.html")
    time.sleep(3)

    my_check_1 = driver.find_element(By.ID, "my-check-1")
    my_check_2 = driver.find_element(By.ID, "my-check-2")

    if not my_check_2.is_selected():
        my_check_2.click()

    assert my_check_1.is_selected() == True and my_check_2.is_selected() == True


def test_multiple_checkboxes():
    driver = webdriver.Chrome()
    driver.get("http://www.tizag.com/htmlT/htmlcheckboxes.php")
    time.sleep(3)

    checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox' and @name='sports']")

    for checkbox in checkboxes:
        if checkbox.get_attribute("value") == "football":
            checkbox.click()


def test_dropdown():
    driver = webdriver.Chrome()
    driver.get("https://www.selenium.dev/selenium/web/web-form.html")
    time.sleep(3)

    dropdown_element = driver.find_element(By.XPATH, "//select[@name='my-select']")
    dropdown = Select(dropdown_element)
    time.sleep(1)
    # Method 1: Select by visible text
    dropdown.select_by_visible_text("Two")
    time.sleep(2)
    selected_option = dropdown.first_selected_option
    assert selected_option.text == "Two"

    # Method 2: Select by value
    dropdown.select_by_value("1")
    time.sleep(1)
    selected_option = dropdown.first_selected_option
    assert selected_option.text == "One"

    # Method 3: Select by index
    dropdown.select_by_index(3)
    time.sleep(1)
    selected_option = dropdown.first_selected_option
    assert selected_option.text == "Three"


def test_alert():
    driver = webdriver.Chrome()
    driver.get("https://www.selenium.dev/selenium/web/alerts.html#")
    time.sleep(3)

    alert_link = driver.find_element(By.ID, "prompt")
    alert_link.click()
    time.sleep(2)
    alert = driver.switch_to.alert
    time.sleep(2)

    # Send text to the alert
    alert.send_keys("Hello Selenium")
    time.sleep(2)

    print(alert.text)
    # Accept the alert
    alert.accept()


def test_login_valid():
    # setup code

    button = driver.find_element(By.ID, "//")


def test_invalid_login():
    # setup code

    button = driver.find_element(By.ID, "//")