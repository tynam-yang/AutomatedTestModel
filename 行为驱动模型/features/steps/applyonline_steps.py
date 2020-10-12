# -*- coding: utf-8 -*-

import time
from behave import *


@When('打开访问的网页 "{url}"')
def step_open(context, url):
    context.driver.get(url)
    time.sleep(5)


@Then('进入了技术顾问预约网站成功')
def step_assert_open(context):
    title = context.driver.title
    assert title == "预约技术顾问 - 葡萄城官网"


@When('输入姓名 "{compellation}"、电话 "{telephonenumber}"、邮箱 "{email}"、'
      '公司全称 "{companyname}"、职务 "{duty}"、感兴趣产品 "{pid}"、内容描述 "{otherdemand}" 然后进行预约')
def step_applyonline(context, compellation, telephonenumber, email, companyname, duty, pid, otherdemand):
    time.sleep(1)
    compellation_element = context.driver.find_element_by_name('compellation')
    compellation_element.send_keys(compellation)

    time.sleep(1)
    telephonenumber_element = context.driver.find_element_by_name('telephonenumber')
    telephonenumber_element.send_keys(telephonenumber)

    time.sleep(1)
    email_element = context.driver.find_element_by_name('email')
    email_element.send_keys(email)

    time.sleep(1)
    companyname_element = context.driver.find_element_by_name('companyname')
    companyname_element.send_keys(companyname)

    time.sleep(1)
    duty_element = context.driver.find_element_by_id('duty')
    duty_element.send_keys(duty)

    time.sleep(1)
    pid_element = context.driver.find_element_by_id('pid')
    pid_element.send_keys(pid)

    time.sleep(1)
    otherdemand_element = context.driver.find_element_by_name('otherdemand')
    otherdemand_element.send_keys(otherdemand)

    time.sleep(1)
    submit_btn = context.driver.find_element_by_class_name('gc-btn')
    submit_btn.click()


@Then('技术顾问预约成功')
def step_assert_applyonline(context):
    success_message = context.driver.title
    assert success_message == "感谢预约技术顾问 - 葡萄城官网"
