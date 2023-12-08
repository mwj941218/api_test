#
# #
#
#
#
# import requests
#
#
# sess = requests.session()
#
# headers = {"Content-type": "application/json",
#
#                    }
# url = "https://www.yidab.com/doctor-app/user/info.do"
# data={
#     "mobile": "17600556607",
#     "verifyCode": "8888"
# }
#
# res = sess.request("POST",url,json=data,headers=headers)
# print(res.json())
#
#
#
#
#
#

class Decorator:
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, owner):
        print('调用的是get函数')
        return self.func(instance)


class Test:
    def __init__(self, *args, **kwargs):
        self.value_list = []
        if args:
            for i in args:
                if str(i).isdigit():
                    self.value_list.append(i)
        if kwargs:
            for v in kwargs.values():
                if str(v).isdigit():
                    self.value_list.append(v)
    @Decorator
    def sum(self):
        result = 0
        print(self.value_list)
        for i in self.value_list:
            result += i

        return result


if __name__ == '__main__':
    t = Test(1,2,3,4,5,6,7,8,i=9,ss=10,strings = 'lll')
    print(t.sum)
