from collections import OrderedDict

ElementsDetails = \
    {
        # Common to all Elements
        'screenshotsBasePath': 'C:\\Users\\ashish.t\\PycharmProjects\\Appium\\Appium_python\\Assets\\elements-screenshots\\',

        # End of Common Elements

        # Application Level Permission
        'appEnablePermissionPkg': {
            'multipleTimes': False,
            'pkgName': 'com.clearfly.groupfone',
            'pkgClassName': 'android.widget.FrameLayout',
            'imageSubPath': 'appEnablePermission' + '\\',
            'screenshotFileName': '2018-11-15_8-50-24.png',
            'pkgElements': {
                0: {
                    'class': 'android.widget.TextView',
                    'resourceID': 'com.clearfly.groupfone:id/snackbar_text',
                    'text': 'This functionality needs multiple app permissions',
                    'gesture': None,
                    'reaction': None
                },
                1: {
                    'class': 'android.widget.Button',
                    'resourceID': 'com.clearfly.groupfone:id/snackbar_action',
                    'text': 'ENABLE',
                    'gesture': 'tap',
                    'reaction': ''
                }
            }
        },
        'appPermissionsPkg': {
            'multipleTimes': True,
            'pkgName': 'com.android.packageinstaller',
            'pkgClassName': 'com.android.packageinstaller',
            'imageSubPath': 'appEnablePermission' + '\\',
            'screenshotFileName': '2018-11-15_8-51-24.png',
            'pkgElements': {
                0: {
                    'class': 'android.widget.TextView',
                    'resourceID': 'com.android.packageinstaller:id/permission_message',
                    'gesture': None,
                    'reaction': None,
                    'multipleText': {
                        0: 'Allow FoneApp to record audio?',
                        1: 'Allow FoneApp to make and manage phone calls?',
                        2: 'Allow FoneApp to access this device\'s location?'
                    }
                },
                1: {
                    'class': 'android.widget.TextView',
                    'resourceID': 'com.android.packageinstaller:id/current_page_text',
                    'text': '1 of 3',
                    'gesture': None,
                    'reaction': None
                },
                2: {
                    'class': 'android.widget.Button',
                    'resourceID': 'com.android.packageinstaller:id/permission_deny_button',
                    'text': 'DENY',
                    'gesture': None,
                    'reaction': None
                },
                3: {
                    'class': 'android.widget.Button',
                    'resourceID': 'com.android.packageinstaller:id/permission_allow_button',
                    'text': 'ALLOW',
                    'gesture': None,
                    'reaction': None
                }

            }
        },
        'loginNSignUpPkg': {
            'multipleTimes': False,
            'pkgName': 'com.clearfly.groupfone',
            'pkgClassName': 'android.widget.ScrollView',
            'imageSubPath': 'loginNSignUp' + '\\',
            'screenshotFileName': '2018-11-15_8-53-24.png',
            'pkgElements': {
                0: {
                    'class': 'android.widget.TextView',
                    'resourceID': 'com.clearfly.groupfone:id/tvIsdCode',
                    'text': '+1',
                    'gesture': None,
                    'reaction': None
                },
                1: {
                    'class': 'android.widget.EditText',
                    'resourceID': 'com.clearfly.groupfone:id/edtPhoneNumber',
                    'text': 'Phone Number',
                    'gesture': None,
                    'reaction': None
                },
                2: {
                    'class': 'android.widget.TextView',
                    'resourceID': 'com.clearfly.groupfone:id/or_text',
                    'text': 'Or',
                    'gesture': None,
                    'reaction': None
                },
                3: {
                    'class': 'android.widget.EditText',
                    'resourceID': 'com.clearfly.groupfone:id/edtEmail',
                    'text': 'Email',
                    'gesture': None,
                    'reaction': None
                },
                4: {
                    'class': 'android.widget.EditText',
                    'resourceID': 'com.clearfly.groupfone:id/edtPassword',
                    'text': 'Password',
                    'gesture': None,
                    'reaction': None
                },
                5: {
                    'class': 'android.widget.Button',
                    'resourceID': 'com.clearfly.groupfone:id/tvLogin',
                    'text': 'LOGIN',
                    'gesture': None,
                    'reaction': None
                },
                6: {
                    'class': 'android.widget.Button',
                    'resourceID': 'com.clearfly.groupfone:id/tvSignUp',
                    'text': 'SIGN UP',
                    'gesture': None,
                    'reaction': None
                },
                7: {
                    'class': 'android.widget.TextView',
                    'resourceID': 'com.clearfly.groupfone:id/tvForgotPassword',
                    'text': 'Forgot Password?',
                    'gesture': None,
                    'reaction': None
                }
            }

        },
        'agreementPkg': {
            'multipleTimes': False,
            'pkgName': 'com.clearfly.groupfone',
            'pkgClassName': 'android.widget.FrameLayout',
            'imageSubPath': 'loginNSignUp' + '\\',
            'screenshotFileName': '2018-11-15_8-54-24.png',
            'pkgElements': {
                0: {
                    'class': 'android.widget.TextView',
                    'resourceID': None,
                    'text': 'Welcome To',
                    'gesture': None,
                    'reaction': None
                },
                1: {
                    'class': 'android.widget.TextView',
                    'resourceID': 'com.clearfly.groupfone:id/tv_terms_conditions',
                    'text': 'Terms & Conditions',
                    'gesture': None,
                    'reaction': None
                },
                2: {
                    'class': 'android.widget.Button',
                    'resourceID': 'com.clearfly.groupfone:id/btnAgreement',
                    'text': 'I Agree & Continue',
                    'gesture': None,
                    'reaction': None
                }

            }

        }
    }


def fAppModuleExecuter(self, ModuleName, data=None, elementsRID=None):
    def moduleNotFound():
        print "No Module Found named with " + ModuleName
        return False

    func = getattr(self, ModuleName, moduleNotFound)(data, elementsRID)


fAppModules = [
    # Activate Dummy Section
    {'moduleName': 'fAppDummy',
     'simulationData': {'dummyData': 'Nothing Serious'
                        },
     'elmntsRef': ElementsDetails['appEnablePermissionPkg']},

    # Activate SignUp Section
    {'moduleName': 'testSignUp',
     'simulationData': {'firstName': 'Amit',
                        'lastName': 'Pant',
                        'Country': 'India',
                        'Mobile': '9993994107'
                        },
     'elmntsRef': ElementsDetails['appPermissionsPkg']},

    # Activate Login Section
    {'moduleName': 'testLogin',
     'simulationData': {'username': '9999394017',
                        'password': '123456',
                        'email': 'amit@gmail.com',
                        'withEmail': False
                        },
     'elmntsRef': ElementsDetails['appEnablePermissionPkg']}
]

# for fAppModule, data in fAppModules.items():
#     print(type(fAppModule))

elmnt = ElementsDetails['loginNSignUpPkg']['pkgElements'][6]['resourceID']

print(elmnt)

for module in  fAppModules:
    print(module['moduleName'])

# fAppModuleExecuter(fAppModule, data, elements)

# print(ElementsDetails.__getitem__('appEnablePermissionPkg'))
# for m in ElementsDetails['appEnablePermissionPkg'].items():
#     print(m)
