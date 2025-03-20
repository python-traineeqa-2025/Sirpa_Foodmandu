from Page_Object.Checkout_Pom.Checkout_Locators import Checkout_Locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Checkout_Prop(Checkout_Locators):

    @property
    def go_checkout(self):
        return self.driver.find_element(*Checkout_Locators.checkout_btn)

    @property
    def input_address(self):
        #return self.driver.find_element(*Checkout_Locators.enterloc_btn)
        return self.wait.until(
            EC.element_to_be_clickable(Checkout_Locators.enterloc_btn)
        )

    @property
    def auto_suggest(self):
        return self.wait.until(
            EC.element_to_be_clickable(Checkout_Locators.auto_suggest_item)
        )

    @property
    def confirm_location(self):
        return self.wait.until(
            EC.element_to_be_clickable(Checkout_Locators.confirmLoc_btn)
        )

    @property
    def address_title(self):
        return self.driver.find_element(*Checkout_Locators.address_title)

    @property
    def input_direction(self):
        return self.driver.find_element(*Checkout_Locators.direction)

    @property
    def input_phone(self):
        return self.driver.find_element(*Checkout_Locators.phone)

    @property
    def set_default_address(self):
        return self.driver.find_element(*Checkout_Locators.default_chk)

    @property
    def click_save(self):
        return self.driver.find_element(*Checkout_Locators.save)

    @property
    def schedule_delivery(self):
        return self.driver.find_element(*Checkout_Locators.schedule_delivery_btn)

    @property
    def select_date(self):
        return self.driver.find_element(*Checkout_Locators.date_btn)

    @property
    def select_time(self):
        return self.driver.find_element(*Checkout_Locators.time_btn)

    @property
    def payment_option(self):
        return self.driver.find_element(*Checkout_Locators.pay_option)

    @property
    def click_continue(self):
        return self.driver.find_element(*Checkout_Locators.continue_btn)






