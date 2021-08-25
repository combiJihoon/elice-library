from config.default import *
from datetime import timedelta

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(
    os.path.join(BASE_DIR, 'library.db')) + '?check_same_thread=False'
SQLALCHEMY_TRACK_MODIFICATIONS = False
PERMANENT_SESSION_LIFETIME = timedelta(hours=24)
SECRET_KEY = "dev"
