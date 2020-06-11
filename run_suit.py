#导包
import os
import time
import unittest
#创建测试套件
import HTMLTestRunner_PY3

from script.test_tpshop_login import TestTpshopLogin

suite=unittest.TestSuite()
#将测试用例添加到测试套件
suite.addTest(unittest.makeSuite(TestTpshopLogin))
#定义测试报告目录和名称
BASE_DIR=os.path.dirname(os.path.abspath(__file__))
report_path=BASE_DIR + "/report/tpshop{}.html".format(time.strftime('%Y%m%d %H%M%S'))
#使用HTMLTestRunner_Py3生成测试报告
with open(report_path,mode="wb")as f:
    #实例化HTMLtestRunner_PY3
    runner = HTMLTestRunner_PY3.HTMLTestRunner(f,verbosity=1,title="tpshop登录接口功能测试",
                                               description="这是一个更加美观的报告")
    #s使用实例化runner运行测试套件，生成测试报告
    runner.run(suite)