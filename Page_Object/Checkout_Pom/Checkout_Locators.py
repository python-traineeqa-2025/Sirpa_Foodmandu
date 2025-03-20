from selenium.webdriver.common.by import By


class Checkout_Locators(object):
    checkout_btn=(By.XPATH,"//div[@class='cart__summary']//div//div//button[@class='btn btn-block btn--primary'][normalize-space()='Proceed to Checkout']")

                #address details popup
    enterloc_btn=(By.XPATH,"//input[@id='googleLocation']")
    auto_suggest_item=(By.XPATH,"//div[@class='pac-container pac-logo hdpi']//div[2]")
    confirmLoc_btn=(By.XPATH,"//a[normalize-space()='Confirm this Location']")
    address_title=(By.XPATH,"//input[@placeholder='Enter Title e.g. Home, Office']")
    direction=(By.XPATH,"//textarea[@placeholder='Enter Detail Address Direction']")
    phone=(By.XPATH,"//input[@placeholder='98XXXXXXXX']")
    default_chk=(By.XPATH,"//label[@for='set_default_address']")
    save=(By.XPATH,"//button[normalize-space()='Save']")

                #deliver date and time
    schedule_delivery_btn=(By.XPATH,"//input[@id='delivery_2']")
    date_btn=(By.XPATH,"//select[@class='form-control select select--full-width ng-pristine ng-untouched ng-valid ng-not-empty']")
    time_btn=(By.CSS_SELECTOR,".select-dropdown .select")

                #payment option
    pay_option=(By.XPATH,"//input[@id='2']")

    continue_btn=(By.XPATH,"//button[normalize-space()='Continue']")


