import os


class Config(object):
    MONGO_URI = os.getenv("DATABASE_URI", default="mongodb://mongodb:27017/myDatabase")
    SECRET_KEY = os.getenv("SECRET_KEY", default="MY_SECRET_KEY")
