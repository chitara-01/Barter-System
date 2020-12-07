from app import application
from flask import render_template
from forms import RegistrationForm, LoginForm
from models import User, Post


posts = [
    {
        'author': 'Anugrah Shukla',
        'title': 'My fav job these days :)',
        'content': 'East or west CoinSwitch is the BEST!!',
        'date_posted': 'November 24, 2020'
    },
    {
        'author': 'Muskan Chitara',
        'title': 'One LAZY day in my life :)',
        'content': 'Bleh bleh bleh bleh...',
        'date_posted': 'January 05, 2021'
    },
    {
        'author': 'Prince Chitara',
        'title': 'One TUTION day in my life :)',
        'content': 'Work work work work work work...',
        'date_posted': 'October 24, 2004'
    }
]


@application.route("/")
@application.route("/home")
def home():
    return render_template('home.html', posts=posts)

@application.route("/about")
def about():
    return render_template('about.html', title='About')

@application.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)

@application.route("/register")
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)
