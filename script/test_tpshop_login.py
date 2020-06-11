import unittest
import requests

from api.test_tpshop_api import TestTpshopApi


# 创建函数
class TestTpshopLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # 实例化封装登录接口
        cls.login_api = TestTpshopApi()
        # 实例化session
        cls.session = requests.session()

    @classmethod
    def tearDownClass(cls):
        if cls.session != None:
            cls.session.close()

    def test01_login_success(self):
        # 发送获取验证码接口请求
        response = self.login_api.get_verify(self.session)
        # 断言验证码返回数据
        self.assertIn("image", response.headers.get("Content-Type"))
        # 发送登录接口请求
        data = {"username": "13800138006", "password": "123456", "verify_code": "8888"}
        response = self.login_api.login(data, self.session)
        print("打印结果为：", response.json())
        # 断言登录
        self.assertEqual(200, response.status_code)
        self.assertEqual(1, response.json().get("status"))
        self.assertIn("登陆成功", response.json().get("msg"))
    def test02_username_is_not(self):
        # 发送获取验证码接口请求
        response = self.login_api.get_verify(self.session)
        # 断言验证码返回数据
        self.assertIn("image", response.headers.get("Content-Type"))
        # 发送登录接口请求
        data = {"username": "13900138006", "password": "123456", "verify_code": "8888"}
        response = self.login_api.login(data, self.session)
        print("打印结果为：", response.json())
        # 断言登录
        self.assertEqual(200, response.status_code)
        self.assertEqual(-1, response.json().get("status"))
        self.assertIn("账号不存在", response.json().get("msg"))
    def test03_password_error(self):
        # 发送获取验证码接口请求
        response = self.login_api.get_verify(self.session)
        # 断言验证码返回数据
        self.assertIn("image", response.headers.get("Content-Type"))
        # 发送登录接口请求
        data = {"username": "13800138006", "password": "1234567", "verify_code": "8888"}
        response = self.login_api.login(data, self.session)
        print("打印结果为：", response.json())
        # 断言登录
        self.assertEqual(200, response.status_code)
        self.assertEqual(-2, response.json().get("status"))
        self.assertIn("密码错误", response.json().get("msg"))

