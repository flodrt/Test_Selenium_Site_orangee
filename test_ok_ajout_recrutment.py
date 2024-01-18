# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class TestV2Siteorange(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('')
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_v2_siteorange(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        driver.find_element(By.NAME, "username").click()
        driver.find_element(By.NAME, "username").clear()
        driver.find_element(By.NAME, "username").send_keys("Admin")
        driver.find_element(By.NAME, "password").click()
        driver.find_element(By.NAME, "password").clear()
        driver.find_element(By.NAME, "password").send_keys("admin123")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")
        driver.find_element(By.XPATH, "//div[@id='app']/div/div/aside/nav/div[2]/ul/li[5]/a/span").click()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/recruitment/viewCandidates")

        # compter les candidats avant
        list_candidats_before = driver.find_elements(By.CLASS_NAME, "oxd-table-card")
        print("list des employé contient tant de membre ", len(list_candidats_before))

        
        ## ajouter un candidat
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div[2]/div/button").click()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/recruitment/addCandidate")
        driver.find_element(By.NAME, "firstName").click()
        driver.find_element(By.NAME, "firstName").clear()
        driver.find_element(By.NAME, "firstName").send_keys("olivier")
        driver.find_element(By.NAME, "lastName").click()
        driver.find_element(By.NAME, "lastName").clear()
        driver.find_element(By.NAME, "lastName").send_keys("barach")
        
        

        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div/form/div[3]/div/div/div/div[2]/input").click()
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div/form/div[3]/div/div/div/div[2]/input").clear()
  
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div/form/div[3]/div/div/div/div[2]/input").send_keys("olivier@example.com")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        driver.find_element(By.LINK_TEXT, "Leave").click()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/leave/viewLeaveList")
        driver.find_element(By.XPATH, "//div[@id='app']/div/div/aside/nav/div[2]/ul/li[5]/a/span").click()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/recruitment/viewCandidates")

        #extraire le text d'une balise 
        text = driver.find_element(By.XPATH, "//body/div[@id='app']/div[1]/div[1]/aside[1]/nav[1]/div[2]/ul[1]/li[1]/a[1]/span[1]").text
        print (text)

        # compter les candidats apres
        list_candidats_after = driver.find_elements(By.CLASS_NAME, "oxd-table-card")
        print("list des candidats apres ajout contient tant de membre ", len(list_candidats_after))

        #impresion des candidats 
        for candidats in list_candidats_after:
            print( candidats)

        #logout
        driver.find_element(By.XPATH, "//div[@id='app']/div/div/header/div/div[2]/ul/li/span/i").click()
        driver.find_element(By.LINK_TEXT, "Logout").click()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

        

    # # Compte le nombre d'elements selon la pagination (numeros de pages)
    #     total_count_after = 0
    #     while True:

    #         # Enregistrez le contenu de la liste avant l'ajout de l'élément
    #         list_candidats_after = driver.find_elements(By.CLASS_NAME, "oxd-table-card")

    #         count_on_page = len(list_candidats_after)

    #         # Accumuler le total
    #         total_count_after += count_on_page

    #         print(f'Page actuelle: {count_on_page} éléments sur la premiere page | Total jusqu à présent: {total_count_after} éléments')
            
    #         if count_on_page < 50 :
    #             break
    #         else :
    #             next_page_button = self.driver.find_element(By.XPATH, "//button[@class='oxd-pagination-page-item oxd-pagination-page-item--previous-next']")

    #             if 'disabled' in next_page_button.get_attribute('class'):
    #                 # Pas de page suivante, sortie de la boucle
    #                 break

    #             next_page_button.click()
        



        #Comparaison des deux varibles
        print("########################################################################")
        self.assertEqual(len(list_candidats_after), len(list_candidats_before)+1,)

        

    
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
