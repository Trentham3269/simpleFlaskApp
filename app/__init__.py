# Third part imports
from flask import Flask
from flask_sqlalchemt import SQLAlchemy

# Local imports
from config import app_config

# Database variable initialisation
db = SQLAlchemy()

def create_app(config_name):
	app = Flask(__name__, instance_relative_config=True)
	app.config.from_object(app_config[config_name])
	app.config.from_pyfile('config')
	db.init_app(app)

	return app
