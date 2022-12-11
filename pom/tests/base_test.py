import unittest

from selenium import webdriver


class BaseTest(unittest.TestCase):
    def setUp(self) -> None:  # implementam setup
        self.driver = webdriver.Chrome()

    def tearDown(self) -> None:
        self.driver.quit()
