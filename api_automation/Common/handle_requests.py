import requests
import json
from Common.handle_logging import logger
from Common.handle_config import conf





def __handle_header(token=None):
    headers = {"Content-type": "application/json",

               }
    if token:
        headers["token"] = token
    return headers




def __pre_url(url):
    """
    :param url: 处理拼接URL
    :return:
    """

    base_url = conf.get("server", "base_url")
    if url.startswith("/"):
        return base_url + url
    elif url.startswith("http"):
        return url

    else:
        return base_url + "/" + url

def __pre_data(data):
    if data is not None and isinstance(data, str):
        return json.loads(data)
    return data

def send_requests(mathod, url, data=None,token=None):
    """
    自定义发送请求，实例化session，创建会话，登录获取cookies会自动存储会话，之后接口用实例调用request发送请求会自动带上cookisx
    :param mathod:请求方式
    :param url: 请求地址
    :param data: 请求参数
    :param cookies: cookies值
    :param headers: 请求头
    :return:
    """
    headers = __handle_header(token)
    # logger.info("请求头是：{}".format(headers))
    url = __pre_url(url)
    logger.info("拼接后的URL：{}".format(url))
    # 如果是字符串则转换成字典对象
    data = __pre_data(data)
    if "token" in headers.keys():
        res = requests.request(mathod, url, json=data, headers=headers)
    else:
        sess = requests.session()
        res = sess.request(mathod, url, json=data, headers=headers)
        logger.info("cookies:{}".format(res.cookies))
    logger.info("request:{}".format(data))
    logger.info("response：{}".format(res.json()))
    return res

