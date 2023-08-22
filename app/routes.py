from app import app
from flask import render_template


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login')
def login():
    return render_template('account/login.html', title='Login')


@app.route('/signup')
def signup():
    return render_template('account/signup.html', title='Sign Up')
