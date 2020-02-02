from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    #from .models import models
    # from services import services
    app = Flask(__name__, instance_relative_config=False)
    db.init_app(app)
    # models.init_app(app)
    # services.init_app(app)
    app.config.from_object('config.Config')

    with app.app_context():
        db.create_all()

        return app