import sys
# sys.path.append('..')
import unittest
from Demo.page.wenzhangPage import *
from Demo.page.guangdian import *
from Demo.page.init import *
from Demo.untils import function


# from unittest import TestCase

class gdCMStest(Init, GuangDian, Wenzhangguanli):
    ''' 新增文章 '''
    # def test_article(self):
    #     self.login('nigaoren', '123456')
    #     self.article('11111', '索易科技', '山西索易', 'admin','221')




    """ 文章管理查询 """
    def test_check(self):
        self.login('nigaoren', '123456')
        self.checkArticle('今天星期二 ，上街买毛衣')
        time.sleep(2)
        articles = self.findElement(By.XPATH, '//*[@id="tabList"]/tbody/tr[1]/td[2]').text
        self.assertEqual(articles, '今天星期二 ，上街买毛衣')
        function.insert_img(self.driver, 'articles_check.png')


if __name__ == 'main':
    unittest.main(verbosity=2)
