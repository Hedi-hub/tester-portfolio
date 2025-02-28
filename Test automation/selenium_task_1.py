
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up the driver
driver = webdriver.Chrome()

# Step 1: Open the website
driver.get("https://www.saucedemo.com/")
time.sleep(3)

# Step 2: Locate the login fields and login
username_field = driver.find_element(By.ID, "user-name")
password_field = driver.find_element(By.ID, "password")
login_button = driver.find_element(By.ID, "login-button")
time.sleep(4)

username_field.send_keys("standard_user")
password_field.send_keys("secret_sauce")
login_button.click()
time.sleep(4)  # Wait for page to load

# Step 3: Verify successful login
products_header = driver.find_element(By.CLASS_NAME, "title")
assert "Products" in products_header.text
time.sleep(4)
# Step 4: Locate and verify the "Sauce Labs Backpack" product
product = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CLASS_NAME, "inventory_item_name"))
)
assert product.text == "Sauce Labs Backpack"
time.sleep(4)
print("Login and Product Verification Successful!")

driver.quit()