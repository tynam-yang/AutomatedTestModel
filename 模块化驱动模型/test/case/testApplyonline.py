# -*-coding:utf-8-*-

import time, os
import unittest
from selenium import webdriver
from 模块化驱动模型.utils.ReadConfig import ReadConfig
from 模块化驱动模型.test.pages.applyonlinePage import ApplyonlinePage


class TestApplyonline(unittest.TestCase):
    """测试预约技术顾问"""

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)

    def tearDown(self):
        self.driver.quit()

    def test_applyonline(self):
        """预约技术顾问测试"""
        url = self.get_url()
        self.driver.get(url)
        time.sleep(1)
        applyonline = ApplyonlinePage(self.driver)
        applyonline.applyonline('test', '13888888888', 'test@grapecity.com',
                                      '西安XXXX有限责任公司', '技术爱好者', 'SpreadJS 纯前端表格控件', '学习使用')

    def get_url(self):
        current_path = os.path.abspath((os.path.dirname(__file__)))
        data = ReadConfig().read_json(current_path + "/../../config/base_data.json")
        return data['url']


if __name__ == '__main__':
    unittest.main()
