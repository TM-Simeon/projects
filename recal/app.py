from flask import Flask, request, render_template, redirect, url_for
from db import *


app = Flask(__name__)

@app.route('/index.html')
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/parent.html')
def parent():
    return render_template('parent.html',methods=['POST','GET'])

@app.route('/staff.html', methods=['POST','GET'])
def staff():
    return render_template('staff.html')

@app.route('/student.html', methods=['POST','GET'])
def student():
    return render_template('student.html')

@app.route('/character.html', methods=['POST','GET'])
def character():
    if request.method == 'POST':
        attribute = request.form['course_id']
    return render_template('character.html')

@app.route('/club.html', methods=['POST','GET'])
def club():
    if request.method == 'POST':
        club_id = request.form['course_id']
    return render_template('club.html')

@app.route('/sports.html', methods=['POST','GET'])
def sports():
    if request.method == 'POST':
        game_id = request.form['course_id']
    return render_template('sports.html')

@app.route('/test.html', methods=['POST','GET'])
def test():
    if request.method == 'POST':
        course_id = request.form['course_id']
    return render_template('test.html')

@app.route('/updatecharacter.html', methods=['POST','GET'])
def updatecharacter():
    if request.method == 'POST':
        attribute = request.form['course_id']
    return render_template('updatecharacter.html')

@app.route('/updateclub.html', methods=['POST','GET'])
def updateclub():
    if request.method == 'POST':
        club_id = request.form['course_id']
    return render_template('updateclub.html')

@app.route('/updatesport.html', methods=['POST','GET'])
def updatesport():
    if request.method == 'POST':
        game_id = request.form['course_id']
    return render_template('updatesport.html')

@app.route('/updatetest.html', methods=['POST','GET'])
def updatetest():
    if request.method == 'POST':
        course_id = request.form['course_id']
    return render_template('updatetest.html')

@app.route('/insertstaff', methods=['POST','GET'])
def insertstaff():
    if request.method == 'POST':
        staff_name = request.form['name']
        course_id = request.form['staff_id']
        email = request.form['email']
        insertstaff(staff_name,course_id, email)
    return render_template('insertstaff.html', methods=['POST','GET'])

@app.route('/insertstudent')
def insertstudent():
    if request.method == 'POST':
        student_name = request.form['name']
        email = request.form['email']
        department = request.form['department']
        insertstudent(student_name, email, department)
    return render_template('insertstudent.html')

@app.route('/insertcourse')
def insertcourse():
    if request.method == 'POST':
        course_id = request.form['course_id']
        course_title = request.form['course_title']
        description = request.form['description']
        staff_id = request.form['staff_id']
        insertcourse(course_id, course_title, description, staff_id)
    return render_template('insertcourse.html')

@app.route('/insertenrollment')
def insertenrollment():
    if request.method == 'POST':
        student_id = request.form['student_id']
        course_id = request.form['course_id']
        insertenrollment(student_id, course_id)
    return render_template('insertenrollment.html')

@app.route('/insertresult')
def insertresult():
    if request.method == 'POST':
        student_id = request.form['student_id']
        course_id = request.form['course_id']
        test1 = request.form['test1']
        test2 = request.form['test2']
        test3 = request.form['test3']
        exam = request.form['exam']
        insertresults(student_id, course_id, test1, test2, test3, exam)
    return render_template('insertresult.html')

@app.route('/updateresult')
def updateresult():
    if request.method == 'POST':
        course_position = request.form['courese_position']
        student_id = request.form['student_id']
        course_id = request.form['course_id']
        updateresult(course_position, student_id, course_id)
    return render_template('updateresult.html')

@app.route('/insertclassresult')
def insertclassresult():
    if request.method == 'POST':
        student_id = request.form['student_id']
        total_score = request.form['total_score']
        department = request.form['department']
        insertclassresult(student_id, total_score, department)
    return render_template('insertclassresult.html')

@app.route('/calresults')
def calresult():
    if request.method == 'POST':
        department = request.form['department']
        calresults(department)
    return render_template('calresult.html')


if __name__ == '__main__':
    app.run()
