import logging
from Search_pom.Search_Prop import Search_Prop

class Search(Search_Prop):

    def __init__(self,driver):
        self.driver = driver

    def Search_item(self,restaurant):

        search_bar = self.search_input
        search_bar.click()
        search_bar.send_keys(restaurant)

        magnifier = self.search_magnifier
        magnifier.click()





