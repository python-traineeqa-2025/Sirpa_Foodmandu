from selenium.webdriver.common.by import By


class Login_Locators(object):
    Email =(By.NAME, "Email")
    Password =(By.NAME,"Password")
    Checkbox=(By.CSS_SELECTOR, 'input[type=\"checkbox\"] + label')
    Login_btn=(By.CSS_SELECTOR, '.btn-block')