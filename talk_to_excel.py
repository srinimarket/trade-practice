# Talk to excel
wb = xw.Book("data_with_excel.xlsx")

# Talk to sheet
sht_1 = wb.sheets['Sheet1']
sht_2 = wb.sheets['Sheet2']

# Write to any cell
sht_1.range('A1').value = 'Start Algo Trade'
sht_2.range('A1').value = 'Stop Algo Trade'

# Read from any cell
data = sht_1.range('E1').value