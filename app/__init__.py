from flask import Flask

# Initialise the application
app = Flask(__name__, instance_relative_config=True)

# Load our views
from app import views

# Load the config file
app.config.from_object('config')