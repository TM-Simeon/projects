from flask import Flask, render_template, redirect, url_for, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from flask.views import View

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'

# Initialize Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)

# Define a user model for Flask-Login
class User(UserMixin):
    def __init__(self, id):
        self.id = id
        
# Define a user loader function for Flask-Login
@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

class SignupView(View):
    methods = ['GET', 'POST']

    def __init__(self):
        self.form = SignupForm()

    def dispatch_request(self):
        if self.form.validate_on_submit():
            username = self.form.username.data
            password = self.form.password.data
            # ...
            return redirect(url_for('login'))
        return render_template('signup.html', form=self.form)
    
class LoginView(View):
    methods = ['GET', 'POST']

    def __init__(self):
        self.form = LoginForm()

    def dispatch_request(self):
        if self.form.validate_on_submit():
            username = self.form.username.data
            password = self.form.password.data
            # Verify user credentials
            user_id = 1  # Replace with your user ID lookup logic
            user = User(user_id)
            login_user(user)
            return redirect(url_for('dashboard'))
        return render_template('login.html', form=self.form)

class DashboardView(View):
    methods = ['GET']

    @login_required
    def dispatch_request(self):
        return render_template('dashboard.html', user=current_user)

class SignupForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('confirm_password', message='Passwords must match')])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired()])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')

app.add_url_rule('/', view_func=lambda: render_template('index.html'))
app.add_url_rule('/signup', view_func=SignupView.as_view('signup'))
app.add_url_rule('/login', view_func=LoginView.as_view('login'))
app.add_url_rule('/dashboard', view_func=DashboardView.as_view('dashboard'))





