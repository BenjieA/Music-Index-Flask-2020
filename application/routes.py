from application import app
from flask import render_template

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home')

@app.route('/about')
def about():
    return render_template('about.html', title='about')

@app.route('/login')
def login():
    return render_template('login.html', title='Login')

@app.route('/register')
def register():
    return render_template('register.html', title='Register')

@app.route('/search')
def search():
    return render_template('search.html', title='Search')

@app.route('/add')
def add():
    return render_template('add.html', title='Add a Song')
