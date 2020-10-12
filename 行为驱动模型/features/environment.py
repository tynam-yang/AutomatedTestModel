# -*- coding: utf-8 -*-

from selenium import webdriver


def before_feature(context, feature):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()


def after_feature(context, feature):
    context.driver.quit()
