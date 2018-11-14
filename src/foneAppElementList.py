fAppelementsDetails = \
    {
        # Common to all Elements
        'screenshotsBasePath': 'C:\\Users\\ashish.t\\PycharmProjects\\Appium\\Appium_python\\Assets\\elements-screenshots\\appPermissions\\',

        # End of Common Elements

        # Application Level Permission
        'appEnablePermission': {
            'multiple': False,
            'pkgName': 'com.clearfly.groupfone',
            'pkgClassName': 'android.widget.FrameLayout',
            'screenshotFileName': 'screenshot-2018-11-14_12.17.26.8.png',
            'pkgElements': {
                0: {
                    'class': 'android.widget.TextView',
                    'resourceID': 'com.clearfly.groupfone:id/snackbar_text',
                    'text': 'This functionality needs multiple app permissions'
                },
                1: {
                    'class': 'android.widget.Button',
                    'resourceID': 'com.clearfly.groupfone:id/snackbar_action',
                    'text': 'ENABLE'
                }
            }
        },
        'appPermissionsPkg': {
            'multiple': True,
            'pkgName': 'com.android.packageinstaller',
            'pkgClassName': 'com.android.packageinstaller',
            'screenshotFileName': 'screenshot-2018-11-14_12.20.23.199.png',
            'pkgElements': {
                0: {
                    'class': 'android.widget.TextView',
                    'resourceID': 'com.android.packageinstaller:id/permission_message',
                    'text': 'Allow FoneApp to record audio?'
                },
                1: {
                    'class': 'android.widget.TextView',
                    'resourceID': 'com.android.packageinstaller:id/current_page_text',
                    'text': '1 of 3'
                },
                2: {
                    'class': 'android.widget.Button',
                    'resourceID': 'com.android.packageinstaller:id/permission_deny_button',
                    'text': 'DENY'
                },
                3: {
                    'class': 'android.widget.Button',
                    'resourceID': 'com.android.packageinstaller:id/permission_allow_button',
                    'text': 'ALLOW'
                }
            }
        },
        'signUpPkg': {
            'multiple': True,
            'pkgName': 'com.android.packageinstaller',
            'pkgClassName': 'com.android.packageinstaller',
            'screenshotFileName': 'screenshot-2018-11-14_12.20.23.199.png',
            'pkgElements':{
            0: {
                'class': 'android.widget.TextView',
                'resourceID':'com.android.packageinstaller:id/permission_message',
                'text': 'Allow FoneApp to record audio?'
              },
            1: {
                'class': 'android.widget.TextView',
                'resourceID':'com.android.packageinstaller:id/current_page_text',
                'text': '1 of 3'
              },

            }
        }
    }
