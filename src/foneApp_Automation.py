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

            # Check if Enable Permission Snackbar Present
            elmntEnablePermissionBtn = self.uIElementExist(fAppElmnts.ElementsDetails['appEnablePermissionPkg']['pkgElements'][1]['resourceID'])
            if elmntEnablePermissionBtn != None:
                elmntEnablePermissionBtn.click()
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
    # Get Source Page Element
    def sourcePageElmnt(sourcePage, actionElmntIndex, subPage=None):
    # Check if UI is Process based or Not

        if fAppElmnts.ElementsDetails[sourcePage]['isProcess']:
            if isinstance(fAppElmnts.ElementsDetails[sourcePage]['UIPages'], list):
                return max(fAppElmnts.ElementsDetails[sourcePage]['UIPages'])[subPage]['UIElements'][actionElmntIndex]['resourceID']
        else:
            if isinstance(fAppElmnts.ElementsDetails[sourcePage]['UIElements'], dict):
                return fAppElmnts.ElementsDetails[sourcePage]['UIElements'][actionElmntIndex]['resourceID']

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
    # {'testName': 'testDummyModule',
    #  'simulationData': {'dummyData': 'Nothing Serious'
    #                     },
    #  'moduleDetails': fAppElmnts.ElementsDetails['dummyModule']},

    # Activate Enable Permission
    # {'testName': 'testAppEnablePermissionDialog',
    #  'simulationData': None,
    #  'moduleDetails': fAppElmnts.ElementsDetails['appEnablePermissionDialog']},

    # Enable Application Permissions
    # {'testName': 'testAppGrantPermissionDialogs',
    #  'simulationData': None,
    #  'moduleDetails': fAppElmnts.ElementsDetails['appGrantPermissionDialogs']},

    # Activate SignUp
    {'testName': 'testSignUpModule',
     'simulationData': {'firstName': 'Amit',
                        'lastName': 'Pant',
                        'Country': 'India',
                        'Mobile': '9993994107'
                        },
     'moduleDetails': fAppElmnts.ElementsDetails['signUpModule']},

    # Activate Login
    # {'moduleName': 'testLoginModule',
    #  'simulationData': {'username': '9999394017',
    #                     'password': '123456',
    #                     'email': 'amit@gmail.com',
    #                     'withEmail': False
    #                     },
    #  'moduleDetails': fAppElmnts.ElementsDetails['loginModule']}
]

# Executing All FoneApp Application Tests
for module in fAppModules:
    print(fAppPixel.prefixDash('Automating ' + module['testName'] + ' Module'))
    fAppPixel.fAppModuleExecuter(module['testName'], module['simulationData'], module['moduleDetails'])
