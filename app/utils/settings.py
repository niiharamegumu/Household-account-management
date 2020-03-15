import os
from dotenv import load_dotenv

PROJECT_DIR_NAME = 'household-account-management'


class EnvironmentVar:
    def __init__(self):
        self.root_path = self.generate_root_path()
        self.env_path = os.path.join(self.root_path, '.env')

    def generate_root_path(self):
        current_dir = os.path.abspath('./')
        split_list = current_dir.split(PROJECT_DIR_NAME)
        root_path = os.path.join(split_list[0], PROJECT_DIR_NAME)
        return root_path

    def get_json_key_path(self) -> str:
        load_dotenv(self.env_path)
        env_value = os.environ.get('JSON_KEY_PATH')
        return os.path.join(self.root_path, env_value)

    def get_environment_var_value(self, var_name: str) -> str:
        load_dotenv(self.env_path)
        return os.environ.get(var_name)
