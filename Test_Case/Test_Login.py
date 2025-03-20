import time
from Base_Test.Base_Test import BaseTest
from Page_Object.Login_pom import Login

class TestLogin(BaseTest):

    def test_Login(self):
        url=self.values["base_url"]
        self.driver.get(url)
        print("Page title:",self.driver.title)

                                        #Login Page
        lg = Login(self.driver)

        Email = self.values["email"]
        Password= self.values["password"]

        lg.Login_Page(Email, Password)

        time.sleep(2)