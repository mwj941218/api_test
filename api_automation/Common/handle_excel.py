"""
excel类，你的需求是实现什么?
1、读取表头
2、读取数据  -读取表头以外的所有数据，最终返回值：列表，成员是每一行数据


初始化工作？ 加载一个excel，打开一个表单

"""
from openpyxl import load_workbook
import os
import json

class HandleExcel:
    def __init__(self, file_path, sheet_name):
        """
        :param file_path:初始化文档路径
        :param sheet_name:初始化文档表单name
        """
        self.wb = load_workbook(file_path)
        self.sh = self.wb[sheet_name]
        # 初始化中的变量要想在其他方法中使用，那么则需要设置为实例属性

    def read_titles(self):
        """
        获取表单的表头
        :return:
        """
        titles = []
        for itm in list(self.sh.rows)[0]:
            titles.append(itm.value)
        return titles
    def read_all_datas(self):
        """
        获取表单所有行数据，从第一行开始获取
        获取后遍历每一行数据，存入列表中
        再将表头与列表打包成字典，存入列表
        :return:
        """
        titles = self.read_titles()
        all_datas = []
        for itmes in list(self.sh.rows)[1:]:
            values = []
            for val in itmes:
                values.append(val.value)
                # print(values)
            res = dict(zip(titles, values))
            # print(res)

            all_datas.append(res)
        return all_datas

    def close_file(self):
        self.wb.close()
#
if __name__ == '__main__':
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../TestDatas/api_case.xlsx")
    exc = HandleExcel(file_path, "yidab_login")
    cases = exc.read_all_datas()
    exc.close_file()
    for itme in cases:
        print(itme)
        print(type(itme))


case = {'id': 1, 'request_method': 'POST', 'title': '登录', 'request_url': 'https://api.yidab.com/yideb-app/user/login.do', 'request_data': '{\n "deviceId": "EB44550306D24FB0990882E38B6C9DFD",\n "osType": "2",\n "userId": "1528915867000246272",\n "deviceModel": "iPhone 8 Plus",\n "channel": "苹果",\n "data": {\n  "mobile": "#phone#",\n  "verifyCode": "0829"\n },\n "version": "v3.5.3",\n "terminalType": "3",\n "networkType": "4",\n "osVersion": "13.6",\n "networkOperator": "46001",\n "deviceBrand": "苹果"\n}', 'response_data': '{"code": 200,"msg": "登录成功","success": True}', 'check_sql': 'SELECT * FROM `cmt-user-center`.ids_user WHERE mobile = "#phone#"'}
