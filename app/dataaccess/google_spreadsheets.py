import gspread
from oauth2client.service_account import ServiceAccountCredentials
from app.utils.settings import EnvironmentVar
from gspread.models import Spreadsheet


class GoogleSpreadsheetsDataAccess:
    def __init__(self, work_field_name: str):
        self.work_field_name = work_field_name
        self.scope = [
            'https://spreadsheets.google.com/feeds',
            'https://www.googleapis.com/auth/drive'
        ]
        self.credentials = ServiceAccountCredentials.from_json_keyfile_name(
            EnvironmentVar().get_json_key_path(), self.scope)
        self.gc = gspread.authorize(self.credentials)
        self.spreadsheet: Spreadsheet = self.open_spreadsheet()

    def open_spreadsheet(self):
        return self.gc.open_by_key(
            EnvironmentVar().get_environment_var_value(self.work_field_name)
        )

    def get_range_value(self, sheet: str, start_cell: str, end_cell: str) -> list:
        return self.spreadsheet.worksheet(sheet).range(f'{start_cell}:{end_cell}')

    def get_cell_by_label(self, sheet: str, label: str):
        return self.spreadsheet.worksheet(sheet).acell(label)
