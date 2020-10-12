# -*-coding:utf-8-*-

import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class ElementOperation:
    def __init__(self, browser="chrome"):
        self.driver = StartBrowser().browser_start(browser)

    def browser_operate(self, action, parameter=None):
        return Browser(self.driver).browser_operate(action, parameter)

    def element_operate(self, local, action, parameter=None):
        return Element(self.driver).element_operate(local, action, parameter)

    def time_operate(self, action, parameter=None):
        return Time().time_operate(action, parameter)



class Element:
    def __init__(self, driver):
        self.driver = driver

    def __find_element(self, local):
        """
        默认使用css定位，如果需要其他定位使用：分割，例如：id：password
        :param by:
        :return:
        """
        if ":" in local:
            [by, element] = local.split(":")
            return self.__element_find(by, element)
        else:
            return self.__element_find("css", local)


    def __element_find(self, by, element):
        """
        定位元素
        :param by:
        :param element:
        :return:
        """
        if by == "id":
            return self.driver.find_element(By.ID, element)
        elif by == "class":
            return self.driver.find_element(By.CLASS_NAME, element)
        elif by == "name":
            return self.driver.find_element(By.NAME, element)
        elif by == "tag":
            return self.driver.find_element(By.TAG_NAME, element)
        elif by == "link":
            return self.driver.find_element(By.LINK_TEXT, element)
        elif by == "xpath":
            return self.driver.find_element(By.PARTIAL_LINK_TEXT, element)
        elif by == "css":
            return self.driver.find_element(By.CSS_SELECTOR, element)
        else:
            return

    def element_operate(self, local, action, parameter=None):
        """
        元素操作
        :param element:
        :param action:
        :param parameter:
        :return:
        """
        element = self.__find_element(local)
        if action == "input" and parameter:
            element.send_keys(parameter)
        elif action == "click":
            element.click()
        elif action == "assert":
            element_text = element.text
            assert element_text == parameter
        else:
            return


class StartBrowser:
    def __init__(self):
        pass

    def browser_start(self, browser="chrome"):
        """
        浏览器启动
        :param browser:
        :return:
        """
        driver = ''
        if browser == "chrome":
            driver = webdriver.Chrome()
        elif browser == "firefox":
            driver = webdriver.Firefox()
        else:
            print("浏览器操作关键字参数传入错误")
        return driver


class Browser:
    def __init__(self, driver):
        self.driver = driver

    def browser_operate(self, action, parameter=None):
        """
        浏览器操作
        :param action:
        :param parameter:
        :return:
        """
        try:
            if action == "open" and parameter:
                self.driver.get(parameter)
            elif action == "max":
                self.driver.maximize_window()
            elif action == "close":
                self.driver.close()
            elif action == "quit":
                self.driver.quit()
        except Exception :
            print("浏览器操作关键字传入错误")


class Time:
    def __init__(self):
        pass

    def time_operate(self, action, parameter=None):
        """
        时间操作
        :param action:
        :param parameter:
        :return:
        """
        if action == "sleep" and parameter:
            return time.sleep(parameter)
        else:
            return "时间操作关键字传入错误"