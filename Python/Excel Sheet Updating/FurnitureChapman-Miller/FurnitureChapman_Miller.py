#nicholas chapman-miller

import openpyxl
from datetime import date

#Furniture excel file needs to be in project folder for this to work
wb = openpyxl.load_workbook("Furniture.xlsx")

#select worksheet with furniture prices
ws = wb["Furniture"]


#dictionary with updated table prices
priceUpdates = {
    "E": 84.00,
    "D": 184.00,
    "A": 80.40
    }


#loop through spreadsheet, row 1 = headings
for row in range(2, ws.max_row + 1):

    #column E (5) = table type
    tableType = ws.cell(row=row, column=5).value

    #column F (6) = price per table
    if tableType in priceUpdates:

        #update price using dictionary
        ws.cell(row=row, column=6).value = priceUpdates[tableType]

#find last row to put date
lastRow = ws.max_row

#add current date to bottom
ws.cell(row=lastRow + 2, column=1).value = "Last Revision Date: "
ws.cell(row=lastRow + 2, column=2).value = date.today()

#format date
ws.cell(row=lastRow + 2, column= 2).number_format = "mm/dd/yyyy"


#save updated spreadsheet with a new name   
wb.save("updatedFurniture.xlsx")

#display msg when the program finishes
print("Furniture spreadsheet successfully updated !!")
print("Saved as updatedFurniture.xlsx")

input("Press Enter to close the program...")
