# -*-coding:utf-8-*-

import time
import unittest
from ddt import ddt, data, unpack
from selenium import webdriver
from 数据驱动模型.common.ExcelUtil import ExcelUtil


class Case(object):

    def __init__(self):
        pass

    def get_case(self):
        """
        获取数据
        得到有用的数据，并且使数据以邮箱地址、密码、预期结果定位、预期结果的顺序返回
        """

        # 获取 Excel 中的文件数据
        sheet = 'applyonline'
        file = ExcelUtil(sheet_name=sheet)
        data = file.get_data()

        # 得到所需要数据的索引，然后根据索引获取相应顺序的数据
        compellation_index = data[0].index("姓名")
        telephonenumber_index = data[0].index("电话")
        email_index = data[0].index("邮箱")
        companyname_index = data[0].index("公司全称")
        duty_index = data[0].index("职务")
        pid_index = data[0].index("感兴趣产品")
        otherdemand_index = data[0].index("需求描述")
        submit_btn_index = data[0].index("提交预约")
        expected_index = data[0].index("预期结果")

        all_case = []
        # 去除header行，和其他无用的数据
        for i in range(1, len(data)):
            case = []
            case.append(data[i][compellation_index])
            case.append(data[i][telephonenumber_index])
            case.append(data[i][email_index])
            case.append(data[i][companyname_index])
            case.append(data[i][duty_index])
            case.append(data[i][pid_index])
            case.append(data[i][otherdemand_index])
            case.append(data[i][submit_btn_index])
            case.append(data[i][expected_index])
            all_case.append(case)
        return all_case


class Applyonline(object):

    def __init__(self, driver):
        self.driver = driver

    def applyonline(self, compellation, telephonenumber, email, companyname, duty, pid, otherdemand, submit):
        """预约技术顾问步骤"""
        if compellation:
            self.driver.find_element_by_name('compellation').send_keys(compellation)
        if telephonenumber:
            self.driver.find_element_by_name('telephonenumber').send_keys(telephonenumber)
        if email:
            self.driver.find_element_by_name('email').send_keys(email)
        if companyname:
            self.driver.find_element_by_name('companyname').send_keys(companyname)
        if duty:
            self.driver.find_element_by_id('duty').send_keys(duty)
        if pid:
            self.driver.find_element_by_id('pid').send_keys(pid)
        if otherdemand:
            self.driver.find_element_by_name('otherdemand').send_keys(otherdemand)
        if submit:
           self.driver.find_element_by_class_name('gc-btn').submit()

    def applyonline_assert(self, assert_message):
        """预约技术顾问操作断言"""
        time.sleep(1)
        if assert_message == '提交成功':
            assert_title = self.driver.title
            assert assert_title == '感谢预约技术顾问 - 葡萄城官网'
        elif assert_message:
            assert_elements = self.driver.find_elements_by_class_name('signuplabelerror')
            time.sleep(1)
            for assert_element in assert_elements:
                if assert_element.is_displayed() and assert_element.text == assert_message:
                    assert True
                    return
            # 默认使用 class='signuplabelerror' 进行断言，如果位找到则认为断言失败
            assert False
        else:
            return
@ddt
class TestApplyonline(unittest.TestCase):
    """测试预约技术顾问"""

    def setUp(self):
        self.driver = webdriver.Chrome()
        url = "https://www.grapecity.com.cn/applyonline/"
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get(url=url)

    def tearDown(self):
        self.driver.quit()

    case = Case().get_case()

    @data(*case)
    @unpack
    def test_applyonline(self, compellation, telephonenumber, email, companyname, duty, pid, otherdemand,
                         submit, assert_message):
        applyonline = Applyonline(driver=self.driver)
        applyonline.applyonline(compellation, telephonenumber, email, companyname, duty, pid, otherdemand, submit)
        applyonline.applyonline_assert(assert_message)


if __name__ == '__main__':
    unittest.main()
