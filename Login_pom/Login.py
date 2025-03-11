class login():
    def loginpage(self):

        driver = webdriver.Chrome()

        driver.get("https://foodmandu.com/Account/Login")
        driver.find_element(By.NAME,'Email').send_keys('example@practice.com')
        driver.find_element(By.NAME,'Password').send_keys('12345678')
        driver.find_element(By.CSS_SELECTOR, 'input[type=\"checkbox\"] + label').click()
        driver.find_element(By.CSS_SELECTOR, '.btn-block').click()


        time.sleep(5)

findbyname= login()
findbyname.loginpage()