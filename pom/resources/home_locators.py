from selenium.webdriver.common.by import By


class HomePageLocators:
    monthly_revenue = (By.ID, 'price')
    yearly_revenue = (By.CSS_SELECTOR, '#content > div > div:nth-child(2) > div:nth-child(2) > div > div > div > div.col.mr-2 > div.h5.mb-0.font-weight-bold.text-gray-800')

