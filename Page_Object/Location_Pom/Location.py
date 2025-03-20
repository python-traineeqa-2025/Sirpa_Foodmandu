from Page_Object.Location_Pom.Location_prop import Location_prop
import time

class Location(Location_prop):

    def __init__(self, driver):
        self.driver = driver

    def location(self):

        change_btn=self.select_change
        change_btn.click()
        time.sleep(2)

        confirm_btn=self.select_confirm
        confirm_btn.click()
        time.sleep(1)

        done_btn=self.select_done
        done_btn.click()