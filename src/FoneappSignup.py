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
   

   ## Registration Module
        SignupButton = self.driver.find_element_by_id("com.clearfly.groupfone:id/tvSignUp")
        self.assertTrue(SignupButton.is_displayed())
        SignupButton.click() 
        self.driver.find_element_by_id("com.clearfly.groupfone:id/btnAgreement").click() 
        self.driver.find_element_by_id("com.clearfly.groupfone:id/edt_phone_number").send_keys("9810266175")
        self.driver.find_element_by_id("com.clearfly.groupfone:id/tvDone").click() 
        self.driver.find_element_by_id("com.clearfly.groupfone:id/yes_btn").click()
        time.sleep(15)
        self.driver.find_element_by_id("com.clearfly.groupfone:id/edtVerificationField").send_keys("914652")
        time.sleep(10)
        self.driver.find_element_by_id("com.clearfly.groupfone:id/btnOk").click()

        ##Profilesetup
        time.sleep(5)
        self.driver.find_element_by_id("com.clearfly.groupfone:id/edtFirstName").send_keys("Office")
        self.driver.hide_keyboard()
        self.driver.find_element_by_id("com.clearfly.groupfone:id/edtLastName").send_keys("MtoG")
        self.driver.hide_keyboard()
        self.driver.find_element_by_id("com.clearfly.groupfone:id/edtEmail").send_keys("officemoto@gmail.com")
        self.driver.hide_keyboard()
        self.driver.find_element_by_id("com.clearfly.groupfone:id/edtPassword").send_keys("123")
        self.driver.hide_keyboard()
        self.driver.find_element_by_id("com.clearfly.groupfone:id/edtVerifyPassword").send_keys("123")
        self.driver.hide_keyboard()
        self.driver.find_element_by_id("com.clearfly.groupfone:id/btnActionBar").click()
         

        ## Right now we are just verify the displayed message on the Phone
        ## You can right code to handle that toast message and Verify that message


    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(ContactAppTestAppium)
    unittest.TextTestRunner(verbosity=2).run(suite)


