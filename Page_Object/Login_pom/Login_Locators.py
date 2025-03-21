from selenium.webdriver.common.by import By


class Login_Locators(object):
    Go_login=(By.XPATH,"//button[@class='btn btn--hollow hidden-sm-down']")
    Email =(By.NAME, "Email")
    Password =(By.NAME,"Password")
    Checkbox=(By.CSS_SELECTOR, 'label[for=\'agreement\']')
    Login_btn=(By.CSS_SELECTOR, 'button[type=\'submit\']')
    error_login=(By.XPATH,"//p[@class='page-notifications page-notifications--error']")