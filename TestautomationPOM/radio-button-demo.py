from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_radio_button():
    driver = webdriver.Chrome()
    driver.get("https://www.selenium.dev/selenium/web/web-form.html")
    time.sleep(3)
    my_radio_1 = driver.find_element(By.ID, "my-radio-1")
    my_radio_2 = driver.find_element(By.ID, "my-radio-2")
    time.sleep(2)
    if not my_radio_2.is_selected():
        my_radio_2.click()
    time.sleep(1)

    assert my_radio_2.is_selected() == True
