from pom.pages.login_page import LoginPage
from pom.pages.menu_page import MenuPage
from pom.tests.base_test import BaseTest
import time


class TestJsonLogin(BaseTest):
    def setUp(self) -> None:
        super().setUp()
        self.menu = MenuPage(self.driver)
        self.login = LoginPage(self.driver)

    def test_json_login_data(self):
        self.menu.click_on_pages()
        time.sleep(2)
        self.menu.click_on_login()
        time.sleep(2)
        self.login.remember_me()
        time.sleep(2)
        self.login.login()
        time.sleep(2)
