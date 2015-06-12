from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.migrate import Migrate, MigrateCommand

from config import config


db = SQLAlchemy()
migrate = Migrate()

def make_app(env):
    app = Flask(__name__)
    app.config.from_object(config[env])
    config[env].init_app(app)

    db.init_app(app)
    migrate.init_app(app, db)

    @app.route('/')
    def index():
        return 'Hello'

    return app
