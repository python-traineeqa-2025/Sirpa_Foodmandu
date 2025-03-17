from Menu_pom.Menu_prop import Menu_prop

class Menu(Menu_prop):

    def __init__(self, driver):
        self.driver = driver

    def menu(self):
        food=self.select_food
        #self.driver.execute_script("arguments[0].scrollIntoView();",food)\
        food.click()

        pizza_type=self.select_pizza
        self.driver.execute_script("arguments[0].click();", pizza_type)





