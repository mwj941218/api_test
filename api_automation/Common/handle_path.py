"""
测试用例路径
测试数据路径
输出报告路径、日志路径
配置文件路径
"""
import os

# 主路径:其中os.path.abspath(__file__)获取的是当前文件的绝对路径，外出包上dirname获取出来的是当前目录的上级目录
#  此时BaseDir获取到的目录是：D:\py_word\api_automation，也就是整个包的顶层目录
BaseDir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

cases_dir = os.path.join(BaseDir, "TestCases")
datas_dir = os.path.join(BaseDir, "TestDatas")
reports_dir = os.path.join(BaseDir, "OutPuts\\Reports")

logs_dir = os.path.join(BaseDir, "OutPuts\\Logs")
conf_dir = os.path.join(BaseDir, "Conf")