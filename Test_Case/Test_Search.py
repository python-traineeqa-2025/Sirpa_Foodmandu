import time

from selenium.webdriver.common.by import By

from Base_Test.Base_Test import BaseTest
from Page_Object.Search_pom import Search

class TestSearch(BaseTest):

    def test_Search(self):
        url=self.values["base_url"]
        self.driver.get(url)

        searchobj = Search(self.driver)

        restaurant = self.values["restaurant"]
        #location = self.values["location"]

        searchobj.Search_item(restaurant)

        location = self.driver.find_element(By.XPATH, "//span[text()=\'Change\']")
        location.click()

        confirm = self.driver.find_element(By.XPATH, "//a[text()=\'Confirm this Location\']")
        confirm.click()

        done = self.driver.find_element(By.XPATH, "//label[text()=\'Done\']")
        done.click()

        time.sleep(8)