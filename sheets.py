import gspread
from gspread.utils import rowcol_to_a1
from oauth2client.service_account import ServiceAccountCredentials


# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
sheet = client.open("NH Python").sheet1
sheet.clear()

# ## SLOW
# for row in range(1, 11):
#     for col in range(1, 11):
#         sheet.update_cell(row, col, row * col)

## FAST
cell_list = sheet.range('A1:J10')
for cell in cell_list:
    cell.value = cell.row * cell.col
sheet.update_cells(cell_list)

# Sum the columns
sum_cells = sheet.range('A12:J12')
for cell in sum_cells:
    formula = f"=SUM({rowcol_to_a1(1, cell.col)},{rowcol_to_a1(10, cell.col)})"
    cell.value = formula
sheet.update_cells(sum_cells, value_input_option='USER_ENTERED')

# Sum the rows
sum_cells = sheet.range('L1:L10')
for cell in sum_cells:
    formula = f"=SUM({rowcol_to_a1(cell.row, 1)},{rowcol_to_a1(cell.row, 10)})"
    cell.value = formula
sheet.update_cells(sum_cells, value_input_option='USER_ENTERED')