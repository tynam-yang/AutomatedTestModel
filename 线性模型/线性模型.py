# -*-coding: utf-8-*-·

import time
from selenium import webdriver


# 启动浏览器
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)

# 访问 URL
driver.get('https://www.grapecity.com.cn/applyonline')
time.sleep(1)

# 填写内容
driver.find_element_by_name('compellation').send_keys('test')
time.sleep(1)
driver.find_element_by_name('telephonenumber').send_keys('13888888888')
time.sleep(1)
driver.find_element_by_name('email').send_keys('test@grapecity.com')
time.sleep(1)
driver.find_element_by_name('companyname').send_keys('西安XXXX有限责任公司')
time.sleep(1)
driver.find_element_by_id('duty').send_keys('技术爱好者')
time.sleep(1)
driver.find_element_by_id('pid').send_keys('SpreadJS 纯前端表格控件')
time.sleep(1)
driver.find_element_by_name('otherdemand').send_keys('学习使用')
# 提交
driver.find_element_by_class_name('gc-btn').submit()

time.sleep(10)

# 关闭浏览器
driver.quit()
