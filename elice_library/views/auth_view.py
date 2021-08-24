from flask import Blueprint, render_template, request, url_for, flash, session, g
from werkzeug.utils import redirect
from bcrypt import checkpw, hashpw, gensalt
from elice_library import db
from elice_library.models import User

from elice_library.authentication import user_id_validate, signup_pw_validate, name_validate

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
    return render_template('auth/login.html')


@bp.route('/login', methods=['POST'])
def login():
    user_id = request.form['user_id']
    user_password = request.form['user_password']

    user_data = User.query.filter_by(user_id=user_id).first()

    # validators 실행
    if not user_data:
        flash('아이디를 다시 확인해 주세요.')
        return redirect(url_for('auth.login'))

    elif len(user_password) < 8:
        flash('비밀번호는 8자리 이상 입력하세요.')
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
    return render_template('auth/signup.html')


@bp.route('/signup', methods=['POST'])
def signup():
    user_id = request.form['user_id']
    user_password = request.form['user_password']
    user_password_check = request.form['user_password_check']
    user_name = request.form['user_name']

    user_data = User.query.filter_by(user_id=user_id).first()

    # 아이디 validator 실행
    if not user_id_validate(user_id):
        flash('아이디는 이메일 형식으로 입력하세요.')
        return redirect(url_for('auth.signup_try'))

    elif not signup_pw_validate(user_password):
        flash('아래의 비밀번호 규칙을 확인하세요.')
        return redirect(url_for('auth.signup_try'))

    elif not name_validate(user_name):
        flash('이름은 영문 또는 한글로 입력하세요.')
        return redirect(url_for('auth.signup_try'))

    else:
        # 아이디 중복 확인 후 회원가입 시작
        if not user_data:
            if user_password != user_password_check:
                flash('비밀번호가 일치하지 않습니다.')
                return redirect(url_for('auth.signup_try'))
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
