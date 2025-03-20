from selenium.webdriver.common.by import By
import logging

class Search_Locators(object):
    bar=(By.XPATH,"//input[@placeholder=\'Restaurant or Cuisine (leave it blank to browse all)\']")
    search_button=(By.XPATH,"//button[@class=\'btn btn--primary btn-lg btn-block\']")
    logging.info("Select location")
    search_location=(By.CSS_SELECTOR,"input[placeholder=\'Search Location\']")

