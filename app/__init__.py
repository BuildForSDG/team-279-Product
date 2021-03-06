import os
from config.config import app_config
from flask_marshmallow import Marshmallow
from flask import Flask
from flask_login import LoginManager
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
login_manager = LoginManager()


def create_app(config_env):

    app = Flask(__name__)
    app.config.from_object(app_config[config_env])
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = "login"

    return app


""" Application version number. """
__version__ = '0.1.0'

app = create_app(os.getenv('ENVIRONMENT'))
api = Api(app=app, prefix="/api/v1")

# init ma
ma = Marshmallow(app)

from app import views
