from gspread.models import Spreadsheet
from app.dataaccess.google_spreadsheets import GoogleSpreadsheetsDataAccess


class GSCommandService:
    def __init__(self, gs_data_access: GoogleSpreadsheetsDataAccess):
        self.gs_data_access = gs_data_access

    def run(self, input_dict: dict):
        if input_dict['method_mode'].upper() == 'SELECT_MONTH':
            self.get_house_manage_for_month(month=input_dict['month'])

    def get_house_manage_for_month(self, month: str):
        food = self.gs_data_access.get_range_value(
            sheet=month, start_cell='G5', end_cell='I5')
        miscellaneous = self.gs_data_access.get_range_value(
            sheet=month, start_cell='G6', end_cell='I6')
        eating_out = self.gs_data_access.get_range_value(
            sheet=month, start_cell='G6', end_cell='I7')
        other = self.gs_data_access.get_range_value(
            sheet=month, start_cell='G7', end_cell='I8')
        total = self.gs_data_access.get_cell_by_label(
            sheet=month, label='H10')

        text = f'''
        【{month}の支出を表示】
        -------------------------
        ・食料品
        　　現金    {food[0].value}
        　　クレカ  {food[1].value}
        　　合計    {food[2].value}
        -------------------------
        ・雑費
        　　現金    {miscellaneous[0].value}
        　　クレカ  {miscellaneous[1].value}
        　　合計    {miscellaneous[2].value}
        -------------------------
        ・外食費
        　　現金    {eating_out[0].value}
        　　クレカ  {eating_out[1].value}
        　　合計    {eating_out[2].value}
        -------------------------
        ・その他
        　　現金    {other[0].value}
        　　クレカ  {other[1].value}
        　　合計    {other[2].value}
        -------------------------
        ・合計      {total.value}
        -------------------------
        '''
        print(text)
