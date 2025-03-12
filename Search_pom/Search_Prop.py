from Search_pom.Search_Locators import Search_Locators

class Search_Prop(Search_Locators):
    @property
    def search_input(self):
        return self.driver.find_element(*Search_Locators.bar)

    @property
    def search_magnifier(self):
        return self.driver.find_element(*Search_Locators.search_button)

    def location_input(self):
        return self.driver.find_element(*Search_Locators.location)