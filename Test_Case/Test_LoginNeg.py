import time
from Base_Test.Base_Test import BaseTest
from Page_Object.Login_pom.Login import Login

class TestLogin(BaseTest):

    def test_Login_Neg(self):

        url=self.values["base_url"]
        self.driver.get(url)

        neg_lg= Login(self.driver)

        List_user = self.values['users']

        for uname, password in List_user.items():

            neg_lg.Login_Page(uname,password)
            time.sleep(1)

            self.driver.refresh()








