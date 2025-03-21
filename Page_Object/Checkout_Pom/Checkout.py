from selenium.common import NoSuchElementException
import time
import logging

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Page_Object.Checkout_Pom.Checkout_prop import Checkout_Prop
from selenium.webdriver.support.select import Select


class Checkout(Checkout_Prop):

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def checkout_page(self,locH,location_title,phonenumber):

        checkout=self.go_checkout
        checkout.click()

                            #address details pop up
        address=self.input_address
        address.click()
        address.send_keys(locH)

        time.sleep(2)
        auto_item=self.auto_suggest
        auto_item.click()

        time.sleep(3)
        confirm_address=self.confirm_location
        confirm_address.click()

        time.sleep(1)
        title=self.address_title
        title.click()
        title.send_keys(location_title)

        direction_details=self.input_direction
        direction_details.click()
        direction_details.send_keys(locH)

        phone_number=self.input_phone
        phone_number.click()
        phone_number.send_keys(phonenumber)

        default_address=self.set_default_address
        default_address.click()

        save_button=self.click_save
        save_button.click()

        time.sleep(3)

                        #Delivery Date and Time
        self.driver.execute_script('scrollBy(0, 300)')
        schedule=self.schedule_delivery
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(schedule)
        )
        schedule.click()

        time.sleep(2)
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

        self.driver.execute_script('scrollBy(0, 310)')
        time.sleep(2)
                    #pay option
        pay=self.payment_option
        pay.click()

        time.sleep(2)
        continue_btn=self.click_continue
        continue_btn.click()

        time.sleep(3)


    def Neg_checkout_page(self,Neg_loc):

        bag_button = self.go_neg_checkout
        bag_button.click()

        bag_item_list=self.click_bag_item
        bag_item_list.click()

        proceed=self.go_neg_proceed
        proceed.click()

        cross=self.click_cross
        cross.click()

        delete=self.confirm_delete
        delete.click()

                            #address details pop up

        neg_address=self.input_address
        neg_address.click()
        neg_address.send_keys(Neg_loc)

        time.sleep(3)

        confirm_address=self.confirm_location
        confirm_address.click()

        error=self.display_error
        logging.info(error.text)

        time.sleep(3)















