from app import app
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    message = 'welcome'
    return render_template( 'index.html' , message = message )


@app.route('/login')
def login():
    message = 'login'
    return render_template('login.html' , message = message)


@app.route('/archives')
def archives():
    message = 'archives'
    return render_template('archives.html' , message = message)


@app.route('/test')
def test():
    message = 'Test'
    return render_template('test.html' , message = message)
    

@app.route('/user')
def user():
    message = 'UserCenter'
    return render_template('user.html' , message = message)












