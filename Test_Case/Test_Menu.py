import time
from Base_Test.Base_Test import BaseTest
from Login_pom.Login import Login
from Menu_pom.Menu import Menu
from Restaurant_pom.Restaurant import Restaurant
from Search_pom.Search import Search


class TestMenu(BaseTest):

    def test_menu(self):
        #url="https://foodmandu.com/Restaurant/Details/2069#!#Category49907"
        url=self.values["base_url"]
        self.driver.get(url)

        #login
        loginobj = Login(self.driver)
        Email = self.values["email"]
        Password = self.values["password"]
        loginobj.Login_Page(Email, Password)

        # search
        searchobj = Search(self.driver)
        restaurant = self.values["restaurant"]
        searchobj.Search_item(restaurant)
        time.sleep(20)

        #select restaurant
        restobj = Restaurant(self.driver)
        restobj.choose_restaurant()

        #menu
        menuobj = Menu(self.driver)
        menuobj.menu()

        time.sleep(5)





