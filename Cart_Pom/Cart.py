import time
from Cart_Pom.Cart_prop import Cart_prop

class Cart(Cart_prop):

    def __init__(self, driver):
        self.driver = driver

    def add_cart(self,instruction):
        fav_button=self.select_fav
        fav_button.click()

        inst=self.select_desc
        inst.click()
        inst.send_keys(instruction)

        plus=self.select_add
        plus.click()
        time.sleep(2)

        minus=self.select_minus
        minus.click()
        time.sleep(2)

        bag_button=self.select_bag
        bag_button.click()




