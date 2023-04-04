from flask import Flask, render_template, request, redirect
from flask.views import View
import sqlite3

app = Flask(__name__)

# conn = sqlite3.connect('db.db')
# conn.execute('create table if not exists students (name text, addr text, city text)')
# conn.close()



class Index(View):
    def dispatch_request(self):
        return render_template('index.html')

class Signup(View):
    def dispatch_request(self):
        if request.method == 'POST':
            

            return redirect('/login')
        return render_template('signup.html')

class Login(View):
    def dispatch_request(self):
        if request.method == 'POST':
            email = request.form['email']
            password = request.form['password']
            user = User.query.filter_by(email=email, password=password).first()

            if user:
                if user.role == 'student':
                    student = Student.query.filter_by(user=user).first()
                    return redirect('/dashboard/student/' + str(student.id))
                elif user.role == 'instructor':
                    instructor = Instructor.query.filter_by(user=user).first()
                    return redirect('/dashboard/instructor/' + str(instructor.id))
            else:
                return 'Invalid email or password'
        return render_template('login.html')

class Dashboard(View):
    def dispatch_request(self):
        # role = role
        # id = id
        return render_template('dashboard.html')


app.add_url_rule('/', view_func=Index.as_view('index'))
app.add_url_rule('/signup', view_func=Signup.as_view('signup'), methods=['GET', 'POST'])
app.add_url_rule('/login', view_func=Login.as_view('login'), methods=['GET', 'POST'])
# app.add_url_rule('/dashboard/<string:role>/<int:id>', view_func=Dashboard.as_view('dashboard'))
app.add_url_rule('/dashboard', view_func=Dashboard.as_view('dashboard'))



if __name__ == '__main__':
    app.run()