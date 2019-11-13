"""
测试框架搭建：分包
    核心：api +case + data
        api:封装requests相关实现，之既然访问服务器（请求业务）
        case：封装unittest相关实现，断言业务+参数化
        data：封装测试数据
        三者关系：case是核心
        case的测试函数中需要调用api的请求业务，且需要通过参数化读取data中的数据
    报告：report+tools+run_suite.py
    report:保存最终生成的测试报告
    tools：工具
    run_suite.py:组织测试套件，并调用tools生成写出测试报告
    配置：app.py
        app.py:封装接口的资源路径前缀
                封装项目绝对路径的获取
                封装日志输出的配置信息

"""
# 封装接口资源路径前缀
import os

import logging
from logging import handlers

APP_PATH = os.path.abspath(__file__)

PRO_PATH = os.path.dirname(APP_PATH)
BASE_URL = "http://localhost/"


def my_log_config():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    to_1 = logging.StreamHandler()
    to_2 = logging.handlers.TimedRotatingFileHandler(PRO_PATH + "/log/hello.log",
                                                     when="h",
                                                     interval=12,
                                                     backupCount=10,
                                                     encoding="utf-8")
    formatter = logging.Formatter(
        "%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s")
    to_1.setFormatter(formatter)
    to_2.setFormatter(formatter)
    logger.addHandler(to_1)
    logger.addHandler(to_2)
my_log_config()
logging.info("hello")