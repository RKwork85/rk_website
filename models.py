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
    author_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    author = db.relationship(UserModel, backref = "questions")

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


