import pytest
import time
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver import ActionChains
from Common_Startup.BaseClass import BaseClass

class TestHomepage(BaseClass):
    def test_menu(self):
        
        #Clicking Home Button & Checking whether correct or not
        self.driver.find_element(By.XPATH,"//a[@class='s1']").click()
        Home_Text = self.driver.find_element(By.XPATH,"//span[@class='bold']").text
        #print(Home_Text)
        assert "HOME" in Home_Text
        
        #Clicking About Us Button & Checking whether correct or not
        self.driver.find_element(By.XPATH,"//a[@class='s2']").click()
        AboutUs_Text = self.driver.find_element(By.XPATH,"//span[@class='bold']").text
        assert "About PAPAMY" in AboutUs_Text
        
        #Clicking Product -> AC Button & Checking whether correct or not
        self.driver.find_element(By.XPATH,"//a[@class='s3']").click()
        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element(By.XPATH,"//a[@href='modelrange.asp']")).click().perform()
        AC_Text = self.driver.find_element(By.XPATH,"//span[@class='bold']").text
        assert "Products / Model Range" in AC_Text
        
        #Clicking Product -> Compressor & Checking whether correct or not
        self.driver.find_element(By.XPATH,"//a[@class='s3']").click()
        action.move_to_element(self.driver.find_element(By.XPATH,"//a[@href='compressor.asp']")).click().perform()
        Compressors_Text = self.driver.find_element(By.XPATH,"//span[@class='bold']").text
        assert "Products / Compressor / Rotary Compressor" in Compressors_Text
        
        