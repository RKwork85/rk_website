from flask import Blueprint, render_template, jsonify
from models import EmailCaptchaModel
from flask_mail import Message
from flask import request
from exts import mail, db
import string
import random


bp = Blueprint("auth",__name__, url_prefix="/auth")


@bp.route('/login')
def login():
    return render_template("login.html")


@bp.route('/register')
def register():
    return render_template("register.html")

# 验证码发送测试
@bp.route('/mail/test')
def mail_test():
    
    message = Message(subject="邮箱测试", recipients=["2735919386@qq.com"], body="这是三条测试信息")
    mail.send(message)
    return "邮件再次发送成功"

@bp.route('/captcha/email')
def get_email_captcha():

    email = request.args.get("eee")            # 这里抽了email不可以
    print(email)
    source = string.digits *4 
    captcha = random.sample(source, 4)
    print(captcha)
    captcha = ''.join(captcha)
    print(captcha)
    message = Message(subject="rk_website注册登录", recipients=[email], body=f"这是rk_website发送的注册验证码{captcha},快lai收啦！")  # 耗时操作扔给其他进程  写个装饰器起个线程去做
    mail.send(message)

    # email_captcha = EmailCaptchaModel(email=email, captcha= captcha)
    # db.session.add(email_captcha)
    # db.session.commit()


    return jsonify({"code":200, "message": "1332", })


# http://127.0.0.1:5000/auth/captcha/email?eamil=2735919386@qq.com
# http://127.0.0.1:5000/auth/captcha/email?eee=2735919386@qq.com
