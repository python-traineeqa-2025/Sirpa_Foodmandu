from Menu_pom.Menu_Locator import Menu_locator

class Menu_prop(Menu_locator):

    @property
    def select_food(self):
        return self.driver.find_element(*Menu_locator.food_item)

    @property
    def select_pizza(self):
        return self.driver.find_element(*Menu_locator.pizza)