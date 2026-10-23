from playwright.sync_api import Page,sync_playwright
from utils.read_yml import get_login_locator
class LoginPage:
    def __init__(self,page:Page):
        self.page = page
        self.locators = get_login_locator()
        self.username_loc = page.locator(self.locators.username)
        self.password_loc = page.locator(self.locators.password)
        self.submit_loc = page.locator(self.locators.submit)
        self.message_loc = page.locator(self.locators.message)

    def adressurl(self):
        self.page.goto('https://www.saucedemo.com/')

    def login(self,username,password):
        self.username_loc.fill(username)
        self.password_loc.fill(password)
        self.submit_loc.click()
    def get_msg(self):
        return self.message_loc.text_content()





if __name__ == '__main__':
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        loginpage = LoginPage(page)
        loginpage.adressurl()
        browser.close()
