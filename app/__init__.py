import os

from flask import Flask
from flask_cors import CORS
from flask_restful import Api

from app.models import db
from app.schemas import ma

from app.resources.users import Users


def create_app():
    app = Flask(__name__)
    app.config.from_object(os.getenv('APP_SETTINGS'))
    CORS(
        app,
        support_credentials=True,
        resources={r"/*": {"origins": "*"}},
    )
    db.init_app(app)
    ma.init_app(app)
    api = Api(app, prefix='/api')
    api.add_resource(Users, '/users')
    return app
