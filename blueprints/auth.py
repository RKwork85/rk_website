from werkzeug.security import generate_password_hash, check_password_hash
from flask import Blueprint, render_template, jsonify
from models import EmailCaptchaModel, UserModel
from flask import request, redirect, url_for,session
from .forms import RegisterForm, LoginForm
from flask_mail import Message
from datetime import datetime
from exts import mail, db
import string
import random


bp = Blueprint("auth",__name__, url_prefix="/auth")


@bp.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    else:
        form = LoginForm(request.form)
        if form.validate():
            email = form.email.data
            password = form.password.data
            user = UserModel.query.filter_by(email=email).first()
            if not user:
                print('邮箱在数据库中不存在')
                return redirect(url_for("auth.login"))
            if check_password_hash(user.password, password):
                session['user_id'] = user.id
                redirect('/')
            else :
                print('密码错误')
                return redirect(url_for("auth.login"))
            return ('恭喜你成功登录')

        else:
            print(form.errors)
            return redirect(url_for("auth.login"))



@bp.route('/register',methods =["GET", "POST"])
def register():
    if request.method == 'GET':
        return render_template("register.html")
    else:
        form = RegisterForm(request.form)
        if form.validate():
            email = form.email.data
            username = form.username.data
            password = form.password.data
            user = UserModel(email= email, username=username, password= generate_password_hash(password))
            db.session.add(user)
            db.session.commit()
            # return redirect('/auth/login')

            return redirect(url_for('auth.login'))
        else:
            print(form.errors)
            return "fail"

# 验证码发送测试
@bp.route('/mail/test')
def mail_test():
    
    message = Message(subject="邮箱测试", recipients=["2735919386@qq.com"], body=f"我的宝贝，现在是:{datetime.now()}")
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
    message = Message(subject="rk_website注册登录", recipients=[email], body=f"这是rk_website发送的注册验证码{captcha},快lai收啦！发送时间：{datetime.now()}")  # 耗时操作扔给其他进程  写个装饰器起个线程去做
    mail.send(message)

    email_captcha = EmailCaptchaModel(email=email, captcha= captcha)
    db.session.add(email_captcha)
    db.session.commit()


    return jsonify({"code":200, "message": "1332", })


# http://127.0.0.1:5000/auth/captcha/email?eamil=2735919386@qq.com
# http://127.0.0.1:5000/auth/captcha/email?eee=2735919386@qq.com
# /mail/test
