"""
创建类：
        获取验证码的请求函数
"""
import app


class Login:
    # 初始化函数中创建一个成员变量封装，验证码接口的URL
    def __init__(self):
        self.get_verify_code_url = app.BASE_URL + "index.php?m=Home&c=User&a=verify"
        self.login_url = app.BASE_URL + "index.php?m=Home&c=User&a=do_login"

    def get_verify_code(self, session):
        return session.get(self.get_verify_code_url)

    def login(self, session, username, password, verify_code):
        my_login = {"username": username,
                    "password": password,
                    "verify_code": verify_code}
        return session.post(self.login_url, data=my_login)
