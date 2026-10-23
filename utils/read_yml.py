import yaml
from utils.locator_model import LocatorItem


def get_login_locator() -> LocatorItem:
    yaml_file = r'C:\Users\纳\PycharmProjects\pythonProject\playwright-public\data\locator.yml'
    with open(yaml_file,'r', encoding="utf-8") as f:
        data = yaml.safe_load(f)
        login_data = data['login_page']
        # 字典自动解析，校验字段，转成pydantic模型
        locator_model = LocatorItem.model_validate(login_data)
        return locator_model

login_data_file = r"C:\Users\纳\PycharmProjects\pythonProject\playwright-public\data\login_data.yml"
def get_login_data(login_data_file):
    with open(login_data_file,"r",encoding="utf-8") as l_data:
        data = yaml.safe_load(l_data)
        return data