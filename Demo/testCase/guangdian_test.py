import unittest
from Demo.page.guangdian import *
from selenium import webdriver
import time as t
from Demo.untils import function
from Demo.page.init import *
class gdLogin(Init, GuangDian):

    def test_gdlogin_001(self, parent='divText', value='passwordNull'):
        self.login('nigaoren', '')
        self.assertEqual(self.getLoginError, self.getXmlUser(parent, value))
        function.insert_img(self.driver, 'user_pawd_empty.png')

    def test_gdlogin_002(self, parent='divText', value='nameNull'):

        self.login('', '123456')
        self.assertEqual(self.getLoginError, self.getXmlUser(parent, value))
        function.insert_img(self.driver, 'user_empty.png')

    def test_gdlogin_003(self, parent='divText', value='nameNull'):
        self.login('', '')
        self.assertEqual(self.getLoginError, self.getXmlUser(parent, value))
        function.insert_img(self.driver, 'user_password_empty.png')

if __name__ == 'main':
    unittest.main(verbosity=2)