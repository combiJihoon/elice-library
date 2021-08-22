from flask import Blueprint, render_template, request, url_for, flash, session, g
from werkzeug.utils import redirect
from forms import LoginForm, SignupForm
from bcrypt import checkpw, hashpw, gensalt
from app import db
from models import User
from flask_login import login_user


bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')
    if user_id is None:
        g.user = None
    else:
        g.user = User.query.get(user_id)


@bp.route('/login', methods=['GET'])
def login_try():
    return render_template('login.html')


@bp.route('/login', methods=['POST'])
def login():
    user_id = request.form['user_id']
    user_password = request.form['user_password']

    user_data = User.query.filter_by(user_id=user_id).first()

    if not user_data:
        flash('아이디를 다시 확인해 주세요.')
        return redirect(url_for('auth.login'))
    elif len(user_password) < 8:
        flash('비밀번호는 8자리 이상 입력해야 합니다.')
        return redirect(url_for('auth.login'))
    elif not checkpw(user_password.encode('utf-8'), user_data.user_password):
        flash('비밀번호가 일치하지 않습니다.')
        return redirect(url_for('auth.login'))
    else:
        session.clear()
        session['user_id'] = user_id
        flash(f'{user_data.user_name}님 안녕하세요!')
        return redirect(url_for('main.home'))


@bp.route('/signup', methods=['GET'])
def signup_try():
    return render_template('signup.html')


@bp.route('/signup', methods=['POST'])
def signup():
    user_id = request.form['user_id']
    user_password = request.form['user_password']
    user_name = request.form['user_name']

    user_data = User.query.filter_by(user_id=user_id).first()

    # 아이디 중복 확인 후 회원가입 시작
    if not user_data:
        hashed_password = hashpw(
            user_password.encode('utf-8'), gensalt())

        new_user = User(user_id=user_id,
                        user_password=hashed_password, user_name=user_name)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('main.home'))
    else:
        flash('이미 존재하는 아이디입니다. 다시 입력해 주세요.')
        return redirect(url_for('auth.signup_try'))


@bp.route('/logout', methods=['GET'])
def logout():
    session.clear()
    flash('로그아웃 되었습니다.')
    return redirect(url_for('main.home'))
