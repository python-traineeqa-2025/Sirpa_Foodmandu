from selenium.webdriver.common.by import By

class Location_Locator(object):
    change = (By.XPATH, "//span[text()=\'Change\']")
    confirm = (By.XPATH, "//a[text()=\'Confirm this Location\']")
    done = (By.XPATH, "//label[text()=\'Done\']")


# location=self.driver.find_element(By.XPATH,"//span[text()=\'Change\']")
#         location.click()
#         time.sleep(3)
#
#         confirm=self.driver.find_element(By.XPATH,"//a[text()=\'Confirm this Location\']")
#         confirm.click()
#
#         done=self.driver.find_element(By.XPATH,"//label[text()=\'Done\']")
#         done.click()