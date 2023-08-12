import gspread as gs

from oauth2client.service_account import ServiceAccountCredentials as SAC


scopes = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

creds = SAC.from_json_keyfile_name('vendor/secrets.json')
client = gs.authorize(credentials=creds)

url = 'https://docs.google.com/spreadsheets/d/1IyPC9y8WbA0AAUuvdXaEfzH0zTG91u8ba_ShZWPcSjY/edit#gid=0'
key = '1IyPC9y8WbA0AAUuvdXaEfzH0zTG91u8ba_ShZWPcSjY'

data = client.open_by_url(url=url)

sheet1 = data.sheet1

print(sheet1.get_all_values())
