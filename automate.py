from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up the WebDriver (ensure the correct path to ChromeDriver is set)
driver = webdriver.Chrome()

# Open the web page
driver.get("http://localhost:5000")  # Replace with your Flask app URL

# Debugging: Print the page source to ensure the content is as expected
print(driver.page_source)

test_cases = [
    {"name": "John Doe", "email": "john.doe@example.com"},
    {"name": "Jane Smith", "email": "jane.smith@example.com"},
    {"name": "Alice Johnson", "email": "alice.johnson@example.com"},
    {"name": "Alice Johnson", "email": "alice.johnson@example.com"}
]

cases_done = 0

for case in test_cases:
    try:
        time.sleep(10)
        name = case["name"]
        email = case["email"]
        name_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'name')))
        email_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'email')))
        submit_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//input[@type="submit"]')))

        # Input data
        name_field.send_keys(name)
        email_field.send_keys(email)

        # Submit the form
        submit_button.click()

        # Print the page title after form submission
        cases_done+=1
        print("case:", cases_done, case, "\nsuccessfull")

    except Exception as e:
        print(f"An error occurred: {e}")

    # finally:
    #     # Wait briefly before closing to observe the result (not recommended for production code)
    #     time.sleep(2)
    #     # Close the browser
driver.quit()


