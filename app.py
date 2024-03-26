from flask import Flask
from exts import db
from models import UserModel
from blueprints.auth import bp as auth_bp
from blueprints.qa import bp as qa_bp
from flask_migrate import Migrate

import config

app = Flask(__name__)

# 绑定配置文件
app.config.from_object(config)

db.init_app(app)

# migrate 数据迁移
Migrate(app, db)



# 注册蓝图
app.register_blueprint(auth_bp)
app.register_blueprint(qa_bp)
@app.route('/')
def hello():
    return '你好啊，我是木子'


if __name__ == '__main__':
    app.run(debug=True)
