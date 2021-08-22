import string


def login_pw_min_length(pw):
    return len(pw) >= 8


def signup_pw_check(pw):
    nums = string.digits
    letters = string.ascii_letters
    special_symbols = '!@#$%^&*'

    # rule = set(string.letters + string.digits + '!@#$%^&*')

    is_nums = False
    is_letters = False
    is_special_symbols = False

    if len(pw) >= 8:
        for case in pw:
            if case in nums:
                is_nums = True
            elif case in letters:
                is_letters = True
            elif case in special_symbols:
                is_special_symbols = True

        checker = [is_nums, is_letters, is_special_symbols]
        if len(pw) >= 10 and checker.count(True) >= 2:
            return True
        elif checker.count(True) >= 3:
            return True
        else:
            return False
    else:
        return False
