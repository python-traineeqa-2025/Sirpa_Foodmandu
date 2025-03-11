import json
import logging

from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class BaseTest:
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')
    logger = logging.getLogger(__name__)

    def setup_method(self, method): #the name should always be 'setup_method'
        driver_path = r"C:\Users\sirpah\OneDrive - Infinite Computer Solutions (India) Limited\Desktop\QA\QA Automation\Sirpa_Foodmandu\bins\chromedriver.exe"
        ser = Service(driver_path)
        logging.info("set up driver")
        driver = webdriver.Chrome(service=ser)
        self.driver=driver
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        # creds_path = r"C:\Users\sirpah\OneDrive - Infinite Computer Solutions (India) Limited\Desktop\QA\QA Automation\SirpaAutomation\cred\creds.json"
        # with open(creds_path, "r") as f:
        #     # x=json.load(f)
        #     self.creds = json.load(f)