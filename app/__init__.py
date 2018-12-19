from flask import Flask


def create_app():
    print('create........')
    app = Flask(__name__)
    register_blueprint(app)
    return app


def register_blueprint(app):
    print('hahahahhh')
    from app.user import bl_user
    print('ready register...')
    app.register_blueprint(bl_user)
