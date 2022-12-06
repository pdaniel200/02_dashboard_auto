from pathlib import Path

from pom.pages.base_page import BasePage
from pom.resources.home_locators import HomePageLocators


class HomePage(BasePage):  # mosteneste pe BasePage
    def __init__(self, driver):
        super().__init__(
            driver)  # face referire in mod direct la instanta clasei parinte, ca si cum ar fi fost BasePage


    def get_monthly_earning(self):
        return self.get_text(HomePageLocators.monthly_revenue)

    def get_annual_earning(self):
        return self.get_text(HomePageLocators.yearly_revenue)
