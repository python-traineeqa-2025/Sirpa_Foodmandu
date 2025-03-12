from Login_pom.Login_Locators import Login_Locators


class Login_Prop(Login_Locators):

    @property
    def go_login(self):
        return self.driver.find_element(*Login_Locators.Go_login)

    @property
    def email_input(self):
        return self.driver.find_element(*Login_Locators.Email)

    @property
    def password_input(self):
        return self.driver.find_element(*Login_Locators.Password)

    @property
    def checkbox_tick(self):
        return self.driver.find_element(*Login_Locators.Checkbox)

    @property
    def login_button(self):
        return self.driver.find_element(*Login_Locators.Login_btn)

