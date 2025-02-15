from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import app.models as models


db = SQLAlchemy()
migrate = Migrate()


def create_app(test_config=None):
    app = Flask(__name__)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@localhost:5432/solar_system_development'
    
    db.init_app(app)
    migrate.init_app(app, db)
    #from app.models.book import Book
    models.init_app(app)

    from .routes import solar_system_bp
    app.register_blueprint(solar_system_bp)

    return app
