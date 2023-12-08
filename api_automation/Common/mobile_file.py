import random

from Common.handle_db import select_db
from Common.handle_logging import logger

prefix = [133, 149, 153, 173, 177, 180, 181, 189, 199, 130, 131, 132, 145,
          155, 156, 166, 171, 175, 176, 185, 186, 166, 134, 135, 136, 137,
          138, 139, 147, 150, 151, 152, 157, 158, 159, 172]
def get_new_phone():
    while True:
        phone = get_phone()  # 调用生成手机号方法，存储到phone中
        check_phone = select_db.get_cont('SELECT * FROM `cmt-user-center`.ids_user WHERE mobile = "{}"'.format(phone))
        logger.info(phone)
        if check_phone == 0:   # 查询生成的手机号是否在数据库中，如果查询的条数等于0，则说明数据库中没查到
            # select_db.select_close()  # 没查到说明可用，关闭数据库连接
            return phone   # 返回此手机号

def get_phone():
    index = random.randint(0, len(prefix)-1)
    phone_mobile = str(prefix[index])
    for i in range(0, 8):
        phone_mobile += str(random.randint(0, 9))
    return phone_mobile

print(get_new_phone())