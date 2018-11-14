__author__ = 'WP8Dev'
import os
import unittest
import time
import waiting
import os
import string
import pyperclip
from appium import webdriver

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

class FoneAppDevice():
    driver = None
    def createDriver(self, appConfiguration):
        desired_caps = {}
        desired_caps['platformName'] = appConfiguration['platformName']
        desired_caps['platformVersion'] = appConfiguration['platformVersion']
        desired_caps['deviceName'] = appConfiguration['deviceName']
        # 'D:\Appium_Python\Appium_python\\apk\\Cfone.apk'
        desired_caps['app'] = self.getApkPath(appConfiguration['appPath']) + appConfiguration['appName']
        desired_caps['appPackage'] = appConfiguration['appPackage']
        desired_caps[
            'appActivity'] = appConfiguration['appActivity']

        self.driver = webdriver.Remote(
            'http://127.0.0.1:4723/wd/hub', desired_caps)
        return self.driver

    #Start Fone App Test Section
    def driverExist(self, driver):

        if not driver:
            self.driver = None
            return False
        else:
            return True

    def prefixEqual(self, value):
        stringPrefix = '=================='
        return stringPrefix + value + stringPrefix

    def getApkPath(self, script_path):
        #print(script_path)
        script_path_splitted = script_path.split('\\')
        #print(script_path_splitted)
        # script_path_splitted.length
        Apk_Path = ""
        for x in range(0,  len(script_path_splitted) - 1):
            Apk_Path = Apk_Path + script_path_splitted[x] + "\\"
            #print(Apk_Path)

        return Apk_Path


    def tearDown(self):
        pass
        # self.driver.quit()



# if __name__ == '__main__':
#     pass
#     # suite = unittest.TestLoader().loadTestsFromTestCase(ContactAppTestAppium)
#     # unittest.TextTestRunner(verbosity=2).run(suite)
#     # unittest.main()


