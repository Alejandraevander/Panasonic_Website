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
        log = self.getLogger()
        #Clicking Home Button & Checking whether correct or not
        self.driver.find_element(By.XPATH,"//a[@class='s1']").click()
        Home_Text = self.driver.find_element(By.XPATH,"//span[@class='bold']").text
        Home_URL = self.driver.current_url
        log.info("Home URL : " + Home_URL )
        assert "HOME" in Home_Text
        
        #Clicking About Us Button & Checking whether correct or not
        self.driver.find_element(By.XPATH,"//a[@class='s2']").click()
        AboutUs_Text = self.driver.find_element(By.XPATH,"//span[@class='bold']").text
        AboutUs_URL = self.driver.current_url
        log.info("About Us URL : " + AboutUs_URL )
        assert "About PAPAMY" in AboutUs_Text
        
        #Clicking Product -> AC Button & Checking whether correct or not
        self.driver.find_element(By.XPATH,"//a[@class='s3']").click()
        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element(By.XPATH,"//a[@href='modelrange.asp']")).click().perform()
        AC_Text = self.driver.find_element(By.XPATH,"//span[@class='bold']").text
        AC_URL =  self.driver.current_url
        log.info("AC URL : " + AC_URL )
        assert "Products / Model Range" in AC_Text
        
        #Clicking Product -> Compressor & Checking whether correct or not
        self.driver.find_element(By.XPATH,"//a[@class='s3']").click()
        action.move_to_element(self.driver.find_element(By.XPATH,"//a[@href='compressor.asp']")).click().perform()
        Compressors_Text = self.driver.find_element(By.XPATH,"//span[@class='bold']").text
        Compressors_URL = self.driver.current_url
        log.info("Compressors URL : " + Compressors_URL)
        assert "Products / Compressor / Rotary Compressor" in Compressors_Text
        
        #Clicking Support Button & Checking whether correct or not
        self.driver.find_element(By.XPATH,"//a[@class='s4']").click()
        Support_Text = self.driver.find_element(By.XPATH,"//span[@class='bold']").text
        Support_URL = self.driver.current_url
        log.info("Support URL : " + Support_URL)
        assert "Support" in Support_Text
        
        #Clicking E-Learning Button & Checking whether correct or not
        self.driver.find_element(By.XPATH,"//a[@class='s5']").click()
        ELearning_Text = self.driver.find_element(By.XPATH,"//span[@class='bold']").text
        ELearning_URL = self.driver.current_url
        log.info("ELearning URL : " + ELearning_URL)
        assert "E-Learning" in ELearning_Text
        
        #Clicking E-Vendor Button & Checking whether correct or not
        self.driver.find_element(By.XPATH,"//a[@class='s6']").click()
        EVendor_Text = self.driver.find_element(By.XPATH,"//span[@class='bold']").text
        EVendor_URL = self.driver.current_url
        log.info("EVendor URL : " + EVendor_URL)
        assert "E-Vendor" in EVendor_Text
        
        #Clicking Contact Us Button & Checking whether correct or not
        self.driver.find_element(By.XPATH,"//a[@class='s7']").click()
        ContactUs_Text = self.driver.find_element(By.XPATH,"//span[@class='bold']").text
        ContactUs_URL = self.driver.current_url
        log.info("Contact Us URL : " + ContactUs_URL)
        assert "Contact Us" in ContactUs_Text
    
    def test_BeginLibrary(self):
        log = self.getLogger()
        self.driver.find_element(By.CLASS_NAME,"Pan_CI").click()
        
        #Switching to new window
        windows_opened = self.driver.window_handles
        self.driver.switch_to.window(windows_opened[1])
        Global_URL =  self.driver.current_url
        log.info("Global URL : " + Global_URL)
        self.driver.close()
        
        #Switching back to previous window
        self.driver.switch_to.window(windows_opened[0])
        Main_Window_URL = self.driver.current_url
        log.info("Main Window URL : " + Main_Window_URL)
        
        
        ### Bug 1
        # self.driver.find_element(By.LINK_TEXT, "Home").click()
        
        # try:
        #     #Switching to new window
        #     windows_opened = self.driver.window_handles
        #     self.driver.switch_to.window(windows_opened[1])
        #     Home_URL =  self.driver.current_url
        #     log.info("Home URL : " + Home_URL)
        #     self.driver.close()
        # except Exception as e:
        #     log.info("Error Code :" + str(e) )
        #     pass
        
        # #Switching back to previous window
        # self.driver.switch_to.window(windows_opened[0])
        # Main_Window_URL = self.driver.current_url
        # log.info("Main Window URL : " + Main_Window_URL)
            
    
        self.driver.find_element(By.LINK_TEXT, "Sign In").click()
        
        #Switching to new window
        windows_opened = self.driver.window_handles
        self.driver.switch_to.window(windows_opened[1])
        SignIn_URL =  self.driver.current_url
        log.info("SignIn URL : " + SignIn_URL)
        self.driver.close()
        
        #Switching back to previous window
        self.driver.switch_to.window(windows_opened[0])
        Main_Window_URL = self.driver.current_url
        log.info("Main Window URL : " + Main_Window_URL)