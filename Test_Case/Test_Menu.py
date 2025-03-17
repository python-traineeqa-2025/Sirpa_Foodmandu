import time
from Base_Test.Base_Test import BaseTest
from Menu_pom.Menu import Menu


class TestMenu(BaseTest):

    def test_menu(self):
        url="https://foodmandu.com/Restaurant/Details/2069#!#Category49907"
        self.driver.get(url)


        menuobj=Menu(self.driver)
        menuobj.menu()

        time.sleep(3)



