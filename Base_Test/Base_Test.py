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

        values_path = r"C:\Users\sirpah\OneDrive - Infinite Computer Solutions (India) Limited\Desktop\QA\QA Automation\Sirpa_Foodmandu\Values\login_values.json"
        with open(values_path, "r") as f:
            self.values = json.load(f)