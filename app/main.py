from app.utils.settings import EnvironmentVar
from app.dataaccess.google_spreadsheets import GoogleSpreadsheets

input_dict = {
    'work_field_name': 'HOUSE_MANAGE_FIELD',
    'spread_sheet_name': '2020/03'
}

google_spreadsheets = GoogleSpreadsheets(environment_var=EnvironmentVar())
gc = google_spreadsheets.gc

spreadsheets_key = google_spreadsheets.get_spreadsheets_key_by_work_field_name(
    work_field_name=input_dict['work_field_name'])

work_field = gc.open_by_key(spreadsheets_key)
work_sheets = work_field.worksheets()

print(work_field.worksheet(input_dict['spread_sheet_name']).title)

for sheet in work_sheets:
    print(sheet.title)
