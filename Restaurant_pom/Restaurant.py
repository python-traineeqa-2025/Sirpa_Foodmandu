from Restaurant_pom.Restaurant_prop import Restaurant_prop

class Restaurant(Restaurant_prop):
    def __init__(self, driver):
        self.driver = driver

    def choose_restaurant(self):

        pepe=self.select_restaurant
        pepe.click()