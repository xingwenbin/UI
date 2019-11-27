from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time as t


class WebDriver(object):
    def __init__(self, driver):
        self.driver = driver

    def findElement(self, *loc):
        ''' 单个定位元素的方法'''
        try:
            # print(self.driver.find_element(*loc), '*'*10)
            return self.driver.find_element(*loc)
        except NoSuchElementException as e:
            print('Error Details {0}'.format(e.args[0]))

    def findsElements(self, *loc):
        ''' 单个定位元素的方法'''
        try:
            return self.driver.find_element(*loc)
        except NoSuchElementException as e:
            print('Error Details {0}'.format(e.args[0]))
    def switch_to_frame(self, *loc):
        '''  表格切换  '''
        try:
            return self.driver.switch_to.frame(*loc)
        except NoSuchElementException as e:
            print('Error Details {0}'.format(e.args[0]))

    def execute_script(self, *loc):
        try:
            return self.driver.execute_script(*loc)
        except NoSuchElementException as e:
            print('Error Details {0}'.format(e.args[0]))