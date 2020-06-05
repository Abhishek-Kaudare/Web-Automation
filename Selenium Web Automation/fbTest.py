from selenium import webdriver
from  selenium.webdriver.common.action_chains import ActionChains
from  selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys


import time

import unittest

class LoginTest(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Chrome('E:/Software/chromedriver')
        self.driver.get("https://www.facebook.com/")
        self.driver.maximize_window()

    def test_login(self):

        driver = self.driver
        fbUsername = 'xxxxxxx'
        fbPassword = 'xxxxxxx'

        emailFieldID        = 'email'
        passFieldID         = 'pass'
        loginButtonXpath    = '//input[@value="Log In"]'
        fbLogoXpath         = '(//a[contains(@href, "logo")])[1]'
        logoutButtonXpath   = "//li[@class='_54ni navSubmenu _6398 _64kz __MenuItem']"
        fbNavLabelXpath     = "//div[contains(@id,'userNavigationLabel')]"
        lastXpath           = "//span[@class='_54nh'][contains(.,'Log Out')]"

        emailFieldElement   = WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id(emailFieldID))
        passFieldElement    = WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id(passFieldID))
        loginButtonElement  = WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_xpath(loginButtonXpath))
        emailFieldElement.clear()
        emailFieldElement.send_keys(fbUsername)
        passFieldElement.clear()
        passFieldElement.send_keys(fbPassword)
        loginButtonElement.click()

        elem = WebDriverWait(driver, 2).until(lambda driver: driver.find_element_by_xpath(fbLogoXpath))
        elem.send_keys(Keys.ESCAPE)

        fbNavLabelElement = WebDriverWait(driver, 2).until(lambda driver: driver.find_element_by_xpath(fbNavLabelXpath))
        fbNavLabelElement.click()
        logoutButtonElement = WebDriverWait(driver, 2).until(lambda driver: driver.find_element_by_xpath(logoutButtonXpath))
        logoutButtonElement.click()


        def tearDown(self):
            self.driver.quit()

    if __name__ == "__main__":
        unittest.main()

