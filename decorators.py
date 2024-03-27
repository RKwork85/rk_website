from flask import g, redirect, url_for
from functools import wraps

def login_required(func):
    @wraps(func)
    def inner(*args, **kwargs):
        if g.user:
            return func(*args, **kwargs)
        else:
            return redirect(url_for("auth.login"))
    return inner


'''
问题描述：
    在没有登陆之前不能够访问 发布问答 页面
    如果有多个页面都要实现这个功能要实现一个装饰器用于处理这个函数




装饰器 先导入 functools  wraps
设置一个装饰器函数 参数是代表被装饰器的函数（随便写）
@wraps(func)    保留原函数的信息
在内部定义一个函数处理参数 def inner(*args, **kargs)
进行判断
返回

没有返回 ——8行
error
TypeError: The view function for 'qa.public_question' did not return a valid response. The function either returned None or ended without a return statement.
'''