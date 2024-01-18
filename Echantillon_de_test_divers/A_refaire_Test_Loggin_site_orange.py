# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class TestLoggin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_loggin(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        driver.find_element(By.NAME,"username").click()
        #driver.find_element(By.XPATH,"//input[@class='oxd-input oxd-input--active']").click()
        driver.find_element(By.NAME,"username").clear()
        #driver.find_element(By.XPATH,"//input[@class='oxd-input oxd-input--active']").send_keys("Admin")
        driver.find_element(By.NAME,"password").click()
        #driver.find_element(By.XPATH,"//div[@class='oxd-form-row'][2]/div[@class='oxd-input-group oxd-input-field-bottom-space'][1]/div[2]/input[@class='oxd-input oxd-input--active']").click()
        driver.find_element(By.NAME,"password").clear()
        #driver.find_element(By.XPATH,"//div[@class='oxd-form-row'][2]/div[@class='oxd-input-group oxd-input-field-bottom-space'][1]/div[2]/input[@class='oxd-input oxd-input--active']").send_keys("admin123")
        #driver.find_element(By.XPATH,"//button[@type='submit']").click()
        # driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")
        # driver.find_element(By.XPATH,"//div[@id='app']/div/div/aside/nav/div[2]/ul/li/a/span").click()
        # driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers")
        # driver.find_element(By.XPATH,"//div[@id='app']/div/div/header/div/div[2]/ul/li/span/i").click()
        # driver.find_element(By.LINK_TEXT,"Logout").click()
        # driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        # driver.find_element(By.XPATH,"//div[@id='app']/div/div/div/div/div[2]").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
