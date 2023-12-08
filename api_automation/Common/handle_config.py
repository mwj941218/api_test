
"""
获取config内容
"""
import os
from configparser import ConfigParser
from Common.handle_path import conf_dir
class HandleConfig(ConfigParser):
    def __init__(self, file_path):
        super().__init__()
        self.read(file_path, encoding="utf-8")

file_path= os.path.join(conf_dir, "log_config.ini")
conf = HandleConfig(file_path)
# if __name__ == '__main__':
#     conf = HandleConfig(conf_dir + "log_config.ini")
#     sd = conf.get("log", "name")
#
#     import os
#
#     config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),"log_config.ini")
#     conf = HandleConfig(config_path)

