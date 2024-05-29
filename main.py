from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

# Correctly initialize the service
service = Service(executable_path="./chromedriver")
# Initialize the WebDriver with the service
driver = webdriver.Chrome(service=service)

# Open Google
driver.get("https://google.com")

# Wait for 10 seconds
time.sleep(10)

# Quit the driver
driver.quit()
