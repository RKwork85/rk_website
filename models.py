from exts import db
from datetime import datetime

class UserModel(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), nullable = False)
    password = db.Column(db.String(200), nullable = False)
    email = db.Column(db.String(100), nullable = False, unique = True)
    join_time = db.Column(db.DateTime, default = datetime.now)


class EmailCaptchaModel(db.Model):
    __tablename__ = "email_capthcha"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(100), nullable = False)
    captcha = db.Column(db.String(100), nullable = False)
   
class QuestionModel(db.Model):

    __tablename__ = "question"
    id = db.Column(db.Integer, primary_key = True)   # 不设置自动递增，主键会自动递增
    title = db.Column(db.String(100), nullable = False)
    content = db.Column(db.Text ,nullable = False)
    create_time = db.Column(db.DateTime, default = datetime.now)

    # 外键
    author_id = db.Column(db.Integer, db.ForeignKey("user.id"))     #   定义是写在数据库中的   qa.py里面/ public_question
    author = db.relationship(UserModel, backref = "questions")      # 用来接收实例 而 外键定义的时候就定义了映射关系，sqlalchemy和自动去 
    # author = db.relationship(UserModel, backref = "questions")      # 那backref 就没什么用了
                                                                    # 逻辑：先使用查询查到表的所有数据 for循环 遍历每一条数据
                                                                    #  1 代码中定义外键的那行，就是数据库中表的那一列的列名 即代码中 变量的值（author_id）
                                                                    #  2 代码中backref定义的值， 是使用的方式 通过 questions访问anthor(这个author是定义外键时绑定的user.id的别名，也就是那条数据的别名) 使用方式 questions.anthor.username      

class AnswerModel(db.Model):
    __tablename__ = 'answer'
    id = db.Column(db.Integer, primary_key = True, autoincrement= True)
    content = db.Column(db.Text, nullable = False)
    create_time = db.Column(db.DateTime, default = datetime.now)

    # 外键定义：回答的外键是谁，回答的作者是谁， 回答的问题是什么
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'))
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    # 关系
    question = db.relationship(QuestionModel, backref= db.backref("answers", order_by = create_time.desc()))             # 通过主键拿到外键 通过question拿到answer
    author =  db.relationship(UserModel, backref= "answers")


