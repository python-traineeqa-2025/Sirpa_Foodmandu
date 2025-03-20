
from Base_Test.Base_Test import BaseTest
from Page_Object.Search_pom.Search import Search
from Page_Object.Restaurant_pom.Restaurant import Restaurant

class TestRestaurant(BaseTest):

    def testRestaurant(self):

        url = self.values["base_url"]
        #url="https://foodmandu.com/Restaurant/Index?q=pepe%20pizza&k=restaurant&c=&cty=1&sortby=4"
        searchobj = Search(self.driver)

        restaurant = self.values["restaurant"]
        # location = self.values["location"]
        searchobj.search_item(restaurant)
        self.driver.get(url)

        restobj = Restaurant(self.driver)
        restobj.choose_restaurant()

