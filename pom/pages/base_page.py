from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click(self, by_locator):
        WebDriverWait(self.driver, timeout=10).until(EC.visibility_of_element_located(by_locator)).click()

    def enter_text(self, by_locator, text):
        WebDriverWait(self.driver, timeout=10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_text(self, by_locator):
        return WebDriverWait(self.driver, timeout=10).until(EC.visibility_of_element_located(by_locator)).text
