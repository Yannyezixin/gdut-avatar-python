# coding: utf-8

from flask import Flask


def build_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('config.default')
    app.config.from_pyfile('config.py')
    app.config.from_envvar('APP_CONFIG_FILE', silent=True)

    from main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
