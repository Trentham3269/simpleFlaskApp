from flask import render_template

from app import app

# Serve index.html on home URL
@app.route('/')
def index():
	return render_template("index.html")

# Serve about.html on /about
@app.route('/about')
def about():
	return render_template("about.html")