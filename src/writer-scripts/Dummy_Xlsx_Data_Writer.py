import sys
import xlsxwriter

# Append src folder to system Path
sys.path.append('C:\\Users\\ashish.t\\PycharmProjects\\Appium\\Appium_python\\src\\')

# Now we can Import foneAppElementList
import foneAppElementList as fAppElmnts
import simulationData as simData


# End of Import Section


class xlsxTemplateWriter():
    # File Handle
    workbook = None
    allErrorCodes = {
        'substringNotFound': -1
    }

    def __init__(self, workbookName):
        self.workbook = xlsxwriter.Workbook(workbookName)

    # Get Source Page Element
    def headerWriter(self, allElements):
        # Check if UI is Process based or Not

        for worksheetName in allElements.keys():

            # Create Worksheets for all Modules
            if worksheetName.find('Module') != self.allErrorCodes['substringNotFound']:
                try:
                    # Length for Worksheet Name Must be <=31
                    worksheet = self.workbook.add_worksheet(worksheetName[:31])

                    # only Process Based UI Pages
                    if allElements[worksheetName]['isProcess']:
                        # print(allElements[worksheetName])
                        headingRow = 0
                        headingColmn = 0
                        subHeadingRow = 1
                        subHeadingcolmn = 0
                        for page in allElements[worksheetName]['UIPages']:
                            try:
                                for elements in page.keys():
                                    try:
                                        # Write Heading
                                        worksheet.write(headingRow, headingColmn, elements)

                                        for element in page[elements]['UIElements'].keys():

                                            colmnSubHeaderName = page[elements]['UIElements'][element]['dataColumn']
                                            if colmnSubHeaderName != None:
                                                # Write Sub Headings
                                                subHeadingcolmn += 1
                                                worksheet.write(subHeadingRow, subHeadingcolmn, colmnSubHeaderName)

                                        headingColmn = subHeadingcolmn + 1
                                        subHeadingcolmn += 1

                                    except KeyError as error:
                                        self.errorDisplay(
                                            'No Key ' + str(error) + ' in ' + worksheetName + ' Please check Manually')
                                        continue
                            except KeyError as error:
                                self.errorDisplay(
                                    'No Key ' + str(error) + ' in ' + worksheetName + ' Please check Manually')
                                continue
                    else:
                        # print(allElements[worksheetName])
                        row = 0
                        column = 0
                        for element in allElements[worksheetName]['UIElements'].keys():
                            try:
                                colmnHeaderName = allElements[worksheetName]['UIElements'][element]['dataColumn']
                                if colmnHeaderName != None:
                                    worksheet.write(row, column, colmnHeaderName)
                                    column += 1
                            except KeyError as error:
                                self.errorDisplay(
                                    'No Key ' + str(error) + ' in ' + worksheetName + ' Please check Manually')
                                continue

                except xlsxwriter.exceptions.InvalidWorksheetName:
                    print('Worksheet Name must be <=31')

    # Display Error Messages of Whole System
    def errorDisplay(self, message):
        print(message)


# ================== End of Section Start ==================

# ================== Main Section Start ==================
template = xlsxTemplateWriter(simData.simulationData['outputSourceBasePath'] + simData.simulationData['outputFilename'])

# Write Template File
template.headerWriter(fAppElmnts.ElementsDetails)

# ================== Main Section Ends ==================


# ================== Clean-Up Process Start ==================
# Save & Close Workbook
template.workbook.close()

# Delete Template Object
del template

# ================== Clean-Up Process Ends ==================
