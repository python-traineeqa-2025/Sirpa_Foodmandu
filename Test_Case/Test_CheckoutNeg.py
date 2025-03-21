from Base_Test.Base_Test import BaseTest
from Page_Object.Login_pom.Login import Login
from Page_Object.Checkout_Pom.Checkout import Checkout

class TestNegCheckout(BaseTest):

    def test_neg_checkout(self):

        url = self.values["base_url"]
        self.driver.get(url)

        # login
        loginobj = Login(self.driver)
        Email = self.values["email"]
        Password = self.values["password"]
        loginobj.Login_Page(Email, Password)

        #neg_checkout
        negcobj= Checkout(self.driver)
        Nlocation="haatttiisaarr"
        negcobj.Neg_checkout_page(Nlocation)