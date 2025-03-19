from selenium.webdriver.common.by import By


class Cart_Locators(object):
    fav=(By.XPATH,"//button[@class='btn btn--fav mt-2 spinner']")
    desc_box=(By.XPATH,"//textarea[@placeholder='Add Notes']")
    add=(By.XPATH,"//span[@class='icomoon icon-add icomoon--green']")
    minus=(By.XPATH,"//span[@class='icomoon icon-remove icomoon--green']")
    bag=(By.XPATH,"//button[@class='btn btn--primary btn-block btn--add-to-cart']")