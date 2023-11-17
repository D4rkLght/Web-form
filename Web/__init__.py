from flask import Flask
from flask_pymongo import PyMongo

from settings import Config


app = Flask(__name__)
app.config.from_object(Config)
app.config["MONGO_URI"] = "mongodb://mongodb:27017/myDatabase"
mongo = PyMongo(app)
db = mongo.db
PHONE_NUMBER_PATTERN = r"^(\+?7|7|8)(\d{3})(\d{3})(\d{2})(\d{2})$"
EMAIL_PATTERN = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
DATE_PATTERN = r"^(\d{2})\.(\d{2})\.(\d{4})$"

from . import api_views
