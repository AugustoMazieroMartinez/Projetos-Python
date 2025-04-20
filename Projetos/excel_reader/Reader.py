import openpyxl as px

wb = px.load_workbook('videogamesales.xlsx')
ws = wb.active
ws = wb['vgsales']

# print('Total number of rows: ' + str(ws.max_row) + "\nTotal number of columns:" + str(ws.max_column))  
print('The value in cell A1 is: ' + str(ws['c1'].value))