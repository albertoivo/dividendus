import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    """Set Flask configuration vars."""

    DEBUG = True

    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@postgres:5432/dividendusdb'

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SECRET_KEY = os.urandom(32)

    SESSION_COOKIE_SECURE = True

    SESSION_COOKIE_NAME = 'Div-Cookie'

    WTF_CSRF_TIME_LIMIT = None
