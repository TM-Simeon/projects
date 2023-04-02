from flask import Flask, render_template, request
from flask.views import View
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo
from flask_login import LoginManager, UserMixin
# from insertdb import *
import sqlite3

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'

# Initialize Flask-Login
# login_manager = LoginManager()
# login_manager.init_app(app)

# Define a user model for Flask-Login
class User(UserMixin):
    def __init__(self, id):
        self.id = id
        
# Define a user loader function for Flask-Login
# @login_manager.user_loader
# def load_user(user_id):
#     return User(user_id)

class Index(View):
    methods = ['GET']

    def dispatch_request(self):
        # return "you refreshed last at: " + datetime.now().strftime("%H:%M:%S")
        return render_template("index.html")

class SignUp(View):
    methods = ['GET', 'POST']
    
    def __init__(self):
        self.form = SignupForm()

    def dispatch_request(self):
        
        # if self.form.validate_on_submit():
        if request.method == 'POST':
            conn = sqlite3.connect('db.db')
            cursor = conn.cursor()
            query = 'insert into users(name, age, email) values("simeon",36,"simeon@gmail.com");'
            cursor.execute(query)
            conn.commit()
            conn.close()
            # insertUser(data)
            return "value inserted"
            # return redirect(url_for('login'))
        return render_template("signup.html", form=self.form)
    
class Login(View):
    methods = ['GET']

    def dispatch_request(self):
        return render_template("login.html")
    
class DashBoard(View):
    methods = ['GET']

    def dispatch_request(self):
        return render_template("dashboard.html")

class SignupForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('confirm_password', message='Passwords must match')])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired()])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')
    
app.add_url_rule('/', view_func=Index.as_view('index'))
app.add_url_rule('/signup', view_func=SignUp.as_view('signup'))
app.add_url_rule('/login', view_func=Login.as_view('login'))
app.add_url_rule('/dashboard', view_func=DashBoard.as_view('dashboard'))


if __name__ == '__main__':
    app.run(debug=True)