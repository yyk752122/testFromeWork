import requests


# 定义封装的类
class TestTpshopApi:
    def __init__(self):
        # 验证码url和登录url
        self.verify_url = "http://localhost/index.php?m=Home&c=User&a=verify"
        self.login_url = "http://localhost/index.php?m=Home&c=User&a=do_login"

    # 封装获取验证码
    def get_verify(self, session):
        return session.get(url=self.verify_url)

    # 封装登录接口
    def login(self, data, session):
        return session.post(url=self.login_url, data=data)
