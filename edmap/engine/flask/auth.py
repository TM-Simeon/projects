# from flask import Flask, render_template, redirect, url_for, request
# from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required
# import sqlite3

# # create a Flask app instance
# app = Flask(__name__)
# app.config['SECRET_KEY'] = 'edmap#secret' # set secret key for session management

# # create a LoginManager instance and initialize it with the Flask app
# login_manager = LoginManager()
# login_manager.init_app(app)

# # create a User class that inherits from UserMixin
# class User(UserMixin):
#     pass

# # callback function to load a user by their ID from the database
# @login_manager.user_loader
# def load_user(user_id):
#     conn = sqlite3.connect('db.db')
#     cur = conn.cursor()
#     cur.execute('SELECT * FROM users WHERE user_id = ?', (user_id))
#     user_data = cur.fetchone()
#     if user_data:
#         user = User()
#         user.id = user_data[0]
#         user.email = user_data[1]
#         user.password = user_data[2]
#         user.username = user_data[3]
#         return user

# # route to handle login page
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         email = request.form['email']
#         password = request.form['password']
#         conn = sqlite3.connect('db.db')
#         cur = conn.cursor()
#         cur.execute('SELECT * FROM users WHERE email = ? AND password = ?', (email, password))
#         user_data = cur.fetchone()
#         if user_data:
#             user = User()
#             user.id = user_data[0]
#             user.email = user_data[1]
#             user.password = user_data[2]
#             user.username = user_data[3]
#             login_user(user)
#             return redirect(url_for('index'))
#         else:
#             return render_template('login.html', error='Invalid email or password')
#     else:
#         return render_template('login.html')

# # route to handle logout
# @app.route('/logout')
# @login_required
# def logout():
#     logout_user()
#     return redirect(url_for('login'))

# # a protected route that requires login
# @app.route('/')
# @login_required
# def index():
#     return render_template('index.html')

# if __name__ == '__main__':
#     app.run(debug=True)