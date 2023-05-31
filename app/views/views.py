from app import app
from flask import render_template

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login/login.html')

@app.route('/signup')
def signup():
    return render_template('signup/signup.html')

# Add more routes and views as needed
