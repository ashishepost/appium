# fAppModules = ['testSignUp',
#                'testLogin']

fAppModules = {'testSignUp': {'firstName': 'Amit',
                              'lastName': 'Pant',
                              'Country': 'India',
                              'Mobile': '9993994107'
                              },
               'testLogin': {'username': '9999394017',
                             'password': '123456',
                             'email': 'amit@gmail.com',
                             'withEmail': False
                             }

               }

for fAppModule in fAppModules:
    print fAppModules[fAppModule]


