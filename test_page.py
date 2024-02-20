import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver import ActionChains
from Common_Startup.BaseClass import BaseClass

class TestHomepage(BaseClass):
    def test_menu(self):
        
        self.driver.find_element(By.XPATH,"//a[@class='s1']").click()
        Home_Text = self.driver.find_element(By.XPATH,"span[@class='bold']").text
        assert "Home" in Home_Text
        
        self.driver.find_element(By.XPATH,"//a[@class='s2']").click()
        AboutUs_Text = self.driver.find_element(By.XPATH,"span[@class='bold']").text
        assert "About PAPAMY" in AboutUs_Text
        
        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element(By.LINK_TEXT,"Products")).perform()
        action.move_to_element(self.driver.find_element(By.LINK_TEXT,"Air Conditioners")).click().perform()
        AC_Text = self.driver.find_element(By.XPATH,"span[@class='bold']").text
        assert "Products / Model Range" in AC_Text
        
        action.move_to_element(self.driver.find_element(By.LINK_TEXT,"Products")).perform()
        action.move_to_element(self.driver.find_element(By.LINK_TEXT,"Compressors")).click().perform()
        Compressors_Text = self.driver.find_element(By.XPATH,"span[@class='bold']").text
        assert "Products / Compressor / Rotary Compressor" in Compressors_Text
        
        