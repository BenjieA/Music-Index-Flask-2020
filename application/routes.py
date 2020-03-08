from application import app
from flask import render_template

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Search')

@app.route('/about')
def about():
    return render_template('about.html', title='about')

@app.route('/login',methods=['GET', 'POST'])
def login():
    return render_template('login.html', title='Login')

@app.route('/register',methods=['GET', 'POST'])
def register():
    return render_template('register.html', title='Register')


@app.route('/add',methods=['GET', 'POST'])
def add():
    return render_template('add.html', title='Add a Song')

@app.route('/edit', methods=['GET', 'POST'])
def edit():
    return render_template('edit.html', title='')
