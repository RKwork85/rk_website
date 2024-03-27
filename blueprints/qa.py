

from flask import Blueprint, render_template,request, g,redirect, url_for
from .forms import QusetionForm
from models import QuestionModel
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
            question = QuestionModel(title= title, content= content ,author = g.user)
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