import time
from Base_Test.Base_Test import BaseTest
from Search_pom.Search import Search

class TestSearch(BaseTest):

    def test_Search(self):
        url=self.values["base_url"]
        self.driver.get(url)

        searchobj = Search(self.driver)

        restaurant = self.values["restaurant"]
        #location = self.values["location"]

        searchobj.Search_item(restaurant)

        time.sleep(8)