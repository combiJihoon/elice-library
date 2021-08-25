from datetime import timedelta
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(
    os.path.join(BASE_DIR, 'library.db')) + '?check_same_thread=False'
SQLALCHEMY_TRACK_MODIFICATIONS = False
PERMANENT_SESSION_LIFETIME = timedelta(hours=24)
SECRET_KEY = "b'\x0b,\x96\xdf\x9f\x85\xb2\xedj\x86\xe2\x9a\xae\x17\xa2\xdd'"
