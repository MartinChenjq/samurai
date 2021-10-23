from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_pymongo import PyMongo
from flask_marshmallow import Marshmallow
from samurai.settings import Config

db = SQLAlchemy()
mongo = PyMongo()
ma = Marshmallow()

app = Flask(__name__)


def create_app():
    app.config.from_object(Config)
    db.init_app(app)

    mongo.init_app(app)

    ma.init_app(app)
    return app


create_app()
