from Page_Object.Cart_Pom.Cart_Locators import Cart_Locators

class Cart_prop(Cart_Locators):

    @property
    def select_fav(self):
        return self.driver.find_element(*Cart_Locators.fav)

    @property
    def select_desc(self):
        return self.driver.find_element(*Cart_Locators.desc_box)

    @property
    def select_add(self):
        return self.driver.find_element(*Cart_Locators.add)

    @property
    def select_minus(self):
        return self.driver.find_element(*Cart_Locators.minus)

    @property
    def select_bag(self):
        return self.driver.find_element(*Cart_Locators.bag)





