from Page_Object.Location_Pom.Location_Locators import Location_Locator

class Location_prop(Location_Locator):

    @property
    def select_change(self):
        return self.driver.find_element(*Location_Locator.change)

    @property
    def select_confirm(self):
        return self.driver.find_element(*Location_Locator.confirm)

    @property
    def select_done(self):
        return self.driver.find_element(*Location_Locator.done)

