__author__ = 'WP8Dev'
import os
import unittest
import time
import waiting
import os
import string
import sys
from collections import OrderedDict

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

# Custom Libraries
import foneapp_module as FAM
import foneAppElementList as fAppElmnts


class FoneAppAutomation():
    foneAppGooglePixel = None
    foneAppGooglePixelDriver = None
    userInput = None

    # Create Device & it's Driver Object
    def __init__(self, pixelConfiguration):

        if pixelConfiguration != None:

            self.foneAppGooglePixel = FAM.FoneAppDevice()

            self.foneAppGooglePixelDriver = self.foneAppGooglePixel.createDriver(pixelConfiguration)

            if self.foneAppGooglePixel.driverExist(self.foneAppGooglePixelDriver):
                print(self.foneAppGooglePixel.prefixEqual("Driver Object is Available"))
            else:
                print(self.foneAppGooglePixel.prefixEqual("Driver NOT Object is Available"))
        else:
            pass

    # Automate User Registration Page
    def testSignUp(self, simulationData, elmntDetails):

        elmntSignUpBtnRID = elmntDetails['pkgElements'][6]['resourceID']

        elmntSignUpBtn = self.uIElementExist(elmntSignUpBtnRID)
        if elmntSignUpBtn != None:
            # Simulate Click on Sign Up
            elmntSignUpBtn.click()


        else:
            print(self.prefixDash('Element ' + elmntSignUpBtnRID + ' Not Present'))
            return

    # Automate Agreement Page
    def testAgreement(self, simulationData, elmntDetails):
        # All Reference ID Decelerations
        elmntTermsNCndtnTxtVwRID = 'com.clearfly.groupfone:id/tv_terms_conditions'
        elmntAgreeBtnVwRID = 'com.clearfly.groupfone:id/btnAgreement'

        elmnTermsNCndtnBtn = self.uIElementExist(elmntTermsNCndtnTxtVwRID)
        if elmnTermsNCndtnBtn != None:
            elmnTermsNCndtnBtn.click()
        else:
            print(self.prefixDash('Element ' + elmntTermsNCndtnTxtVwRID + ' Not Present'))
            return
            # exit(1)

    def testFAppEnablePermissions(self, simulationData, elmntDetails):
        pass


    # Automate User Login Page
    def testLogin(self, simulationData, elmntDetails):
        pass

    # Check Element Existence in User Interface
    def uIElementExist(self, elementResourceID):

        while True:
            try:
                # print(self.foneAppGooglePixelDriver)
                elementRefrence = self.foneAppGooglePixelDriver.find_element_by_id(elementResourceID)
            except NoSuchElementException:
                if self.continueScript(elementResourceID):
                    continue
                else:
                    return None
            else:
                return elementRefrence

    def prefixDash(self, value):
        stringPrefix = '----'
        return stringPrefix + value + stringPrefix

    def continueScript(self, elementResourceID=None):

        if elementResourceID != None:
            print(self.prefixDash('Element ' + elementResourceID + ' Not Present'))
            print("Please Check for Element Existence Manually & continue script accordingly")

            while self.userInput != "y" or self.userInput != "n":
                self.userInput = raw_input("Press 'y' to continue or 'n' to exit Execution: ")
                if self.userInput == 'y':
                    return True
                elif self.userInput == 'n':
                    exit(1)
                else:
                    print("Enter 'y' OR 'n'")
        else:
            print(self.prefixDash('No Element is Passed to Continue Script'))
            return False

    def fAppModuleExecuter(self, ModuleName, simulationData=None, elmntDetails=None):
        def moduleNotFound():
            print "No Module Found named with " + ModuleName
            return False

        func = getattr(self, ModuleName, moduleNotFound)(simulationData, elmntDetails)

    # Dummy Method to Test Class Things
    def fAppDummy(self, simulationData, elmntDetails):
        print('Dummy Test Starting Automation')
        print(simulationData, elmntDetails)

        # Dummy Module
        exit(1)


# ======Automation Section Start======

# Get Driver Object
fAppPixel = FoneAppAutomation({'appPath': 'C:\\Users\\ashish.t\\PycharmProjects\\Appium\\Appium_python\\apk\\',
                              'appName': 'app-release-02112018.apk',
                              'platformName': 'Android',
                              'platformVersion': '7.1.1',
                              'deviceName': '192.168.25.101:5555',
                              'appPackage': 'com.clearfly.groupfone',
                              'appActivity': 'com.clearfly.app.mvp.splash.SplashActivity'
                              })

# List of All Modules with Data to be Executed.
# Note:Just Comment out to Exclude Module
fAppModules = [
    # Activate Dummy Section
    # {'moduleName': 'fAppDummy',
    #  'simulationData': {'dummyData': 'Nothing Serious'
    #                     },
    #  'elmntDetails': fAppElmnts.ElementsDetails['appEnablePermissionPkg']},

    # Activate Enable Permission Section
    # {'moduleName': 'testFAppEnablePermissions',
    #  'simulationData': None,
    #  'elmntDetails': fAppElmnts.ElementsDetails['appEnablePermissionPkg']},

    # Activate SignUp Section
    {'moduleName': 'testSignUp',
     'simulationData': {'firstName': 'Amit',
                        'lastName': 'Pant',
                        'Country': 'India',
                        'Mobile': '9993994107'
                        },
     'elmntDetails': fAppElmnts.ElementsDetails['loginNSignUpPkg']},
    #
    # # Activate Login Section
    # {'moduleName': 'testLogin',
    #  'simulationData': {'username': '9999394017',
    #                     'password': '123456',
    #                     'email': 'amit@gmail.com',
    #                     'withEmail': False
    #                     },
    #  'elmntDetails': fAppElmnts.ElementsDetails['appEnablePermissionPkg']}
]

# Executing All Fone App Modules
for module in fAppModules:
    print(fAppPixel.prefixDash('Automating ' + module['moduleName'] + ' Module'))
    fAppPixel.fAppModuleExecuter(module['moduleName'], module['simulationData'], module['elmntDetails'])
