# -*-coding:utf-8-*-

from 关键字驱动模型.common.ExcelUtil import ExcelUtil
from 关键字驱动模型.action.ElementOperation import ElementOperation


class Action:
    def __init__(self):
        self.element = ElementOperation()

    def set_value(self, element, action, parameter=None):
        """
        根据传入的值进行操作
        :param element:
        :param action:
        :param parameter:
        :return:
        """
        if element == "browser":
            return self.element.browser_operate(action, parameter)
        elif element == "time":
            return self.element.time_operate(action, parameter)
        elif element is None or element == "":
            return
        else:  # 如果不是其他的关键字，则默认为定位的元素
            return self.element.element_operate(element, action, parameter)

    def case_operate(self, excel, sheet):
        """
        测试数据运行
        :param excel:
        :param sheet:
        :return:
        """
        all_case = ExcelUtil(excel_path=excel, sheet_name=sheet).get_case()
        for case in all_case:
            self.set_value(case[0], case[1], case[2])


if __name__ == '__main__':
    excel = '../case/casedata.xlsx'
    Action().case_operate(excel=excel, sheet='技术顾问预约')


