
from Base_Test.Base_Test import BaseTest
from Restaurant_pom.Restaurant import Restaurant

class TestRestaurant(BaseTest):

    def testRestaurant(self):


        url="https://foodmandu.com/Restaurant/Index?q=pepe%20pizza&k=restaurant&c=&cty=1&sortby=4"
        self.driver.get(url)

        restobj = Restaurant(self.driver)
        restobj.choose_restaurant()

