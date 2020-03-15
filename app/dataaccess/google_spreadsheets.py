import gspread
from oauth2client.service_account import ServiceAccountCredentials
from app.utils.settings import EnvironmentVar


class GoogleSpreadsheets:
    def __init__(self, environment_var: EnvironmentVar):
        self.environment_var = environment_var
        self.scope = [
            'https://spreadsheets.google.com/feeds',
            'https://www.googleapis.com/auth/drive'
        ]
        self.credentials = ServiceAccountCredentials.from_json_keyfile_name(
            self.environment_var.get_json_key_path(), self.scope)
        self.gc = gspread.authorize(self.credentials)

    def get_spreadsheets_key_by_work_field_name(
            self, work_field_name: str):
        return self.environment_var.get_environment_var_value(work_field_name)
