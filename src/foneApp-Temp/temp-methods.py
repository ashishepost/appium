import sys
sys.path.append('C:\\Users\\ashish.t\\PycharmProjects\\Appium\\Appium_python\\src\\')

import foneAppElementList as fAppElmnts


# Get Source Page Element
def sourcePageElmnt(sourcePage, actionElmntIndex, subPage=None):
    # Check if UI is Process based or Not

    if fAppElmnts.ElementsDetails[sourcePage]['isProcess']:
        if isinstance(fAppElmnts.ElementsDetails[sourcePage]['UIPages'], list):
            return max(fAppElmnts.ElementsDetails[sourcePage]['UIPages'])[subPage]['UIElements'][actionElmntIndex]['resourceID']
    else:
        if isinstance(fAppElmnts.ElementsDetails[sourcePage]['UIElements'], dict):
            return fAppElmnts.ElementsDetails[sourcePage]['UIElements'][actionElmntIndex]['resourceID']

def complementElmnt(module, actionElmntIndex=None):
    # Check if UI is Process based or Not
    # print(type(module['isProcess']))
    if module['isProcess']:
        if isinstance(module['UIPages'], list):
            print( module['UIPages'][1])
    # else:
    #     if isinstance(fAppElmnts.ElementsDetails[sourcePage]['UIElements'], dict):
    #         return fAppElmnts.ElementsDetails[sourcePage]['UIElements'][actionElmntIndex]['resourceID']


# print(sourcePageElmnt(fAppElmnts.ElementsDetails['signUpModule']['sourcePage'],fAppElmnts.ElementsDetails['signUpModule']['actionElmntIndex'], 'agreementPageElmnts'))
complementElmnt(fAppElmnts.ElementsDetails['signUpModule'])




# print(fAppElmnts.ElementsDetails)
