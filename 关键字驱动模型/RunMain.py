# -*-coding:utf-8-*-

import os
from selenium import webdriver
from 关键字驱动模型.common.ExcelUtil import ExcelUtil
from 关键字驱动模型.action.Action import Action


if __name__ == '__main__':
    excel = 'case/casedata.xlsx'
    a = Action().case_operate(excel=excel, sheet='技术顾问预约')
