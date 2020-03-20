from app.dataaccess.google_spreadsheets import GoogleSpreadsheetsDataAccess
from app.service.gs_command import GSCommandService

input_dict = {
    'month': '2020/05',
    'method_mode': 'シート複製',
    'copy_original': 'template',
    'new_sheet_name': '2020/05'
}

gs_data_access = GoogleSpreadsheetsDataAccess(work_field_name='HOUSE_MANAGE_FIELD')
gs_command_service = GSCommandService(gs_data_access=gs_data_access)

gs_command_service.run(input_dict=input_dict)
