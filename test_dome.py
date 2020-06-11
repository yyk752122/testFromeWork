import requests
#发送获取验证码请求
verify_url="http://localhost/index.php?m=Home&c=User&a=verify"
#实例化session
session=requests.session()
session.get(url=verify_url)
#发送登录请求
login_ulr="http://localhost/index.php?m=Home&c=User&a=do_login"
data={"username":"13800138006","password":"123456","verify_code":"8888"}
response_login=session.post(url=login_ulr,data=data)
#查看结果
print("登录结果为：",response_login.json())
session.close()