from selenium import webdriver
from pathlib import Path
import time
from selenium.webdriver.common.by import By


def test_price():
    my_driver = webdriver.Chrome()
    html_file = Path.cwd() / "website/index.html"
    my_driver.get(html_file.as_uri())
    time.sleep(3)

    monthly_revenue = (By.ID, 'price')
    monthly_revenue_value = my_driver.find_element(*monthly_revenue).text
    print(monthly_revenue_value)
    assert '$' in monthly_revenue_value

# comanda din terminal pytest --html=test_price.html