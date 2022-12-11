from pom.pages.login_page import LoginPage
from pom.pages.menu_page import MenuPage
from pom.tests.base_test import BaseTest


class TestLogin(BaseTest):
    def setUp(self) -> None:
        super().setUp()
        self.menu = MenuPage(self.driver)
        self.login = LoginPage(self.driver)

    def test_valid_email_and_password(self):
        self.menu.click_on_pages()
        self.menu.click_on_login()
        self.login.enter_email(my_dict["user_valid"])
        # self.login.enter_email('x@y.com')
        self.login.enter_password('1234')
        self.login.remember_me()
        self.login.login()


    def test_empty_email_and_password(self):
        self.menu.click_on_pages()
        self.menu.click_on_login()
        self.login.remember_me()
        self.login.login()





#todo de introdus la fiecare test si cate un assert,
#todo 10 scenarii de a testa login-ul
#todo de creat o functie care citeste dintr-un fisier JSON datele de login
