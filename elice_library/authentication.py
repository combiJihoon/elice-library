from flask import url_for, redirect, flash
from bcrypt import checkpw, hashpw
import string
import re


'''
# 로그인: 비밀번호
def login_pw_length_validate(pw: str):
    if len(pw) < 8:
        flash('비밀번호는 8자리 이상 입력하세요.')
        return redirect(url_for('auth.login'))
'''


# 로그인, 회원가입: 이메일 아이디
def user_id_validate(user_id: str) -> bool:
    rule = r'^([\w-]+(?:\.[\w-]+)*)@((?:[\w-]+\.)*\w[\w-]{0,66})\.([a-z]{2,6}(?:\.[a-z]{2})?)$'
    valid = re.search(rule, user_id)

    if not valid:
        return False
    return True


'''
def user_id_exists_validate(user_data):
    if not user_data:
        flash('아이디를 다시 확인해 주세요.')
        return redirect(url_for('auth.login'))
'''

# 회원가입: 비밀번호
# 영문, 숫자, 특수문자 중 2종류 이상을 조합하여 최소 10자리 이상
# 3종류 이상을 조합하여 최소 8자리 이상의 길이로 구성


def signup_pw_validate(pw: str) -> bool:
    rules = "^(?=.*[a-zA-Z])(?=.*[0-9])[a-zA-Z0-9]{10,}$|^(?=.*[a-zA-Z])(?=.*[!@#$%^&*?])[a-zA-Z!@#$%^&*?]{10,}$|^(?=.*[!@#$%^&*?])(?=.*[0-9])[!@#$%^&*?0-9]{10,}$|^(?=.*[a-zA-Z])(?=.*[0-9])(?=.*[!@#$%^&*?])[a-zA-Z0-9!@#$%^&*?]{8,}$"
    p = re.compile(rules)
    if p.search(pw) is None:
        return False
    return True


'''
def password_exists_validate(user_data, user_password):
    if not checkpw(user_password.encode('utf-8'), user_data.user_password):
        flash('비밀번호가 일치하지 않습니다.')
        return redirect(url_for('auth.login'))
'''

# 회원가입: 이름


def name_validate(name: str) -> bool:
    rule = '^[A-Za-zㄱ-ㅣ가-힣]*$'
    p = re.compile(rule)
    if p.search(name) is None:
        return False
    return True


# def signup_pw_check(pw):
#     nums = string.digits
#     letters = string.ascii_letters
#     special_symbols = '!@#$%^&*'

#     is_nums = False
#     is_letters = False
#     is_special_symbols = False

#     if len(pw) >= 8:
#         for case in pw:
#             if case in nums:
#                 is_nums = True
#             elif case in letters:
#                 is_letters = True
#             elif case in special_symbols:
#                 is_special_symbols = True

#         checker = [is_nums, is_letters, is_special_symbols]
#         if len(pw) >= 10 and checker.count(True) >= 2:
#             return True
#         elif checker.count(True) >= 3:
#             return True
#         else:
#             return False
#     else:
#         return False
