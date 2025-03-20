from selenium.common import ElementClickInterceptedException
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Page_Object.Menu_pom.Menu_prop import Menu_prop

class Menu(Menu_prop):

    def __init__(self, driver):
        self.driver = driver

    def menu(self):

        self.driver.execute_script('scrollBy(0,300)')
        time.sleep(2)
        #to select pizza from categories
        food=self.select_food
        self.driver.execute_script("arguments[0].scrollIntoView();",food)
        food.click()
        time.sleep(5)

        #To select Margarita pizza
        try:
            # parent = self.driver.find_element(By.XPATH, "//ul[contains(@class, 'menu__items')]")
            # element = parent.find_element(By.XPATH, "//li//div[@class='menu__price']")
            #element=self.driver.find_element(By.XPATH, "(//li[@class='d-flex justify-content-between ng-scope'])[72]")
            element=self.margaritta_pizza
            self.driver.execute_script("arguments[0].click();", element)

        except ElementClickInterceptedException:
            # Scroll into view
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

            # Wait for element to be clickable
            element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//li//div[@class='menu__price']"))
            )

            # Use JavaScript click
            self.driver.execute_script("arguments[0].click();", element)


        #time.sleep(5)

        # pizza_type=self.select_pizza
        # self.driver.execute_script("arguments[0].scrollIntoView(true);", pizza_type)
        # pizza_type.click()

        #pizza_type.click()
        # try:
        #     parent = self.driver.find_element(By.XPATH, "//ul[contains(@class, 'menu__items')]")
        #     parent.find_element(By.XPATH ,"//li//div[@class='menu__price']").click()
        #
        # except ElementClickInterceptedException:
        #     parent = self.driver.find_element(By.XPATH, "//ul[contains(@class, 'menu__items')]")
        #     parent.find_element(By.XPATH, "//li//div[@class='menu__price']").click()






