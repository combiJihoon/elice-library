from flask import Blueprint, render_template, request, url_for, flash, session, g
from werkzeug.utils import redirect
from bcrypt import checkpw, hashpw, gensalt
from app import db
from models import User

from authentication import user_id_validate, signup_pw_validate, name_validate

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
        # return redirect(url_for('auth.login_try'))
        return render_template('auth/login.html', user_password=user_password, user_id=user_id)

    elif len(user_password) < 8:
        flash('비밀번호는 8자리 이상 입력하세요.')
        # return redirect(url_for('auth.login_try'))
        return render_template('auth/login.html', user_password=user_password, user_id=user_id)

    elif not checkpw(user_password.encode('utf-8'), user_data.user_password):
        flash('비밀번호가 일치하지 않습니다.')
        # return redirect(url_for('auth.login_try'))
        return render_template('auth/login.html', user_password=user_password, user_id=user_id)

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
        # return redirect(url_for('auth.signup_try'))
        return render_template('auth/signup.html', user_id=user_id, user_password=user_password, user_password_check=user_password_check, user_name=user_name)

    elif not signup_pw_validate(user_password):
        flash('비밀번호는 영문, 숫자, 특수문자 중 2종류 이상을 조합하여 최소 10자리 이상 또는 3종류 이상을 조합하여 최소 8자리 이상의 길이로 구성해야 합니다.')
        # return redirect(url_for('auth.signup_try'))
        return render_template('auth/signup.html', user_id=user_id, user_password=user_password, user_password_check=user_password_check, user_name=user_name)

    elif not name_validate(user_name):
        flash('이름은 영문 또는 한글로 입력하세요.')
        # return redirect(url_for('auth.signup_try'))
        return render_template('auth/signup.html', user_id=user_id, user_password=user_password, user_password_check=user_password_check, user_name=user_name)

    else:
        # 아이디 중복 확인 후 회원가입 시작
        if not user_data:
            if user_password != user_password_check:
                flash('비밀번호가 일치하지 않습니다.')
                # return redirect(url_for('auth.signup_try'))
                return render_template('auth/signup.html', user_id=user_id, user_password=user_password, user_password_check=user_password_check, user_name=user_name)

            hashed_password = hashpw(
                user_password.encode('utf-8'), gensalt())

            new_user = User(user_id=user_id,
                            user_password=hashed_password, user_name=user_name)
            db.session.add(new_user)
            db.session.commit()

            flash('성공적으로 가입 되었습니다!')
            return redirect(url_for('auth.login'))
        else:
            flash('이미 존재하는 아이디입니다. 다시 입력해 주세요.')
            # return redirect(url_for('auth.signup_try'))
            return render_template('auth/signup.html', user_id=user_id, user_password=user_password, user_password_check=user_password_check, user_name=user_name)


@bp.route('/logout', methods=['GET'])
def logout():
    session.clear()
    flash('로그아웃 되었습니다.')
    return redirect(url_for('main.home'))
