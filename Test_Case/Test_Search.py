import time

from selenium.webdriver.common.by import By

from Base_Test.Base_Test import BaseTest
from Page_Object.Search_pom.Search import Search
from Page_Object.Location_Pom.Location import Location

class TestSearch(BaseTest):

    def test_Search(self):
        url=self.values["base_url"]
        self.driver.get(url)

        searchobj = Search(self.driver)

        restaurant = self.values["restaurant"]
        #location = self.values["location"]

        searchobj.search_item(restaurant)

        # location
        locationobj = Location(self.driver)
        locationobj.location()
        time.sleep(2)

        time.sleep(8)