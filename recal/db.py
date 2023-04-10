import sqlite3

# create database  DO NOT DELETE THIS COMMENTS, WE USE IT TO CREATE TABLES THEN COMMENT IT OUT TO IMPROVE SPEED
# conn = sqlite3.connect('db.db')
# conn.execute('CREATE TABLE IF NOT EXISTS staff (staff_id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, course_id TEXT NOT NULL, email TEXT NOT NULL, UNIQUE(name, email, course_id))')
# conn.execute('CREATE TABLE IF NOT EXISTS student(student_id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, email TEXT NOT NULL UNIQUE)')
# conn.execute('CREATE TABLE IF NOT EXISTS courses (course_id TEXT PRIMARY KEY NOT NULL UNIQUE, course_title TEXT NOT NULL UNIQUE, description TEXT NOT NULL, staff_id INTEGER NOT NULL, FOREIGN KEY (staff_id) REFERENCES staff(staff_id))')
# conn.execute('CREATE TABLE IF NOT EXISTS enrollment (enrollment_id INTEGER PRIMARY KEY AUTOINCREMENT, student_id INTEGER NOT NULL, course_id TEXT NOT NULL, UNIQUE(student_id, course_id) FOREIGN KEY (student_id) REFERENCES student(student_id), FOREIGN KEY (course_id) REFERENCES courses(course_id))')
# conn.execute('CREATE TABLE IF NOT EXISTS results (student_id INTEGER NOT NULL, course_id TEXT NOT NULL, test1 INTEGER, test2 INTEGER, test3 INTERGER, exam INTEGER, total INTEGER, course_position INTEGER, UNIQUE(student_id, course_id), FOREIGN KEY (student_id) REFERENCES student(student_id) FOREIGN KEY (course_id) REFERENCES courses(course_id))')
# conn.execute('CREATE TABLE IF NOT EXISTS class_result (student_id INTEGER NOT NULL UNIQUE, total_score INTEGER NOT NULL, class_position INTEGER,  FOREIGN KEY (student_id) REFERENCES student(student_id))')
# conn.commit()
# conn.close()

def insertstaff(name, course_id, email):
    try:
        conn = sqlite3.connect('db.db')
        conn.execute("INSERT INTO staff (name, course_id, email) values('{}','{}','{}')".format(name, course_id, email))
        conn.commit()
        conn.close()
        return ("staff inserted successfully")
    except Exception as e:
        return e

def insertstudent(name, email):
    try:
        conn.sqlite3.connect('db.db')
        conn.execute("INSERT INTO student (name, email) values('{}','{}')".format(name, email))
        conn.commit()
        conn.close()
        return ("student insersed successfully")
    except Exception as e:
        return e
    
def insertcourse(course_id, course_title, description, staff_id):
    try:
        #check if staff id exist
        conn = sqlite3.connect('db.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM staff WHERE staff_id='{}'".format(staff_id))
        results = cursor.fetchone()
        conn.commit()
        conn.close()
        if results is not None:
            try:
                conn = sqlite3.connect('db.db')
                conn.execute("INSERT INTO courses (course_id, course_title, description, staff_id) values('{}','{}','{}','{}')".format(course_id, course_title, description, staff_id))
                conn.commit()
                conn.close()
                return ("course insersed successfully")
            except Exception as e:
                return e
        else:
            return ("there is currently no staff for this course")
    except Exception as e:
        return e
    
def insertenrollment(student_id, course_id):
    try:
        conn = sqlite3.connect('db.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM student WHERE student_id='{}'".format(student_id))
        student = cursor.fetchone()
        cursor.execute("SELECT * FROM courses WHERE course_id='{}'".format(course_id))
        course = cursor.fetchone()
        if student is not None and course is not None:
            try:
                conn = sqlite3.connect('db.db')
                conn.execute("INSERT INTO enrollment (student_id, course_id) values('{}','{}')".format(student_id, course_id))
                conn.commit()
                conn.close()
                return ("student enrolled successfully")
            except Exception as e:
                return e
        else:
            return ("check that you are a student and the course is available")
    except Exception as e:
        return e
    
def insertresults(student_id, course_id, test1, test2, test3, exam):
    total = test1 + test2 + test3 + exam
    try:
        conn = sqlite3.connect('db.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM student WHERE student_id='{}'".format(student_id))
        student = cursor.fetchone()
        cursor.execute("SELECT * FROM courses WHERE course_id='{}'".format(course_id))
        course = cursor.fetchone()
        conn.commit()
        conn.close()
        if student is not None and course is not None:
            try:
                conn = sqlite3.connect('db.db')
                conn.execute("INSERT INTO results (student_id, course_id, test1, test2, test3, exam, total) values('{}','{}','{}','{}','{}','{}','{}')".format(student_id, course_id, test1, test2, test3, exam, total))
                conn.commit()
                conn.close()
                return ("result insersed successfully")
            except Exception as e:
                return e
        else:
            return ("check that you are a student and you registered for this course")
    except Exception as e:
        return e
    
def updateresult(course_position, student_id, course_id):
    try:
        conn = sqlite3.connect('db.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM student WHERE student_id='{}'".format(student_id))
        student = cursor.fetchone()
        cursor.execute("SELECT exam FROM results WHERE student_id='{}' AND course_id='{}'".format(student_id, course_id))
        exam = cursor.fetchone()
        conn.commit()
        conn.close()
        if student is not None and exam is not None:
            try:
                conn = sqlite3.connect('db.db')
                conn.execute("UPDATE results SET course_position='{}' WHERE student_id='{}' AND course_id='{}'".format(course_position, student_id, course_id))
                conn.commit()
                conn.close()
                return ("course_position updated successfully")
            except Exception as e:
                return e
        else:
            return ("check that you are a student and you have writen exams for this course")
    except Exception as e:
        return e
   
    
def insertclassresult(student_id, total_score, class_position):
    try:
        conn = sqlite3.connect('db.db')
        conn.execute("INSERT INTO class_result (student_id, total_score, class_position) values('{}','{}','{}')".format(student_id, total_score, class_position))
        conn.commit()
        conn.close()
        return ("class_position inserted successfully")
    except Exception as e:
        return e
    
# print(insertstaff('Amadi solomon','mat','amadisolomon@gmail.com'))
# print(insertstaff('Comfort Abigail','eng','comfortabigail@gmail.com'))
# print(insertstaff('Buki Johnson','phy','bukijohnoson@gmail.com'))
# print(insertstaff('Badmos Kobe','chm','badmoskobe@gmail.com'))
# print(insertstaff('Ada Cynthia', 'geo', 'adacynthia@gmail.com'))
# print(insertstaff('Kofi Emmanuel','eco','kofiemmanuel@gmail.com'))
# print(insertcourse('Fmaths','further mathematics', 'instroduction to further mathematics', 6))
# print(insertenrollment(3,'mat'))
# print(insertresults(1,"phy", 20, 20, 20, 40))
# print(updateresult(1,1,'phy'))

