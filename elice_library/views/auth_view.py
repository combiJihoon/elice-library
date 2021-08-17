from flask import Blueprint, render_template, request, url_for, flash, session
from werkzeug.utils import redirect
from ..forms import RegistrationForm
from bcrypt import checkpw, hashpw, gensalt
from models import *

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/login', methods=['GET', 'POST'])
def login():
    login_form = RegistrationForm(request.form)
    if request.method == 'POST' and login_form.validate():
        user_data = User.query.filter(user_id=login_form.user_id.data).first()
        if not user_data:
            flash('존재하지 않는 아이디입니다.')
            return redirect(url_for('auth.login'))
        elif not checkpw(login_form.user_password.data.encode('utf-8'), user_data.user_password):
            flash('비밀번호가 일치하지 않습니다.')
            return redirect(url_for('auth.login'))
        else:
            session.clear()
            session['user_id'] = user_data.user_id
            flash(f'{user_data.user_id}님 안녕하세요!')
            return redirect(url_for('main.home'))
    else:
        return render_template('login.html')


@bp.route('/signup', methods=['GET', 'POST'])
def signup():
    return render_template('signup.html')
