

from flask import Blueprint, render_template,request, g,redirect, url_for
from .forms import QusetionForm, AnswerForm
from models import QuestionModel, AnswerModel
from exts import db
from decorators import login_required

bp = Blueprint("qa", __name__, url_prefix="/qa")

# 127.0.0.1:5000
@bp.route("/public_question", methods= ["GET", "POST"])
@login_required
def public_question():
    if request.method == "GET":
        return render_template('public_question.html')
    else:
        form = QusetionForm(request.form)
        if form.validate():
            title = form.title.data
            content = form.content.data
            question = QuestionModel(title= title, content= content ,author = g.user)   # 我猜测就是这个g.user是那个外键的作用
            db.session.add(question)
            db.session.commit()
            return redirect(url_for('qa.index'))
        else:
            print(form.errors)
            return redirect(url_for("qa.public_question"))
        
@bp.route('/index')
def index():
    questions = QuestionModel.query.order_by(QuestionModel.create_time.desc()).all()   # 分页查询待补充
    return render_template('index.html', questions=questions)

@bp.route('/detail/<qa_id>')
def detail(qa_id):
    question = QuestionModel.query.get(qa_id)

    return render_template('detail.html', question= question)


# @bp.post("/answer/public") # 路由的另外一种写法
@bp.route('/answer/public', methods = ['POST'])
@login_required              # 只有登录了才能够评论
def public_answer():

    form = AnswerForm(request.form, methods=["POST"])
    print(form)
    print(form.question_id.data)
    if form.validate():
        print('hhhhhhhhhh')
        content = form.content.data
        print(content)
        question_id = form.question_id.data
        print(question_id)
        answer = AnswerModel(content = content, question_id=question_id, author_id = g.user.id)   #传入的参数要和和接口给的参数一致; author_id 又写错了...
        db.session.add(answer)
        db.session.commit()
        return redirect(url_for('qa.detail', qa_id = question_id))      # url_for 要写到一起，参数和地址


    else:
        print(form.errors)
        return redirect(url_for('qa.detail', qa_id = request.form.get("question_id")))