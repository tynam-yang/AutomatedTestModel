# -*-coding:utf-8-*-

"""
Created on 2020-10-1
Project: GrapecityTest
@Author: Tynam
"""

import os, time, unittest
from 数据驱动模型.common.HwTestReport import HTMLTestReport


class RunMain:
    def get_all_case(self):
        """导入所有的用例"""
        case_path = os.getcwd()
        discover = unittest.defaultTestLoader.discover(case_path,
                                                       pattern="Test*.py")
        print(discover)
        return discover

    def set_report(self, all_case, report_path=None):
        """设置测试报告"""
        if report_path is None:
            current_path = os.path.abspath(os.path.dirname(__file__))
            report_path = current_path + '/report/'
        else:
            report_path = report_path

        # 获取当前时间
        now = time.strftime('%Y{y}%m{m}%d{d}%H{h}%M{M}%S{s}').format(y="年", m="月", d="日", h="时", M="分", s="秒")
        # 标题
        title = u"葡萄城技术顾问预约测试"
        # 设置报告存放路径和命名
        report_abspath = os.path.join(report_path, title + now + ".html")
        # 测试报告写入
        with open(report_abspath, 'wb') as report:
            runner = HTMLTestReport(stream=report,
                                    verbosity=2,
                                    images=True,
                                    title=title,
                                    tester='Tynam')
            runner.run(all_case)

    def run_case(self, report_path=None):
        all_case = self.get_all_case()
        self.set_report(all_case, report_path)


if __name__ == "__main__":
    RunMain().run_case()




