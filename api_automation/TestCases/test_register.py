
import unittest

import requests

from Common.myddt import ddt,data
from Common.handle_excel import HandleExcel
from Common.handle_requests import send_requests
from Common.handle_path import datas_dir
from Common.handle_logging import logger
from Common.handle_db import select_db
from Common.mobile_file import get_new_phone
from Common.handle_data import replace_mark_with_data



# 实例化表获取表单数据类，传入文件路径名称和表单名称
he = HandleExcel(datas_dir+"\\api_case.xlsx","yidab_login")
# 获取到所有数据后存储至cases变量中
cases = he.read_all_datas()
he.close_file()
# 继承testcase类，引入ddt数据驱动
@ddt
class TestRegister(unittest.TestCase):
    @data(*cases) # cases拆包传递所有数据，case参数接收每一条测试数据zl
    def test_register_ok(self, case):
        """
        利用ddt数据驱动，传递每一条测试数据x
        :param case:用来接收获取到的cases表单数据
        :return:
        """
        # 动态替换请求参数中的手机号，sql中的手机号替换操作
        if case["request_data"].find("#phone") != 1:
            new_phone = get_new_phone()
            case = replace_mark_with_data(case, "#phone#", new_phone)
        # 将请请求数据从json字符串转换成字典对象
        # case["request_data"] = json.loads(case["request_data"])
        # 将response_data转成成字典
        response_data = eval(case["response_data"])
        #   步骤 测试数据  - 发起请求
        response = send_requests(case["request_method"], case["request_url"], case["request_data"])
        #   断言
        try:
            self.assertEqual(response.json()["code"], response_data["code"])
            self.assertEqual(response.json()["msg"], response_data["msg"])
            self.assertEqual(response.json()["success"], response_data["success"])
            # 如果check_sql有值，则需要查询sql
            if case["check_sql"]:
                sql_file = select_db.select_one_data(case["check_sql"])
                logger.info("sql查询结果: {}".format(sql_file))
                self.assertIsNotNone(sql_file)
        except AssertionError:
            logger.exception("断言失败")
            raise

