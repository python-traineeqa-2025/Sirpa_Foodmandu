import logging

from selenium.common import StaleElementReferenceException

from Search_pom.Search_Prop import Search_Prop

class Search(Search_Prop):

    def __init__(self,driver):
        self.driver = driver

    def search_item(self,restaurant):
        try:

            search_bar = self.search_input
            search_bar.click()
            search_bar.send_keys(restaurant)

        except StaleElementReferenceException:
            search_bar = self.search_input
            search_bar.click()
            search_bar.send_keys(restaurant)

        magnifier = self.search_magnifier
        magnifier.click()










