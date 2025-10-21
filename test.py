#!/usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import os

BASE_DIR = os.path.dirname(__file__)
chromedriver_path = os.path.join(BASE_DIR, "chromedriver")
service = Service(executable_path=chromedriver_path)

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    driver.get("https://www.google.com")
    print("Title:", driver.title)

    screenshots_dir = os.path.join(BASE_DIR, "screenshots")
    os.makedirs(screenshots_dir, exist_ok=True)
    screenshot_path = os.path.join(screenshots_dir, "google.png")
    driver.save_screenshot(screenshot_path)
    print(f"Screenshot saved to {screenshot_path}")
finally:
    driver.quit()
