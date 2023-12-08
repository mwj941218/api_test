""""
1.一条用例涉及到的数据当中，有几个需要替换的，如：url，reqeust_data,check_sql


"""
import json


def  replace_mark_with_data(case, mark, real_data):
    """
    遍历一个用例涉及到的所有数据，如果需要替换都会替换
    :param case: excel单条用例
    :param mark: 用例当中的占位符，#XXX# ，要替换的数据
    :param real_data: 生成的真实数据，要替换mark最终的数据
    :return:
    """
    for key, value in case.items():
        if value is not None and isinstance(value, str):
            if value.find(mark) != -1:
                case[key] = value.replace(mark, real_data)
    return case

#
# if __name__ == '__main__':
#     from Common.mobile_file import get_new_phone
#
#     new_phone = get_new_phone()
#     case = {'id': "#phone#", 'request_method': 'POST', 'title': '登录',
#                        'request_url': 'https://api.yidab.com/yideb-app/user/login.do',
#                        'request_data': '{"deviceId": "EB44550306D24FB0990882E38B6C9DFD","osType": "2","userId": '
#                                        '"1528915867000246272","deviceModel": "iPhone 8 Plus", "channel": "苹果",'
#                                        '"data": {"mobile": "#phone#","verifyCode": "0829"},"version": "v3.5.3",'
#                                        '"terminalType": "3","networkType": "4","osVersion": "13.6","networkOperator":'
#                                        '"46001","deviceBrand": "苹果"}',
#                        'response_data': '{"code": 200,"msg": "登录成功","success": True}',
#                        'check_sql': 'SELECT * FROM `cmt-user-center`.ids_user WHERE mobile = "#phone#"'}
#
#     if case["request_data"].find("#phone#") != -1:
#         case = replace_mark_with_data(case,'#phone#',new_phone)
#     print(case)
