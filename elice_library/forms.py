from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

import re


def user_name_check(form, field):
    message = '이름은 한글 또는 영문으로만 입력하세요.'
    p = re.findall('^[A-Za-zㄱ-ㅣ가-힣]*$', field.data)
    if not p:
        raise ValidationError(message)


# '비밀번호는 영문, 숫자, 특수문자 중 2종류 이상을 조합하여 최소 10자리 이상 또는 3종류 이상을 조합하여 최소 8자리 이상의 길이로 구성'
'''
def user_password_check(form, field):
    message = '영문, 숫자, 특수문자를 혼합하여 비밀번호를 입력하세요.'
    en = '^[a-zA-Z]*$'
    num = '^[0-9]*$'
    sc = '^[!@#$%^&*?]*$'
    if len(field.data) >= 10:

    raise ValidationError(message)
'''


class SignupForm(FlaskForm):
    user_id = StringField("elice@elice.com", validators=[
                          DataRequired("아이디는 필수로 입력해야 합니다."), Email("이메일 형식으로 입력해야 합니다.")])
    user_password = PasswordField("비밀번호를 입력하세요", validators=[
                                  DataRequired("비밀번호는 필수로 입력해야 합니다."), EqualTo('user_password2', message='비밀번호가 일치하지 않습니다.')])
    user_password2 = PasswordField(
        "비밀번호를 다시 한 번 입력하세요", validators=[DataRequired("비밀번호 확인 항목은 필수로 입력해야 합니다.")])
    user_name = StringField("이름을 입력하세요", validators=[
                            DataRequired("이름은 필수로 입력해야 합니다."), user_name_check])


class LoginForm(FlaskForm):
    user_id = StringField("아이디를 입력하세요", validators=[
                          DataRequired("아이디를 입력하세요."), Email()])
    user_password = PasswordField("비밀번호를 입력하세요", validators=[
                                  DataRequired("비밀번호를 입력하세요.")])


class CommentForm(FlaskForm):
    content = StringField("의견을 입력해 주세요.", validators=[Length(min=10, max=300)])
