from flask import Flask, redirect, url_for, render_template, request, flash, jsonify
from db import *

app = Flask(__name__)

number_of_teams = 0
count = 1

@app.route('/quiz')
def quiz():
	return render_template("quiz.html")

@app.route('/staff')
def staff():
	return render_template("staff.html")

@app.route('/staffinsert', methods=['GET','POST'])
def staffinsert():
	return render_template("staffinsert.html")

@app.route('/teams', methods=['GET', 'POST'])
def answer():
	data = request.get_json()
	teams = data['teams']
	number_of_teams = teams
	return "Number of teams inserted"

@app.route('/score', methods=['GET','POST'])
def score():
	data = request.get_json()
	name = data['name']
	team = data['team']
	return team

@app.route('/insertscore', methods=['GET','POST'])
def insertscore():
	data = request.get_json()
	team = data['team']
	subject = data['subject']
	question_number = data['question_number']
	score = data['score']

	try:
		conn = sqlite3.connect('db.db')
		conn.execute("INSERT INTO scores (team, subject, question_number, score) values('{}','{}','{}','{}')".format(team, subject, question_number, score))
		conn.commit()
		conn.close()
	except Exception as e:
		return "error"

	return team + " + " + str(score) + subject + str(question_number)

@app.route('/get_questions', methods=['GET','POST'])
def getquestions():
	data = request.get_json()
	subject = data['subject']
	# subject = "maths"
	try:
		conn = sqlite3.connect('db.db')
		cursor = conn.cursor()
		cursor.execute("SELECT * FROM questions WHERE subject='{}'".format(subject))
		results = cursor.fetchall()
		conn.commit()
		conn.close()
		results_json = {}
		results_json['subject'] = subject
		count = 1
		for row in results:
			results_json["question"+str(count)] = row[3]
			results_json[str(count)+"a"] = row[4]
			results_json[str(count)+"b"] = row[5]
			results_json[str(count)+"c"] = row[6]
			results_json[str(count)+"d"] = row[7]
			results_json[str(count)+"correct"] = row[8]
			count += 1
		print('i did print')
		return jsonify(results_json)
		# return "done inserting"
	except Exception as e:
		return str(e)

@app.route('/get_scores', methods=['GET','POST'])
def get_scores():
	data = request.get_json()
	teams = data['teams']

	scores_json = {}
	for team in teams:
		total = 0
		try:
			conn = sqlite3.connect('db.db')
			cursor = conn.cursor()
			cursor.execute("SELECT * FROM scores WHERE team='{}'".format(team))
			results = cursor.fetchall()
			conn.commit()
			conn.close()
			results_json = {}
			for row in results:
				# results_json["question"+str(count)] = row[3]
				total += row[3]
			scores_json['{}'.format(team)] = total
		except Exception as e:
			return str(e)
	return jsonify(scores_json)

@app.route('/get_sorted_scores', methods=['GET','POST'])
def get_sorted_scores():
	data = request.get_json()
	teams = data['teams']

	sorted_scores_list = []
	sorted_scores_json = {}
	for team in teams:
		total = 0
		try:
			conn = sqlite3.connect('db.db')
			cursor = conn.cursor()
			cursor.execute("SELECT * FROM scores WHERE team='{}'".format(team))
			results = cursor.fetchall()
			conn.commit()
			conn.close()
			results_json = {}
			for row in results:
				# results_json["question"+str(count)] = row[3]
				total += row[3]
			sorted_scores_list.append(total)
		except Exception as e:
			return str(e)
	# sort sorted_scores_list and return it
	bubbleSort(sorted_scores_list)
	sorted_scores_json['scores'] = sorted_scores_list
	return jsonify(sorted_scores_json)


@app.route('/test', methods=['GET','POST'])
def test():
	data =  request.get_json()
	teams = data['teams']
	return 'test completed'

@app.route('/insert_question', methods=['GET','POST'])
def insert_question():
	data = request.get_json()
	subject = data['subject']
	question_number = data['question_number']
	question_number = int(question_number) + 20
	question = data['question']
	optionA = data['optionA']
	optionB = data['optionB']
	optionC = data['optionC']
	optionD = data['optionD']
	correct = data['correct']


	try:
		conn = sqlite3.connect('db.db')
		cursor = conn.cursor()
		cursor.execute("INSERT INTO questions (subject, question_number, question, optionA, optionB, optionC, optionD,  correct) values('{}','{}','{}','{}','{}','{}','{}','{}')".format(subject, question_number, question, optionA, optionB, optionC, optionD, correct))
		results = cursor.fetchall()
		conn.commit()
		conn.close()
	except Exception as e:
		return str(e)
	
	return render_template("staffinsert.html")

if __name__ == '__main__':
	app.run()