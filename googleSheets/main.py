import gspread
from google.oauth2.service_account import Credentials

scopes = [
    "https://www.googleapis.com/auth/spreadsheets"
] #scopes the the different things that we have access to when we are working with the different files

creds = Credentials.from_service_account_file("credentials.json", scopes=scopes)

client = gspread.authorize(creds)

sheet_id = "1n59xbT1Sl8v5S4dggJ_r9xHrGP8bLVzXwBne_nuP0uU"

sheet = client.open_by_key(sheet_id)
values_list = sheet.sheet1.row_values(2)
# print(values_list)

sheets= map(lambda x: x.title, sheet.worksheets()) #to get only the title of sheets
# print(list(sheets))

sheet1 = sheet.worksheet("TestSheet")
sheet1.update_title("TestSheet") #if we wanna update the title
print(sheet1) #if we want to get a sheet from it's title

sheet1.update_acell("D3","updatedCell")
# if we wanna update a single cell there're two methods of doing this (1) sheet1.update_acell("B3") OR (2)sheet1.update_cell(1,2) this 1,2 refers to the number of column and row

value = sheet1.acell("A3").value #when we want the value of a specific cell
cellFind = sheet1.find("updatedCell") #when we wat to locate a specific cell by it's value
print(cellFind.row , cellFind.col)

sheet1.format("A1:D1",{"textFormat": {"bold": True}})
sheet1.format("A2:A3",{"textFormat": {"bold": False}})
