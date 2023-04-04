import sqlite3

conn = sqlite3.connect('db.db')
conn.execute('CREATE TABLE IF NOT EXISTS users (user_id INTEGER PRIMARY KEY AUTOINCREMENT, username text NOT NULL UNIQUE, password TEXT NOT NULL, email TEXT NOT NULL UNIQUE)')
conn.execute('CREATE TABLE IF NOT EXISTS student(student_id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER NOT NULL, first_name TEXT NUO NULL, last_name TEXT NOT NULL, email TEXT NOT NULL UNIQUE, FOREIGN KEY(user_id) REFERENCES users(user_id))')
conn.execute('CREATE TABLE IF NOT EXISTS courses (course_id INTEGER PRIMARY KEY NOT NULL UNIQUE, course_title TEXT NOT NULL UNIQUE, description TEXT NOT NULL)')
conn.execute('CREATE TABLE IF NOT EXISTS instructor(instructor_id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER NOT NULL, first_name TEXT NOT NULL, last_name TEXT NOT NULL, email TEXT NOT NULL UNIQUE, FOREIGN KEY (user_id) REFERENCES users(user_id))')
conn.execute('CREATE TABLE IF NOT EXISTS enrollment (enrollment_id INTEGER PRIMARY KEY AUTOINCREMENT, student_id INTEGER NOT NULL, course_id INTEGER NOT NULL, FOREIGN KEY (student_id) REFERENCES student(student_id), FOREIGN KEY (course_id) REFERENCES courses(course_id))')
conn.commit()
conn.close()

def fetchdata(table, key, value):
    try:
        conn = sqlite3.connect('db.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM {} WHERE {} = "{}"'.format(table, key, value))
        # cursor.execute("select * from users where email='email1'")
        data = cursor.fetchone()
        conn.close()
        return data
    except Exception as e:
        return e

def fetchdataall(table, key, value):
    try:
        conn = sqlite3.connect('db.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM {} WHERE {} = "{}"'.format(table, key, value))
        # cursor.execute("select * from users where email='email1'")
        data = cursor.fetchall()
        conn.close()
        return data
    except Exception as e:
        return e


def insertuser(name, password, emaildata):
    try:
        results = fetchdata("users", "email", emaildata)
        if results is None:
            results2 = fetchdata("users", "username", name)
            if results2 is None:
                conn = sqlite3.connect('db.db')
                cursor = conn.cursor()
                cursor.execute("INSERT INTO users(username, password, email) VALUES('{}','{}','{}')".format(name, password, emaildata))
                conn.commit()
                conn.close()
                return "user {} created successfully".format(emaildata)
            else:
                return "user already exist with the username: {}".format(name)
        else:
            return "user already exist with the email: {}".format(results[3])
    
    except Exception as e:
        return e

def insertStudent(emaildata, first_name, last_name):
    try:
        results = fetchdata("users", "email", emaildata)
        if results is None:
            return "sorry {}, you have to register as a user before you can register as a student!".format(first_name)
        conn = sqlite3.connect('db.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO student (user_id, first_name, last_name, email) VALUES({},'{}','{}','{}');".format(results[0], first_name, last_name, results[3]))
        conn.commit()
        conn.close()
        print('{}, you have registered as a student'.format(emaildata))
    
    except Exception as err:
        return err

def insertCourse(course_id, course_title, description):
    # check courses to see that course_id and course_title dont already exist
    try:
        results = fetchdata("courses","course_id", course_id)
        results2 = fetchdata("courses","course_title", course_title)
        if results is not None:
            if results[0] == course_id:
                return "A course already exist with the id: {}".format(course_id)
            elif results[1] == course_title:
                return "A course already exist with the title: {}".format(course_title)
        elif results2 is not None:
            if results2[0] == course_id:
                return "A course already exist with the id: {}".format(course_id)
            elif results2[1] == course_title:
                return "A course already exist with the title: {}".format(course_title)
        else:
            conn = sqlite3.connect('db.db')
            cursor = conn.cursor()
            cursor.execute("INSERT INTO courses (course_id, course_title, description) VALUES('{}','{}','{}')".format(course_id, course_title, description))
            conn.commit()
            conn.close()
            return "{} inserted successfully".format(course_title)
        
    except Exception as e:
        return e
# conn.execute('CREATE TABLE IF NOT EXISTS instructor(instructor_id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER NOT NULL, first_name TEXT NOT NULL, last_name TEXT NOT NULL, email TEXT NOT NULL UNIQUE, FOREIGN KEY (user_id) REFERENCES users(user_id))')

def insertInstructor(first_name, last_name, emaildata):
    #check that user already exist and retrieve user_id and email
    try:
        results = fetchdata("users", "email", emaildata)
        if results is None:
            return "sorry {}, you have to register as a user before you can register as an instructor!".format(first_name)
        results2 = fetchdata("instructor","email", emaildata)
        if results2 is not None:
            return "an instructor already exist with the email {}".format(emaildata)
        conn = sqlite3.connect('db.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO instructor (user_id, first_name, last_name, email) VALUES({},'{}','{}','{}');".format(results[0], first_name, last_name, results[3]))
        conn.commit()
        conn.close()
        return '{}, you have registered as an instructor'.format(emaildata)
    
    except Exception as e:
        return e
# conn.execute('CREATE TABLE IF NOT EXISTS enrollment (enrollment_id INTEGER PRIMARY KEY AUTOINCREMENT, student_id INTEGER NOT NULL, course_id INTEGER NOT NULL, FOREIGN KEY (student_id) REFERENCES student(student_id), FOREIGN KEY (course_id) REFERENCES courses(course_id))')

def insertEnrollment(student_id, course_id, emaildata):
    # check and retrieve student_id from student table
    # check and retrieve course_id from course table
    
    try:
        results = fetchdata("student","email", emaildata)
        results2 = fetchdataall("enrollment", "email", emaildata)
        results3 = fetchdata("course","course_id", course_id)
        if results is None:
            return "sorry {}, you can only enroll for a course if you are a student".format(emaildata)
        if results2 is not None:
            for row in results2:
                if row[2] == course_id:
                    return "{}, you are already registered for this course".format(emaildata)
        if results3 is None:
            return "sorry {}, this course is not available for the moment"
        conn = sqlite3.connect('db.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO enrollment (student_id, course_id) VALUES('{}','{}')".format(student_id, course_id))
        conn.commit()
        conn.close()
        return "course inserted successfully"
    
    except Exception as e:
        return e 


# print(insertuser("blessing111","nguemo",'blessingnguemo111@gmail.com'))
# print(insertInstructor("blessing111","nguemo",'blessingnguemo111@gmail.com'))
print(insertEnrollment("23","introduction to chemical engineering","simeon@gmail.com"))