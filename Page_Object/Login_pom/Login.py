import logging

from selenium.common import NoSuchElementException

from Page_Object.Login_pom.Login_prop import Login_Prop

class Login(Login_Prop):

    def __init__(self, driver):
        self.driver = driver

    def Login_Page(self, Email, Password):

        login= self.go_login
        login.click()

        email = self.email_input
        email.send_keys(Email)

        pwd = self.password_input
        pwd.send_keys(Password)

        checkbox=self.checkbox_tick
        checkbox.click()

        loginbtn = self.login_button
        loginbtn.click()


        try:
            login_error = self.wrong_login
            logging.info(login_error.text)
        except NoSuchElementException:
            print("User logged in successfully")











