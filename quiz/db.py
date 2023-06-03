import sqlite3
# from sort import bubbleSort

# create database  DO NOT DELETE THIS COMMENTS, WE USE IT TO CREATE TABLES THEN COMMENT IT OUT TO IMPROVE SPEED
conn = sqlite3.connect('db.db')
conn.execute('CREATE TABLE IF NOT EXISTS questions (ques_id INTEGER PRIMARY KEY AUTOINCREMENT, subject TEXT NOT NULL, question_number INTEGER NOT NULL, question TEXT NOT NULL, optionA TEXT NOT NULL, optionB TEXT NOT NULL, optionC TEXT NOT NULL, optionD TEXT NOT NULL, correct TEXT NOT NULL, UNIQUE(question_number))')
conn.execute('CREATE TABLE IF NOT EXISTS scores ( team TEXT NOT NULL, subject TEXT NOT NULL, question_number INTEGER NOT NULL, score INTEGER NOT NULL,  FOREIGN KEY (question_number) REFERENCES questions(question_number))')
conn.commit()
conn.close()

# def insertstaff(name, course_id, email):
#     try:
#         conn = sqlite3.connect('db.db')
#         conn.execute("INSERT INTO staff (name, course_id, email) values('{}','{}','{}')".format(name, course_id, email))
#         conn.commit()
#         conn.close()
#         return ("staff inserted successfully")
#     except Exception as e:
#         return e

def bubbleSort(arr):

	n =  len(arr)

	for i in range(n):
		for j in range(0, n - i - 1):
			if arr[j] < arr[j + 1]:
				arr[j], arr[j + 1] = arr[j+1], arr[j]