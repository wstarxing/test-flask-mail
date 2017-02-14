# -*- coding: UTF-8 -*-
from flask import Flask
from flask_mail import Mail

from config import config

mail = Mail()


def create_app(config_name):
    app = Flask(__name__)

    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    mail.init_app(app)

    from app.main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app

