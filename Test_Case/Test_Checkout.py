import time

from selenium.webdriver.common.by import By

from Base_Test.Base_Test import BaseTest
from Login_pom.Login import Login
from Search_pom.Search import Search
from Restaurant_pom.Restaurant import Restaurant
from Menu_pom.Menu import Menu
from Cart_Pom.Cart import Cart
from Checkout_Pom.Checkout import Checkout

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

        location = self.driver.find_element(By.XPATH, "//span[text()=\'Change\']")
        location.click()

        confirm = self.driver.find_element(By.XPATH, "//a[text()=\'Confirm this Location\']")
        confirm.click()

        done = self.driver.find_element(By.XPATH, "//label[text()=\'Done\']")
        done.click()

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
