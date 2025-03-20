from selenium.webdriver.common.by import By

from Checkout_Pom.Checkout_prop import Checkout_Prop
from selenium.webdriver.support.select import Select


class Checkout(Checkout_Prop):

    def __init__(self, driver):
        self.driver = driver

    def checkout_page(self):

        checkout=self.go_checkout
        checkout.click()

                            #address details pop up
        address=self.input_address
        address.click()
        address.send_keys("Hattisar, Kathmandu, Nepal")

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
        schedule=self.schedule_delivery
        schedule.click()

        date_option=self.select_date
        date_option.click()
        date_dd=Select(date_option)
        date_dd.select_by_index(2)

        time_option=self.select_time
        time_option.click()
        time_dd=Select(time_option)
        time_dd.select_by_index(4)

                    #pay option
        pay=self.payment_option
        pay.click()

        continue_btn=self.click_continue
        continue_btn.click()














