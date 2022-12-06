from selenium.webdriver.common.by import By


class MenuLocators:
    components_menu = (By.CSS_SELECTOR, '#accordionSidebar > li:nth-child(6) > a > span')
    pages_menu = (By.CSS_SELECTOR, '#accordionSidebar > li:nth-child(10) > a > span')


class ComponentsLocators:
    components_cards_menu = (By.CSS_SELECTOR, '#collapseTwo > div > a.collapse-item.active')


class PagesLocators:
    pages_login_menu = (By.CSS_SELECTOR, '#collapsePages > div > a:nth-child(2)')
