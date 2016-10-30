import gspread
from oauth2client.service_account import ServiceAccountCredentials
from api_modules import DataBaseManager

scope = ['https://spreadsheets.google.com/feeds']
credentials = ServiceAccountCredentials.from_json_keyfile_name('spreadsheet_modules/secret.json', scope)
gc = gspread.authorize(credentials)
wks = gc.open("FinalProjectPython").sheet1


def get_all_users():
    connection = DataBaseManager.DataBaseManager.connect()
    try:
        with connection.cursor() as cursor:
            query = "SELECT * FROM `user`"
            cursor.execute(query)
            result = cursor.fetchall()
    finally:
        connection.close()

    return result

users = get_all_users()
final_fields = ['fullname', 'enterprise', 'state']

key = 1

for field in final_fields:
    wks.update_cell(1, key, field)
    key += 1

key = 2
for user in users:
    user['fullname'] = user['firstname'] + " " + user['lastname']
    del (user['firstname'], user['lastname'])
    value = 1
    for field in final_fields:
        if field in user:
            wks.update_cell(key, value, user[field])
            value += 1

    key += 1