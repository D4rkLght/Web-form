import os


class Config(object):
    SECRET_KEY = os.getenv('SECRET_KEY', default='MY_SECRET_KEY')