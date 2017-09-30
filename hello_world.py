# Import flask class and create instance
from flask import Flask
app = Flask(__name__)

# Display result at home URL
@app.route('/')
def hello_world():
	return 'Hello World!'