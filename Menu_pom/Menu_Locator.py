from selenium.webdriver.common.by import By

class Menu_locator(object):
    food_item=(By.XPATH,"//a[normalize-space()=\'Pizza\']")
    pizza=(By.XPATH,"//div[@class=\'col-sm-12 col-md-8 col-lg-7 menu__list\']//div[1]//ul[1]//li[1]")