import allure
import pytest
from playwright.sync_api import Page

from pages.login_page import LoginPage


# 钩子：捕获用例执行结果挂载到item上，共fixture读取
@pytest.hookimpl(tryfirst=True,hookwrapper=True)
def pytest_runtest_makereport(item,call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item,"rep_"+rep.when,rep)

@pytest.fixture(scope="function")
def loginpage(page:Page,request):
    lp = LoginPage(page)
    #lp.adressurl()
    lp.page.goto("https://www.saucedemo.com/")
    yield lp

    # 后置：用例执行完后判断是否失败，失败截图
    if request.node.rep_call.failed:
        img = page.screenshot(full_page=True)
        allure.attach(img,name="失败截图",attachment_type=allure.attachment_type.PNG)


