__author__ = 'WP8Dev'
import os
import unittest
import time
import waiting

from appium import webdriver
''' ScrollTest.com by Promode '''
''' This Test Case Just Click on the Refresh Button My Application '''  
''' Just Click and Verify it in you Phone '''
''' Copyright 2015 '''


class ContactAppTestAppium(unittest.TestCase):

    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '7.1.1'
        desired_caps['deviceName'] = 'ZY322BQKG5'
        desired_caps['app'] = 'D:\Appium_Python\Appium_python\\apk\\Cfone.apk'
        desired_caps['appPackage'] = 'com.clearfly.groupfone'
        desired_caps['appActivity'] = 'com.clearfly.app.mvp.splash.SplashActivity'

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        time.sleep(6)
    def test_clicklogin(self):
            
        for x in range(0,3):
            
            self.driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click()
            
         # Login Module
        time.sleep(6)
        self.driver.find_element_by_id("com.clearfly.groupfone:id/tvIsdCode").click() 
        self.driver.find_element_by_id("com.clearfly.groupfone:id/country_name").click() 
        self.driver.find_element_by_id("com.clearfly.groupfone:id/edtPhoneNumber").send_keys("8800467267") 
        self.driver.find_element_by_id("com.clearfly.groupfone:id/edtPassword").send_keys("1")
        loginButton = self.driver.find_element_by_id("com.clearfly.groupfone:id/tvLogin")
        self.assertTrue(loginButton.is_displayed())
        loginButton.click()
        time.sleep(10)
        self.driver.find_element_by_id("com.clearfly.groupfone:id/cellView").click()