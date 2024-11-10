import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_argument("--enable-logging")
options.add_argument("--v=1")

service = Service(ChromeDriverManager().install())
try:
    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://www.google.com")
    time.sleep(10000)  # Keep the browser open for 5 seconds
except Exception as e:
    print(f"Error occurred: {e}")
finally:
    driver.quit()
