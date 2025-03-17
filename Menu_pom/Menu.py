from Menu_pom.Menu_prop import Menu_prop
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Menu(Menu_prop):

    def __init__(self, driver):
        self.driver = driver

    def menu(self):
        food=self.select_food
        #self.driver.execute_script("arguments[0].scrollIntoView();",food)\
        food.click()

        pizza_type=self.select_pizza
        self.driver.execute_script("arguments[0].scrollIntoView();", pizza_type)

        # logged_in_element = WebDriverWait(self.driver, 10).until(
        #     EC.visibility_of_element_located((pizza_type.click())
        #     ))

        self.driver.implicitly_wait(10)
        pizza_type.click()



