from app import application
from models import User, Post

@application.route("/")
@application.route("/home")
def home():
    return "<h1>Welcome to Barter System!</h1>"
