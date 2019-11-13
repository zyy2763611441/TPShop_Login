"""
设计case实现
"""
# 1导包：
import json
import unittest
import requests

import app
from api.LoginApi import Login

from parameterized import parameterized


def read_json():
    data = []
    with open(app.PRO_PATH+"/data/login_data.json", encoding="utf-8") as f:
        for v in json.load(f).values():
            username = v.get("username")
            password = v.get("password")
            verify_code = v.get("verify_code")
            status = v.get("status")
            msg = v.get("msg")
            ele = (username, password, verify_code, status, msg)

            data.append(ele)
    # print(data)
    return data
# read_json()


#2创建测试类:

class TestLogin(unittest.TestCase):
    # 3初始化函数
    def setUp(self):
        self.session = requests.Session()  # 创建session对象
        self.login_obj = Login()

    # 4资源卸载函数
    def tearDown(self):
        self.session.close()

    # 5测试函数
    # 5-1测试验证码
    def test_get_verify_code(self):
        pass
        # 1 请求业务（当前实现：需要将该业务单独封装——封装进api包）
        # 2基本实现思想
        # 封装：api包下创建一个python文件，python文件中创建class，
        # 封装一个请求函数，返回请求结果验证，
        # 调用：创建api包下的class的对象，然后对象.函数（）调用
        # 关键点 ：session的传递
        response = self.login_obj.get_verify_code(self.session)
        # print("验证码接口响应的状态码：",response.status_code)
        # print("验证码接口响应的响应体：",response.content)
        # 2断言业务
        ct = response.headers.get("Content-Type")
        # print(ct)
        self.assertIn("image", ct)
        # 5-2测试登陆
        # 登陆与验证码获取比较：
        #

    @parameterized.expand(read_json())
    def test_login(self, username, password, verify_code, status, msg):
        # print(username, password, verify_code, status, msg)
        #先获取验证码接口
        response1 = self.login_obj.get_verify_code(self.session)
        #登陆
        response2 = self.login_obj.login(self.session, username, password, verify_code)
        # print(response2.json())
        # 断言
        #需要断言的是响应中自定义的状态码与响应体的提示信息
        #获取实际结果
        st = response2.json().get("status")
        ms = response2.json().get('msg')
        print("登陆接口实际的状态码：", st)
        print("登陆接口实际的提示信息:", ms)
        self.assertEqual(status, st)
        self.assertIn(msg, ms)
