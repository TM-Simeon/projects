from flask import Flask, render_template, request, redirect, url_for
from flask.views import View
from db import *
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required
# import sqlite3


app = Flask(__name__)

# create a Flask app instance
# app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key' # set secret key for session management

# create a LoginManager instance and initialize it with the Flask app
login_manager = LoginManager()
login_manager.init_app(app)

# create a User class that inherits from UserMixin
class User(UserMixin):
    pass

# callback function to load a user by their ID from the database
@login_manager.user_loader
def load_user(user_id):
    conn = sqlite3.connect('db.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM users WHERE user_id = ?', (user_id,))
    user_data = cur.fetchone()
    if user_data:
        user = User()
        user.id = user_data[0]
        user.email = user_data[1]
        user.password = user_data[2]
        user.username = user_data[3]
        return user

# route to handle login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        conn = sqlite3.connect('db.db')
        cur = conn.cursor()
        cur.execute('SELECT * FROM users WHERE email = ? AND password = ?', (email, password))
        user_data = cur.fetchone()
        if user_data:
            user = User()
            user.id = user_data[0]
            user.email = user_data[1]
            user.password = user_data[2]
            user.username = user_data[3]
            login_user(user)
            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html')
    else:
        return render_template('login.html')

# route to handle logout
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

# a protected route that requires login
@app.route('/')
# @login_required
def index():
    return render_template('index.html')

# @app.route('/')
# def index():
#     return render_template('index.html')

@app.route('/signup', methods=['POST', 'GET'])
def signup():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        name = request.form['name']
        response = insertuser(name, password, email)
        return response
    return render_template('signup.html')


@app.route('/studentSignup', methods=['POST','GET'])
def studentSignup():
    if request.method == 'POST':
        #check if user in users
        #check if credentials ok
        #insert user into students
        return redirect('/login')
    return render_template('studentSignup.html')
    
@app.route('/staffSignup', methods=['POST','GET'])
def staffSignup():
    if request.method == 'POST':
        #check if user in users
        #check if credentials ok
        #insert user into staff
        return redirect('/login')
    return render_template('staffSignup.html')

# @app.route('/login', methods=['POST','GET'])
# def login():
#     if request.method == 'POST':
#         #check if user in users
#         #check if credentials ok
#         #check if user in student or staff
#         return render_template('dashboard.html')
#     return render_template('login.html')

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')


if __name__ == '__main__':
    app.run(debug=True)