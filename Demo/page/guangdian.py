from Demo.base.basePage import *
from selenium.webdriver.common.by import By

class GuangDian(WebDriver):
    username_loc = (By.ID, 'userName')
    password_loc = (By.ID, 'password')
    login_loc = (By.ID, 'mysubmit')
    LoginError_loc = (By.CSS_SELECTOR, '.layui-layer-content.layui-layer-padding')
    def typeUserName(self, username):
        self.findElement(*self.username_loc)
        self.findElement(*self.username_loc).send_keys(username)

    def typePassWord(self, password):
        self.findElement(*self.password_loc).send_keys(password)
    @property
    def clickLogin(self):
        self.findElement(*self.login_loc).click()

    def login(self, username, password):
        self.typeUserName(username)
        self.typePassWord(password)
        self.clickLogin

    @property
    def getLoginError(self):
        return self.findElement(*self.LoginError_loc).get_attribute('textContent')