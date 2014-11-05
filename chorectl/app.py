from flask import Flask
from .frontend import frontend
from .models.db import db


def create_app():
    app = Flask(__name__)
    db.init_app(app)
    app.register_blueprint(frontend)
    return app
