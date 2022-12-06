from selenium.webdriver.common.by import By


class LoginLocators:
    email_field = (By.CSS_SELECTOR, '#exampleInputEmail')
    password_field = (By.CSS_SELECTOR, '#exampleInputPassword')
    remember_me_checkbox = (By.CSS_SELECTOR, 'body > div > div > div > div > div > div > div:nth-child(2) > div > form > div:nth-child(3) > div > label')
    login_btn = (By.CSS_SELECTOR, 'body > div > div > div > div > div > div > div:nth-child(2) > div > form > a.btn.btn-primary.btn-user.btn-block')
