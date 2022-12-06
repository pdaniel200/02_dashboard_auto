from selenium import webdriver

from pom.pages.base_page import BasePage
from pom.resources.menu_locators import MenuLocators, ComponentsLocators, PagesLocators


class MenuPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_on_components(self):
        self.click(MenuLocators.components_menu)

    def click_on_cards(self):
        self.click(ComponentsLocators.components_cards_menu)

    def click_on_pages(self):
        self.click(MenuLocators.pages_menu)

    def click_on_login(self):
        self.click(PagesLocators.pages_login_menu)
