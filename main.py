# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from selenium import webdriver
from pathlib import Path
import time
from selenium.webdriver.common.by import By

my_driver = webdriver.Chrome()
html_file = Path.cwd() / "website/index.html"
my_driver.get(html_file.as_uri())
time.sleep(3)

monthly_revenue = (By.ID, 'price')
monthly_revenue_value = my_driver.find_element(*monthly_revenue).text
print(monthly_revenue_value)
assert '$' in monthly_revenue_value
