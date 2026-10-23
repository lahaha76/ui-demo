import os.path
import pytest
from utils.logger import logging_info
from utils.read_yml import get_login_data

yaml_path = os.path.join(os.path.dirname(os.path.dirname(__file__)),"data","login_data.yml")
yaml_data = get_login_data(yaml_path)
login_cases_data = yaml_data["login_cases"]


case_param_list = []
for case in login_cases_data:
    marks = []
    if "smoke" in case.get("tag",[]):
        marks.append(pytest.mark.smoke)
    case_param_list.append(pytest.param(case,marks=marks))


class TestLogin:
    @pytest.mark.parametrize("case",case_param_list)
    def test_login_cases(self,loginpage,case):
        case_name = case["case_name"]
        username = case["username"]
        password = case["password"]
        expect_url = case["expect_url"]
        expect_msg = case["expect_msg"]
        logging_info.info(f"开始登陆：[{case_name}],用户名:{username},密码:{password}")
        loginpage.login(username,password)


        if expect_url:
            assert loginpage.page.url == expect_url
        else:
            err_msg = loginpage.get_msg()
            assert err_msg == expect_msg



