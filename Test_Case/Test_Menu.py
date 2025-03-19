import time
from selenium.webdriver.common.by import By

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
        searchobj.search_item(restaurant)

        location=self.driver.find_element(By.XPATH,"//span[text()=\'Change\']")
        location.click()

        confirm=self.driver.find_element(By.XPATH,"//a[text()=\'Confirm this Location\']")
        confirm.click()

        done=self.driver.find_element(By.XPATH,"//label[text()=\'Done\']")
        done.click()

        time.sleep(2)

        #select restaurant
        restobj = Restaurant(self.driver)
        restobj.choose_restaurant()

        #menu
        menuobj = Menu(self.driver)
        menuobj.menu()

'''


//span[text()='Change']

//a[text()='Confirm this Location']

//label[text()='Done']

menu:
parent=//ul[contains(@class, 'menu__items')][contains(., 'Pizza')]
//ul[contains(@class, 'menu__items')][text()='Pizza']

 

 
'''



