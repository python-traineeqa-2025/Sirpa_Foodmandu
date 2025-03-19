from selenium.webdriver.common.by import By

from Checkout_Pom.Checkout_prop import Checkout_Prop



class Checkout(Checkout_Prop):

    def __init__(self, driver):
        self.driver = driver

    def checkout_page(self):

        checkout=self.go_checkout
        checkout.click()

                            #address details pop up
        address=self.input_address
        address.click()
        address.send_keys("P86F+RRR, Kathmandu 44600, Nepal")

        confirm_address=self.confirm_location
        confirm_address.click()

        title=self.address_title
        title.click()
        title.send_keys("Infinite Solutions Pvt.Ltd")

        direction_details=self.input_direction
        direction_details.click()
        direction_details.send_keys("Hattisar")

        phone_number=self.input_phone
        phone_number.click()
        phone_number.send_keys("9834743721")

        default_address=self.set_default_address
        default_address.click()

        save_button=self.click_save
        save_button.click()

                        #Delivery Date and Time














