from app.dataaccess.google_spreadsheets import GoogleSpreadsheetsDataAccess
from app.data.output_txt import output_select_spending_for_month
from app.data.output_txt import output_message_success
from app.data.output_txt import output_message_error


class GSCommandService:
    def __init__(self, gs_data_access: GoogleSpreadsheetsDataAccess):
        self.gs_data_access = gs_data_access

    def run(self, input_dict: dict):
        if input_dict['method_mode'].upper() == '月の支出':
            self.output_spending_for_month(month=input_dict['month'])
        if input_dict['method_mode'].upper() == 'シート複製':
            self.duplicate_sheet(original=input_dict['copy_original'],
                                       new_sheet_name=input_dict['new_sheet_name'])

    def output_spending_for_month(self, month: str):
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

    def duplicate_sheet(self, original: str, new_sheet_name: str):
        try:
            self.gs_data_access.duplicate_sheet(
                original=original, new_sheet_name=new_sheet_name)
            output_message_success(
                message=f'シート【 {new_sheet_name} 】を作成しました。')
        except Exception as e:
            output_message_error(message=e.args[0]['message'])
