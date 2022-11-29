import unittest

from selenium import webdriver

from pom.pages.home_page import HomePage


class BaseTest(unittest.TestCase):
    def setUp(self) -> None:  # implementam setup
        self.driver = webdriver.Chrome()


class TestRevenue(BaseTest):
    def setUp(self) -> None:  # se face override la metoda de setup
        super().setUp()
        self.home_page = HomePage(self.driver)  # clasa din pachetul homepage

    def test_monthly_revenue(self):
        text = self.home_page.get_monthly_earning()
        self.assertIn('$', text)


if __name__ == '__main__':
    unittest.main()

#TODO de crat pentru fiecare pagina din sait cate o clasa in care sa stocam actiunile, op pagina in care stocam locatorii pt fiecare pagina si dupa aia teste - calasa homepage, clasa utilities, etc...