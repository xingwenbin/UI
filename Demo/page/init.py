import unittest
from Demo.untils.operationXml import *
from selenium import webdriver

class Init(unittest.TestCase, OperationXml):
    def setUp(self):
        self.driver =webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(self.getXmlData('url'))
        self.driver.implicitly_wait(5)
    def tearDown(self):
        self.driver.quit()
