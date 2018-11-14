import inspect
from collections import OrderedDict


# userInput = None
#
# while userInput != "y" or userInput != "n":
#     userInput = raw_input("Press 'y' to continue or 'n' to exit")
#     if userInput == 'y':
#
#         continue
#     elif userInput == 'n':
#         exit(1)
#     else:
#         print("Enter only 'y' OR 'n'")

class checkClass():
    member = 10

    def classMethodOne(self):
        print(inspect.stack()[0][3])

    def classMethodTwo(self):
        print(inspect.stack()[0][3])


checkObj = checkClass()
checkObj.classMethodOne()

fAppModules = OrderedDict([
    # Activate Dummy Section
    ('fAppDummy', {'dummyData': 'Amit'
                   }),

    # Activate SignUp Section
    ('testSignUp', {'firstName': 'Amit',
                    'lastName': 'Pant',
                    'Country': 'India',
                    'Mobile': '9993994107'
                    }),

    # Activate Login Section
    # ('testLogin', {'username': '9999394017',
    #               'password': '123456',
    #               'email': 'amit@gmail.com',
    #               'withEmail': False
    #               })

])
# fAppModules = {# Activate Dummy Section
#                'fAppDummy': {'dummyData': 'Amit'
#                                    },
#
#                # Activate SignUp Section
#                'testSignUp': {'firstName': 'Amit',
#                               'lastName': 'Pant',
#                               'Country': 'India',
#                               'Mobile': '9993994107'
#                               },
#
#                # Activate Login Section
#                # 'testLogin': {'username': '9999394017',
#                #               'password': '123456',
#                #               'email': 'amit@gmail.com',
#                #               'withEmail': False
#                #               }
#
#                }




for key, value in fAppModules.items():
	print(value)
