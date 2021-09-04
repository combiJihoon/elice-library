from datetime import timedelta
import os
import json

BASE_DIR = os.path.dirname(__file__)

with open('../secrets.json') as f:
    secrets = json.loads(f.read())
SECRET_PASSWORD = secrets["DATABASE_PASSWORD"]

SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://jihun:{SECRET_PASSWORD}@localhost:3306/library'
SQLALCHEMY_TRACK_MODIFICATIONS = False
PERMANENT_SESSION_LIFETIME = timedelta(hours=24)
SECRET_KEY = "b'\x0b,\x96\xdf\x9f\x85\xb2\xedj\x86\xe2\x9a\xae\x17\xa2\xdd'"
