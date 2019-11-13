# 导包
import unittest
# 创建测试套件对象，组织被执行的测试函数
import app
from case.TestTPShopLogin import TestLogin
from tools.HTMLTestRunner import HTMLTestRunner
import time

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestLogin))
# 执行测试套件，借助于HTMLTestRunner.py将结果写出为测试报告文件（使用文件流）
# 打开文件流--创建HTMLTestRunner对象-----执行suite
with open(app.PRO_PATH+"./report/" + time.strftime("%Y%m%d%H%M%S") + ".html", "wb") as f:
    runner = HTMLTestRunner(f, title="我的测试报告",
                            description='TPshop')
    runner.run(suite)
