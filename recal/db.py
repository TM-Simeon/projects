import sqlite3
from sort import bubbleSort

# create database  DO NOT DELETE THIS COMMENTS, WE USE IT TO CREATE TABLES THEN COMMENT IT OUT TO IMPROVE SPEED
# conn = sqlite3.connect('db.db')
# conn.execute('CREATE TABLE IF NOT EXISTS staff (staff_id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, course_id TEXT NOT NULL, email TEXT NOT NULL, UNIQUE(name, email, course_id))')
# conn.execute('CREATE TABLE IF NOT EXISTS student(student_id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, email TEXT NOT NULL UNIQUE, department TEXT NOT NULL)')
# conn.execute('CREATE TABLE IF NOT EXISTS courses (course_id TEXT PRIMARY KEY NOT NULL UNIQUE, course_title TEXT NOT NULL UNIQUE, description TEXT NOT NULL, staff_id INTEGER NOT NULL, FOREIGN KEY (staff_id) REFERENCES staff(staff_id))')
# conn.execute('CREATE TABLE IF NOT EXISTS enrollment (enrollment_id INTEGER PRIMARY KEY AUTOINCREMENT, student_id INTEGER NOT NULL, course_id TEXT NOT NULL, UNIQUE(student_id, course_id) FOREIGN KEY (student_id) REFERENCES student(student_id), FOREIGN KEY (course_id) REFERENCES courses(course_id))')
# conn.execute('CREATE TABLE IF NOT EXISTS results (student_id INTEGER NOT NULL, course_id TEXT NOT NULL, test1 INTEGER, test2 INTEGER, test3 INTERGER, exam INTEGER, total INTEGER, course_position INTEGER, UNIQUE(student_id, course_id), FOREIGN KEY (student_id) REFERENCES student(student_id) FOREIGN KEY (course_id) REFERENCES courses(course_id))')
# conn.execute('CREATE TABLE IF NOT EXISTS class_result (student_id INTEGER NOT NULL UNIQUE, total_score INTEGER NOT NULL, class_position INTEGER, department TEXT NOT NULL,  FOREIGN KEY (student_id) REFERENCES student(student_id))')
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

def insertstudent(name, email, department):
    try:
        conn = sqlite3.connect('db.db')
        conn.execute("INSERT INTO student (name, email, department) values('{}','{}','{}')".format(name, email, department))
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
    
def insertclassresult(student_id, total_score, department):
    try:
        conn = sqlite3.connect('db.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM student WHERE student_id='{}'".format(student_id))
        student = cursor.fetchone()
        cursor.execute("SELECT total FROM results WHERE student_id='{}'".format(student_id))
        total = cursor.fetchone()
        conn.commit()
        conn.close()
        if student is not None and total is not None:
            try:
                conn = sqlite3.connect('db.db')
                conn.execute("INSERT INTO class_result (student_id, total_score, department) values('{}','{}','{}')".format(student_id, total_score, department))
                conn.commit()
                conn.close()
                return ("class_position inserted successfully")
            except Exception as e:
                return e
        else:
            return ("check that you are a student and you have writen exams for this course")
    except Exception as e:
        return e
            
def callfunction():    
    # print(insertstaff('Amadi solomon','mat','amadisolomon@gmail.com'))
    # print(insertstaff('Comfort Abigail','eng','comfortabigail@gmail.com'))
    # print(insertstaff('Buki Johnson','phy','bukijohnoson@gmail.com'))
    # print(insertstaff('Badmos Kobe','chm','badmoskobe@gmail.com'))
    # print(insertstaff('Ada Cynthia', 'geo', 'adacynthia@gmail.com'))
    # print(insertstaff('Kofi Emmanuel','eco','kofiemmanuel@gmail.com'))
    # print(insertcourse('Fmaths','further mathematics', 'instroduction to further mathematics', 6))
    # print(insertenrollment(3,'mat'))
    # print(insertresults(1,"phy", 20, 20, 20, 40))


    # print(insertstudent('Mnaan Simeon','mnaansimeon@gmail.com','science'))
    # print(insertstudent('Nonso Obinna','nonsoobinna@gmail.com','science'))
    # print(insertstudent('Okolo Chidimma','okolochidimma@gmail.com', 'arts'))
    # print(insertstudent('Iwueseter Josephine','iwueseterjosephine@gmail.com', 'commercial'))
    # print(insertstudent('Alkali Gabriel','alkaligabriel@gmail.com', 'science'))
    # print(insertstudent('Ubi Paulinus1','ubipaulinus1@gmail.com', 'commercial'))
    print(insertstudent('Comfort Simeon','comfortsimeon@gmail.com','science'))
    print(insertstudent('Abutu Terdoo','abututerdoo@gmail.com','science'))
    print(insertstudent('Aboki Cousin','abokicousin@gmail.com','science'))
    print(insertstudent('Ogun Emmanuel','ogunemmanuel@gmail.com','science'))
    print(insertstudent('Lukeman Desmond','lukemandesmond@gmail.com','science'))
    print(insertstudent('Peter Okwe','peterokwe@gmail.com','science'))
    
    
    # print(calresults('arts'))
    # print("----------------")
    # print(calresults('science'))
    # print("----------------")
    # print(calresults('commercial'))


    # print(insertresults(1,'eng',29,15,17,34))
    # print(insertresults(1,'eng',19,18,12,32))
    # print(insertresults(2,'phy',19,18,12,32))
    # print(insertresults(6,'geo',19,15,12,32))
    # print(insertresults(7,'phy',29,15,17,34))
    # print(insertresults(8,'eng',19,18,12,32))
    # print(insertresults(9,'phy',19,18,12,32))
    # print(insertresults(9,'geo',19,15,12,32))
    # print(insertresults(12,'phy',19,15,12,24))
    
    
    # course_position('science')
    # course_position('commercial')
    
    # pass

#calculating results: pass in the department to compute the results for that department and insert into the class_result table
def calresults(department):
    try:
        conn = sqlite3.connect('db.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM student WHERE department='{}'".format(department))
        student = cursor.fetchone()
        # print(student)
        total = None
        if student is not None:
            student_id = student[0]
            cursor.execute("SELECT total FROM results WHERE student_id='{}'".format(student_id))
            total = cursor.fetchone()
            conn.commit()
            conn.close()
        else:
            return ("no student is offering this course")
        
        # return ("passed")
        if student is not None and total is not None:
            try:
                conn = sqlite3.connect('db.db')
                cursor = conn.cursor()
                cursor.execute("SELECT student_id FROM student WHERE department='{}'".format(department))
                students = cursor.fetchall()
                conn.commit()
                conn.close()
                for row in students:
                    student_id = row[0]
                    conn = sqlite3.connect('db.db')
                    cursor = conn.cursor()
                    cursor.execute("SELECT total FROM results WHERE student_id='{}'".format(student_id))
                    total = cursor.fetchall()
                    conn.commit()
                    conn.close()
                    overall = 0
                    for row in total:
                        overall += row[0]
                    try:
                        insertclassresult(student_id,overall,department)
                        # return ("students results inserted successfully")
                        
                    except Exception as e:
                        return e
                    
                    # print("overall score for {} is: {}".format(student_id, overall))
            except Exception as e:
                return e
        else:
            return ("No student wrote exams for this course")
    except Exception as e:
        return e

def calcourseposition(course_id):
    try:
        conn = sqlite3.connect('db.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM enrollment WHERE course_id='{}'".format(course_id))
        course = cursor.fetchone()
        total = None
        if course is not None:
            # student_id = student[0]
            cursor.execute("SELECT total FROM results WHERE course_id='{}'".format(course_id))
            total = cursor.fetchall()
            conn.commit()
            conn.close()
        else:
            conn.commit()
            conn.close()
            return ("no student is offering this course")
        
        # return ("passed")
        # print(total)
        if course is not None and total is not None:
          
            resultarray = []
            for row in total:
                # print(row[0])
                resultarray.append(row[0])
                bubbleSort(resultarray)
                # print(resultarray)
                n = len(resultarray) - 1
                positionties = 0
                position = 1
            while n >= 0:
                score = resultarray[n]
                conn = sqlite3.connect('db.db')
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM results WHERE course_id='{}' AND total='{}'".format(course_id, score))
                scores = cursor.fetchall()
                #insert position n in database
                cursor.execute("UPDATE results SET course_position='{}' WHERE total='{}' AND course_id='{}'".format(position,score, course_id))
                conn.commit()
                conn.close()
                positionties = len(scores)
                n -= positionties
                position += positionties
                    # print("overall score for {} is: {}".format(student_id, overall))
            # except Exception as e:
            #     return e
        else:
            return ("No student wrote exams for this course")
    except Exception as e:
        return e
#sort results and alocate positions to student
def class_position(department):
    try:
        conn = sqlite3.connect('db.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM class_result WHERE department='{}'".format(department))
        results = cursor.fetchall()
        # print(results)
        conn.commit()
        conn.close()
        resultarray = []
        for row in results:
            resultarray.append(row[1])
        bubbleSort(resultarray)
        # print(resultarray)
        n = len(resultarray) - 1
        positionties = 0
        position = 1
        while n >= 0:
            score = resultarray[n]
            conn = sqlite3.connect('db.db')
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM class_result WHERE department='{}' AND total_score='{}'".format(department, score))
            scores = cursor.fetchall()
            #insert position n in database
            cursor.execute("UPDATE class_result SET class_position='{}' WHERE total_score='{}' AND department='{}'".format(position,score, department))
            conn.commit()
            conn.close()
            positionties = len(scores)
            n -= positionties
            position += positionties
    except Exception as e:
        return e

def getstudentresults(student_id):
    results = {}
    try:
        conn = sqlite3.connect('db.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM results WHERE student_id='{}'".format(student_id))
        courseresults = cursor.fetchall()
        cursor.execute("SELECT * FROM class_result WHERE student_id='{}'".format(student_id))
        classresults = cursor.fetchone()
        cursor.execute("SELECT department, name FROM student WHERE student_id='{}'".format(student_id))
        studentdata = cursor.fetchone()
        conn.close()
        if courseresults is not None and classresults is not None and studentdata is not None:
            results['Name'] = studentdata[1]
            results["Department"] = studentdata[0]
            courses = []
            for row in courseresults:
                courses.append(row[1])
                results[row[1]] = {"test1":row[2], "test2": row[3], "test3": row[4], "exam": row[5], "total": row[6], "course_position": row[7]}
            results["overall total"] = classresults[1]
            results["class position"] = classresults[2]
            return courses, results
        else:
            department = studentdata[0]
            name = studentdata[1]
            # return "No result compiled for {} of {} department".format(name, department)
            return {"Report" : "No result compiled for {} of {} department".format(name, department)}
            
    except Exception as e:
        return e
# callfunction()
# calresults('science')
# calresults('commercial')
# class_position('science')
# class_position('commercial')
# calcourseposition('phy')
# calcourseposition('eng')
# calcourseposition('geo')
# calcourseposition('eco')
# calcourseposition("mat")
# course, result = getstudentresults(1)
# print(len(course))
# print(result['eng']['test1'])
# print(course[0])
# for row in getstudentresults(2).items():
#     print(row)
# print(getstudentresults(3))