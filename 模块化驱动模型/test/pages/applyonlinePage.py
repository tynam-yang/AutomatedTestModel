# -*-coding:utf-8-*-

import time
from selenium import webdriver
from selenium.webdriver.support.select import Select


class ApplyonlinePage:
    """预约技术顾问页面"""
    def __init__(self, driver):
        self.driver = driver

    def applyonline_element(self):
        """预约技术顾问页面元素"""
        self.compellation = self.driver.find_element_by_name('compellation')
        self.telephonenumber = self.driver.find_element_by_name('telephonenumber')
        self.email = self.driver.find_element_by_name('email')
        self.companyname = self.driver.find_element_by_name('companyname')
        self.duty = self.driver.find_element_by_id('duty')
        self.pid = self.driver.find_element_by_id('pid')
        self.otherdemand = self.driver.find_element_by_name('otherdemand')
        self.submit_btn = self.driver.find_element_by_class_name('gc-btn')

    def applyonline(self, compellation, telephonenumber, email, companyname, duty, pid, otherdemand):
        """预约技术顾问"""
        self.applyonline_element()
        self.compellation.send_keys(compellation)
        time.sleep(1)
        self.telephonenumber.send_keys(telephonenumber)
        time.sleep(1)
        self.email.send_keys(email)
        time.sleep(1)
        self.companyname.send_keys(companyname)
        time.sleep(1)
        self.duty.send_keys(duty)
        time.sleep(1)
        self.pid.send_keys(pid)
        time.sleep(1)
        self.otherdemand.send_keys(otherdemand)
        time.sleep(1)
        self.submit_btn.submit()
