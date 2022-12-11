import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

credentials = ServiceAccountCredentials.from_json_keyfile_name('client-secret.json', scope)
client = gspread.authorize(credentials)

spreadsheet = client.open('CSVsheet')

with open('csvnoc.csv', 'r', encoding='utf-8') as file_obj:
    content = file_obj.read()
    client.import_csv(spreadsheet.id, data=content)

    
