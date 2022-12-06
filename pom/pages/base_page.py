from pathlib import Path

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        html_file = Path.cwd().parent.parent / "website/index.html"  # se construieste url-ul pt acces index.html
        self.driver.get(html_file.as_uri())

    def click(self, by_locator):
        WebDriverWait(self.driver, timeout=10).until(EC.visibility_of_element_located(by_locator)).click()

    def enter_text(self, by_locator, text):
        WebDriverWait(self.driver, timeout=10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_text(self, by_locator):
        return WebDriverWait(self.driver, timeout=10).until(EC.visibility_of_element_located(by_locator)).text

