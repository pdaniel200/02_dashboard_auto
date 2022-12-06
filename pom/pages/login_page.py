from pom.pages.base_page import BasePage
from pom.resources.login_locators import LoginLocators


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(
            driver)  # face referire in mod direct la instanta clasei parinte, ca si cum ar fi fost BasePage

    def enter_email(self, text):
        self.enter_text(LoginLocators.email_field, text)

    def enter_password(self, text):
        self.enter_text(LoginLocators.password_field, text)

    def remember_me(self):
        self.click(LoginLocators.remember_me_checkbox)

    def login(self):
        self.click(LoginLocators.login_btn)

