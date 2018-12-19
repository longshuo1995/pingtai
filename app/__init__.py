from flask import Flask


def create_app():
    app = Flask(__name__)
    register_blueprint(app)
    return app


def register_blueprint(app):
    from app.user import bl_user
    app.register_blueprint(bl_user)
