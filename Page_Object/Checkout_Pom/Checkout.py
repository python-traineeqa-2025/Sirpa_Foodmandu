from selenium.common import NoSuchElementException
import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Page_Object.Checkout_Pom.Checkout_prop import Checkout_Prop
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
        address.send_keys("Hattisar")

        auto_item=self.auto_suggest
        auto_item.click()

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

        time.sleep(2)

        time_option=self.select_time
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(time_option)
        )
        #time_option.click()
        try:
            time_dd=Select(time_option)
            time_dd.select_by_index(2)

        except NoSuchElementException:
            time_dd = Select(time_option)
            time_dd.select_by_index(2)

        time.sleep(2)
                    #pay option
        pay=self.payment_option
        pay.click()

        time.sleep(2)
        continue_btn=self.click_continue
        continue_btn.click()

        time.sleep(2)














