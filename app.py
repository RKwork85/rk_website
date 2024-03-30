from flask import Flask, g, session
from exts import db, mail
from models import UserModel
from blueprints.auth import bp as auth_bp
from blueprints.qa import bp as qa_bp
from flask_migrate import Migrate

import config

app = Flask(__name__)

# 绑定配置文件
app.config.from_object(config)      

db.init_app(app)
mail.init_app(app)

# migrate 数据迁移
Migrate(app, db)



# 注册蓝图
app.register_blueprint(auth_bp)
app.register_blueprint(qa_bp)

# 两个钩子函数
@app.before_request          #  在请求之前就自动获取变量值， 每次请求都要写代码，获取用户的信息
def my_before_request():
    user_id = session.get("user_id")
    if user_id:
        user = UserModel.query.get(user_id)
        setattr(g, "user", user)
    else:
        setattr(g, "user", None)

@app.context_processor                # 在静态网页中用此变量：g.user（是一个实例）， 上下文处理器
def my_contex_processor():
    return {'user': g.user} 



@app.route('/')
def hello():
    return '你好啊，我是木子'


if __name__ == '__main__':
    app.run(debug=True)
