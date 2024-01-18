# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class TestSiteSearchRecrutementvacancies(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('')
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_site_search_recrutementvacancies(self):
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
        driver.find_element(By.LINK_TEXT, "Vacancies").click()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/recruitment/viewJobVacancy")

        # compter le nb de job vacancie dans la page 
        nbjobvancancies = driver.find_elements(By.CLASS_NAME, "oxd-table-card")
        print("Nombre de job vacancies: ", len(nbjobvancancies))

        for elements in nbjobvancancies:
            print (elements)

        # rechercher "automation tester dasn la list"
        #driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div/div[2]/form/div/div/div/div/div[2]/div/div/div[2]/i").click()
        #driver.find_element(By.XPATH, "//body/div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]").click()
        ############################################################
            
        # # Attendre que le menu déroulant soit présent sur la page en utilisant XPath
        # xpath_menu_deroulant = "//div[@class='oxd-select-text-input']"
        # dropdown = WebDriverWait(driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, xpath_menu_deroulant))
        # )

        # # Cliquer sur le menu déroulant pour le faire apparaître
        # dropdown.click()

        # # Sélectionner un élément dans le menu déroulant par son texte visible
        # element_a_selectionner = "Finance Manager"
        # #   xpath_option = f"//div[@class='oxd-select-option' and text()='{element_a_selectionner}']"
        # xpath_option = f"//div[@class='oxd-select-option' and text()='Finance Manager']"
        # A=WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,"//div[@class='oxd-select-option' and text()='Finance Manager']")))
        # A .click() 

        # # Attendre quelques secondes pour voir le résultat (facultatif)
        # driver.implicitly_wait(5)
        
        # By.# Attendre que le menu déroulant soit présent sur la page en utilisant un sélecteur CSS
        css_selector_menu_deroulant = ".oxd-select-text-input"
        dropdown = WebDriverWait(driver, 2).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, css_selector_menu_deroulant))
            )

        # Cliquer sur le menu déroulant pour le faire apparaître
        dropdown.click()
        time.sleep(5)

        # Sélectionner un élément dans le menu déroulant par son texte visible
        element_a_selectionner = "Finance Manager"
        css_selector_option = f".oxd-select-option:contains('{element_a_selectionner}')"
        option = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, css_selector_option))
        )

        # Utiliser ActionChains pour simuler le clic
        action = ActionChains(driver)
        action.move_to_element(option).click().perform()








        ######################################################################
        time.sleep(5)
        dropdown = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//body/div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]")))
        #select = Select(driver.find_element(By.XPATH, "//div[contains(text(),'Automation Test Engineer')]"))         #("//select[@id='rain']"))
        time.sleep(5)
        # Créer un objet Select pour le menu déroulant
        select = Select(dropdown)

        # Sélectionner un élément dans le menu déroulant par son texte visible
        element_a_selectionner = "QA Lead"
        select.select_by_visible_text(element_a_selectionner)

        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(5)


        #driver.find_element(By.XPATH, "//div[@id='app']/div/div/aside/nav/div[2]/ul/li[8]/a/span").click()

        # compter le nb de job vacancie dans la page 
        nbAutomationTester = driver.find_elements(By.CLASS_NAME, "oxd-table-card")
        print("Nombre de tester : ", len(nbAutomationTester))

        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")
        driver.find_element(By.XPATH, "//div[@id='app']/div/div/header/div/div[2]/ul/li/span/i").click()
        driver.find_element(By.LINK_TEXT, "Logout").click()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    
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