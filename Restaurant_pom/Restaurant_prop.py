from Restaurant_pom.Restaurant_Locators import Restaurant_Locators

class Restaurant_prop(Restaurant_Locators):

    @property
    def select_restaurant(self):
        return self.driver.find_element(*Restaurant_Locators.restaurant_location)
