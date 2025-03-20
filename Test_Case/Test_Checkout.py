import time
from selenium.webdriver.common.by import By

from Base_Test.Base_Test import BaseTest
from Page_Object.Login_pom.Login import Login
from Page_Object.Search_pom.Search import Search
from Page_Object.Location_Pom.Location import Location
from Page_Object.Restaurant_pom.Restaurant import Restaurant
from Page_Object.Menu_pom.Menu import Menu
from Page_Object.Cart_Pom.Cart import Cart
from Page_Object.Checkout_Pom.Checkout import Checkout

class TestCheckout(BaseTest):

    def test_checkout(self):

        url = self.values["base_url"]
        self.driver.get(url)

        # login
        loginobj = Login(self.driver)
        Email = self.values["email"]
        Password = self.values["password"]
        loginobj.Login_Page(Email, Password)

        # search
        searchobj = Search(self.driver)
        restaurant = self.values["restaurant"]
        searchobj.search_item(restaurant)

        # location
        locationobj = Location(self.driver)
        locationobj.location()
        time.sleep(2)

        # select restaurant
        restobj = Restaurant(self.driver)
        restobj.choose_restaurant()

        # menu
        menuobj = Menu(self.driver)
        menuobj.menu()

        # cart
        description = self.values["instruction"]
        cartobj = Cart(self.driver)
        cartobj.add_cart(description)

        # checkout
        checkoutobj= Checkout(self.driver)
        checkoutobj.checkout_page()
