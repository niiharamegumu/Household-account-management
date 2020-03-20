from app.dataaccess.google_spreadsheets import GoogleSpreadsheetsDataAccess
from app.data.output_txt import output_select_spending_for_month


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

        output_select_spending_for_month(
            month=month, food=food, miscellaneous=miscellaneous,
            eating_out=eating_out, other=other, total=total)
