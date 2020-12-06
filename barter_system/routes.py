from flask import render_template, url_for
from barter_system import app
from barter_system.models import User, Post

@app.route("/")
@app.route("/home")
def home():
    return "<h1>Welcome to Barter System!</h1>"
