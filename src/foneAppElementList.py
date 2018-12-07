ElementsDetails = \
    {
        # ========= Common to all Modules =========

        # Root Path to Screenshots Folder
        'screenshotsBasePath': 'C:\\Users\\ashish.t\\PycharmProjects\\Appium\\Appium_python\\Assets\\elements-screenshots\\',

        # Dummy Module which has implemented jot to test connectivity
        'dummyModule': {'dummyData': 'Dummy Data no Use',
                        'isProcess': False,
                        'UIElements': {
                            0: {
                                'dataColumn': 'Dummy Data'

                            }
                        }
                        },
        # ========= End of Common to all Modules =========

        # Application Level Permission
        'appEnablePermissionModule': {
            'isProcess': False,
            'multipleTimes': False,
            'pkgName': 'com.clearfly.groupfone',
            'pkgClassName': 'android.widget.FrameLayout',
            'imageSubPath': 'appEnablePermission' + '\\',
            'screenshotFileName': '2018-11-15_8-50-24.png',
            'UIElements': {
                0: {
                    'class': 'android.widget.TextView',
                    'resourceID': 'com.clearfly.groupfone:id/snackbar_text',
                    'text': 'This functionality needs multiple app permissions',
                    'gesture': None,
                    'reaction': None,
                    'dataColumn': None
                },
                1: {
                    'class': 'android.widget.Button',
                    'resourceID': 'com.clearfly.groupfone:id/snackbar_action',
                    'text': 'ENABLE',
                    'gesture': 'tap',
                    'reaction': '',
                    'dataColumn': None
                }
            }
        },
        'appGrantPermissionDialogsModule': {
            'isProcess': False,
            'multipleTimes': True,
            'pkgName': 'com.android.packageinstaller',
            'pkgClassName': 'com.android.packageinstaller',
            'imageSubPath': 'appEnablePermission' + '\\',
            'screenshotFileName': '2018-11-15_8-51-24.png',
            'UIElements': {
                0: {
                    'class': 'android.widget.TextView',
                    'resourceID': 'com.android.packageinstaller:id/permission_message',
                    'gesture': None,
                    'reaction': None,
                    'multipleText': {
                        0: 'Allow FoneApp to record audio?',
                        1: 'Allow FoneApp to make and manage phone calls?',
                        2: 'Allow FoneApp to access this device\'s location?'
                    },
                    'dataColumn': None
                },
                1: {
                    'class': 'android.widget.TextView',
                    'resourceID': 'com.android.packageinstaller:id/current_page_text',
                    'text': '1 of 3',
                    'gesture': None,
                    'reaction': None,
                    'dataColumn': None
                },
                2: {
                    'class': 'android.widget.Button',
                    'resourceID': 'com.android.packageinstaller:id/permission_deny_button',
                    'text': 'DENY',
                    'gesture': None,
                    'reaction': None,
                    'dataColumn': None
                },
                3: {
                    'class': 'android.widget.Button',
                    'resourceID': 'com.android.packageinstaller:id/permission_allow_button',
                    'text': 'ALLOW',
                    'gesture': None,
                    'reaction': None,
                    'dataColumn': None
                }

            }
        },

        # Sign Process UI Page Elements Details
        'loginModule': {
            'isProcess': False,
            'pkgName': 'com.clearfly.groupfone',
            'pkgClassName': 'android.widget.ScrollView',
            'sourcePage': 'appModule',
            'actionElmntIndex': None,
            'imageSubPath': 'loginModule' + '\\',
            'screenshotFileName': '2018-11-15_8-53-24.png',
            'simulationData': 'loginData',
            'UIElements': {
                0: {
                    'class': 'android.widget.TextView',
                    'resourceID': 'com.clearfly.groupfone:id/tvIsdCode',
                    'text': '+1',
                    'gesture': 'tap',
                    'reaction': 'select-text',
                    'dataColumn': 'tvIsdCode'
                },
                1: {
                    'class': 'android.widget.EditText',
                    'resourceID': 'com.clearfly.groupfone:id/edtPhoneNumber',
                    'text': 'Phone Number',
                    'gesture': 'tap',
                    'reaction': 'edit-text',
                    'dataColumn': 'edtPhoneNumber'
                },
                2: {
                    'class': 'android.widget.TextView',
                    'resourceID': 'com.clearfly.groupfone:id/or_text',
                    'text': 'Or',
                    'gesture': None,
                    'reaction': None,
                    'dataColumn': 'or_text'
                },
                3: {
                    'class': 'android.widget.EditText',
                    'resourceID': 'com.clearfly.groupfone:id/edtEmail',
                    'text': 'Email',
                    'gesture': 'tap',
                    'reaction': 'edit-text',
                    'dataColumn': 'edtEmail'
                },
                4: {
                    'class': 'android.widget.EditText',
                    'resourceID': 'com.clearfly.groupfone:id/edtPassword',
                    'text': 'Password',
                    'gesture': 'tap',
                    'reaction': 'edit-text',
                    'dataColumn': 'edtPassword'
                },
                5: {
                    'class': 'android.widget.Button',
                    'resourceID': 'com.clearfly.groupfone:id/tvLogin',
                    'text': 'LOGIN',
                    'gesture': 'tap',
                    'reaction': 'new-page',
                    'dataColumn': None
                },
                6: {
                    'class': 'android.widget.Button',
                    'resourceID': 'com.clearfly.groupfone:id/tvSignUp',
                    'text': 'SIGN UP',
                    'gesture': 'tap',
                    'reaction': 'new-process',
                    'dataColumn': None
                },
                7: {
                    'class': 'android.widget.TextView',
                    'resourceID': 'com.clearfly.groupfone:id/tvForgotPassword',
                    'text': 'Forgot Password?',
                    'gesture': 'tap',
                    'reaction': 'new-process',
                    'dataColumn': None
                }
            }
        },

        # Sign-Up Process UI Pages Elements Details
        'signUpModule': {
            'isProcess': True,
            'sourcePage': 'loginModule',
            'actionElmntIndex': 6,
            'imageSubPath': 'signUpModule' + '\\',
            'screenshotFileName': None,
            'simulationData': 'signupData',
            'UIPages': [
                {
                    'agreementPageElmnts': {
                        'pkgName': 'com.clearfly.groupfone',
                        'pkgClassName': 'android.widget.FrameLayout',
                        'screenshotFileName': '2018-11-15_8-54-24.png',
                        'UIElements': {
                            0: {
                                'class': 'android.widget.TextView',
                                'resourceID': None,
                                'text': 'Welcome To',
                                'gesture': None,
                                'reaction': None,
                                'dataColumn': "testagg1"
                            },
                            1: {
                                'class': 'android.widget.TextView',
                                'resourceID': 'com.clearfly.groupfone:id/tv_terms_conditions',
                                'text': 'Terms & Conditions',
                                'gesture': None,
                                'reaction': None,
                                'dataColumn': "testagg2"
                            },
                            2: {
                                'class': 'android.widget.Button',
                                'resourceID': 'com.clearfly.groupfone:id/btnAgreement',
                                'text': 'I Agree & Continue',
                                'gesture': None,
                                'reaction': None,
                                'dataColumn': None
                            }

                        }

                    }
                }, {
                    'registerPageElmnts': {
                        'pkgName': 'com.clearfly.groupfone',
                        'pkgClassName': 'android.widget.FrameLayout',
                        'screenshotFileName': '2018-11-15_8-54-24.png',
                        'UIElements': {
                            0: {
                                'class': 'android.widget.TextView',
                                'resourceID': None,
                                'text': 'Welcome To',
                                'gesture': None,
                                'reaction': None,
                                'dataColumn': 'testregist1'
                            },
                            1: {
                                'class': 'android.widget.TextView',
                                'resourceID': 'com.clearfly.groupfone:id/tv_terms_conditions',
                                'text': 'Terms & Conditions',
                                'gesture': None,
                                'reaction': None,
                                'dataColumn': 'testregist2'},
                            2: {
                                'class': 'android.widget.Button',
                                'resourceID': 'com.clearfly.groupfone:id/btnAgreement',
                                'text': 'I Agree & Continue',
                                'gesture': None,
                                'reaction': None,
                                'dataColumn': None
                            },
                            3: {
                                'class': 'android.widget.TextView',
                                'resourceID': 'com.clearfly.groupfone:id/tv_terms_conditions',
                                'text': 'Terms & Conditions',
                                'gesture': None,
                                'reaction': None,
                                'dataColumn': 'testregist3'},

                        }

                    }
                },
                {
                    'noPageElmnts': {
                        'pkgName': 'com.clearfly.groupfone',
                        'pkgClassName': 'android.widget.FrameLayout',
                        'screenshotFileName': '2018-11-15_8-54-24.png',
                        'UIElements': {
                            0: {
                                'class': 'android.widget.TextView',
                                'resourceID': None,
                                'text': 'Welcome To',
                                'gesture': None,
                                'reaction': None,
                                'dataColumn': 'testregist1'
                            },
                            1: {
                                'class': 'android.widget.TextView',
                                'resourceID': 'com.clearfly.groupfone:id/tv_terms_conditions',
                                'text': 'Terms & Conditions',
                                'gesture': None,
                                'reaction': None,
                                'dataColumn': 'testregist2'},
                            2: {
                                'class': 'android.widget.Button',
                                'resourceID': 'com.clearfly.groupfone:id/btnAgreement',
                                'text': 'I Agree & Continue',
                                'gesture': None,
                                'reaction': None,
                                'dataColumn': None
                            },
                            3: {
                                'class': 'android.widget.TextView',
                                'resourceID': 'com.clearfly.groupfone:id/tv_terms_conditions',
                                'text': 'Terms & Conditions',
                                'gesture': None,
                                'reaction': None,
                                'dataColumn': 'testregist3'},

                        }

                    }
                }
            ]

        }

    }
