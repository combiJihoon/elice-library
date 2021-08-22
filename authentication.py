import string
import re


def login_pw_min_length(pw: str) -> bool:
    return len(pw) >= 8


# 비밀번호 규칙
# 영문, 숫자, 특수문자 중 2종류 이상을 조합하여 최소 10자리 이상
# 3종류 이상을 조합하여 최소 8자리 이상의 길이로 구성
def signup_pw_check(pw: str) -> bool:
    rules = "^(?=.*[a-zA-Z])(?=.*[0-9])[a-zA-Z0-9]{10,}$|^(?=.*[a-zA-Z])(?=.*[!@#$%^&*?])[a-zA-Z!@#$%^&*?]{10,}$|^(?=.*[!@#$%^&*?])(?=.*[0-9])[!@#$%^&*?0-9]{10,}$|^(?=.*[a-zA-Z])(?=.*[0-9])(?=.*[!@#$%^&*?])[a-zA-Z0-9!@#$%^&*?]{8,}$"
    p = re.compile(rules)
    if p.search(pw) is None:
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
