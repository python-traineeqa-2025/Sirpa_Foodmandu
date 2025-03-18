import json
import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

class BaseTest:
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')
    logger = logging.getLogger(__name__)

    def setup_method(self, method):  # the name should always be 'setup_method'
        driver_path = r"C:\Users\sirpah\OneDrive - Infinite Computer Solutions (India) Limited\Desktop\QA\QA Automation\Sirpa_Foodmandu\bins\chromedriver.exe"
        ser = Service(driver_path)
        logging.info("set up driver")

        # Set up Chrome options to enable geolocation
        chrome_options = Options()
        chrome_options.add_experimental_option("prefs", {
            "profile.default_content_settings.geolocation": 2
        })

        # Initialize the WebDriver with the options
        self.driver = webdriver.Chrome(service=ser) #,options=chrome_options)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        login_path = r"C:\Users\sirpah\OneDrive - Infinite Computer Solutions (India) Limited\Desktop\QA\QA Automation\Sirpa_Foodmandu\Credentials\login_values.json"
        with open(login_path, "r") as f:
            self.values = json.load(f)

