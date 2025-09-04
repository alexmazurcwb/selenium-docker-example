from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

chrome_options = Options()
chrome_options.add_argument("--headless")  # Run Chrome in headless mode
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.google.com")

print("Title:", driver.title)

# Ensure screenshots folder exists
screenshots_dir = "/screenshots"
os.makedirs(screenshots_dir, exist_ok=True)
screenshot_path = os.path.join(screenshots_dir, "google.png")
driver.save_screenshot(screenshot_path)
print(f"Screenshot saved to {screenshot_path}")

driver.quit()