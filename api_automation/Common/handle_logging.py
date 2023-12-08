"""
日志收集时定制以下几点：
    日志的名字
    日志的级别
    日志的文件-级别
    日志的控制台-级别
    日志的文件路径
可配置化，读取配置文件内的字段值
。ini 后缀,表达格式：
[section]
opthion =value
opthion =value
[section]
opthion =value
opthion =value

yaml
"""
"""
创建好ini文件后，需要python读取ini文件的数据
引入ConfigParse类

实例化ConfigParse(),调用read方法，读取ini文件
conf=ConfigParse()
conf.read(file,encoding = "utf-8") #获取配置文件，把配置文件加载到内存当中

读取配置文件：.get("section","opthion")读取出来的值都是字符串
value = conf.get("log","name")
想改变成其他类型，有一下集中方法：
conf.getboolean(section,option)----获取布尔值，true false
conf.getint(section,option)---获取整数类型值
conf.getfloat(section,option)




"""
import os
import logging
from Common.handle_config import conf
from Common.handle_path import logs_dir



class MyLogger(logging.Logger):
    def __init__(self, file=None):
        # 设置输出级别，输出渠道
        super().__init__(conf.get("log", "name"),conf.get("log", "level"))
        # 设置日志格式
        fmt = "%(asctime)s  %(name)s %(levelname)s %(filename)s line:%(lineno)d：%(message)s"
        formatter = logging.Formatter(fmt)

        # 控制台渠道
        handel1 = logging.StreamHandler()
        handel1.setFormatter(formatter)
        self.addHandler(handel1)

        if file:
            handel2 = logging.FileHandler(file, encoding="utf-8")
            handel2.setFormatter(formatter)
            self.addHandler(handel2)
# 是否需要写入文件
if conf.getboolean("log", "file_ok"):
    file_name = os.path.join(logs_dir, conf.get("log", "file_name"))
    print(file_name)
else:
    file_name = None
logger = MyLogger(file_name)
# logger.info("11111111111")

