import unittest
# import os

from BeautifulReport import BeautifulReport
from Common.handle_path import cases_dir, reports_dir

# 收集用例，abspath当前目录
# cases_dir = os.path.dirname(os.path.abspath(__file__))
s = unittest.TestLoader().discover(cases_dir)

# 生成报告
br = BeautifulReport(s)
br.report("yidab-登录自动化", "report.html", reports_dir)