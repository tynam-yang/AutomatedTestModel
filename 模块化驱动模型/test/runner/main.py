# -*-coding:utf-8-*-

import os, time
import unittest
from 模块化驱动模型.utils.HwTestReport import HTMLTestReport


class Main:
    def get_all_case(self):
        """导入所有的用例"""
        current_path = os.path.abspath(os.path.dirname(__file__))
        case_path = current_path + '/../case/'
        discover = unittest.defaultTestLoader.discover(case_path, pattern="test*.py")
        print(discover)
        return discover

    def set_report(self, all_case, report_path=None):
        """设置测试报告"""
        if report_path is None:
            current_path = os.path.abspath(os.path.dirname(__file__))
            report_path = current_path + '/../../report/'
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


if __name__ == '__main__':
    Main().run_case()
