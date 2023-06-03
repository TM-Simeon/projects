var correctoption = ""
var question_number = 0
var phy_questions = {};
var eng_questions = {};
var counting = 0
var team = ''
var teams = ['teamA', 'teamB', 'teamC', 'teamD', 'ckcc']
var round2teams = []
var totalTeams = teams.length

var maths_questions = {}
async function get_questions_json(){
	var subject = document.getElementById('select_subject').value
	await get_questions(subject)
	for (let i = 1; i <= 20; i++){
		document.getElementById(i).style.background = '#c2d7f0'
	}

}
async function get_questions(subject){

	var data = {subject: subject}

	const response = await fetch("http://localhost:5000/get_questions",{
		method: 'POST',
		headers: {
			'Content-Type':'application/json'
		},
		body: JSON.stringify(data)
	})
	maths_questions = await response.json()
	// document.getElementById('time').innerHTML = maths_questions['1a']

}
	
let status = 0

function clicked(e){
	if (status == 0) {
		document.getElementById("instructions").innerHTML = " "
		status == 1
		
	}
	timer(25, 1000)
	// document.getElementByClassName("actualno")[0].id = e
	document.getElementById(e).style.background ='black'
	document.getElementById("question1").innerHTML = e +". " + maths_questions["question"+e]
	document.getElementById("optionA").innerHTML = "(a) " + maths_questions[e+"a"]
	document.getElementById("optionB").innerHTML = "(b) " + maths_questions[e+"b"]
	document.getElementById("optionC").innerHTML = "(c) " + maths_questions[e+"c"]
	document.getElementById("optionD").innerHTML = "(d) " + maths_questions[e+"d"]
	correctoption = maths_questions[e+"correct"]
	question_number = e

	document.getElementById("optionA").style.color = "black"
	document.getElementById("optionB").style.color = "black"
	document.getElementById("optionC").style.color = "black"
	document.getElementById("optionD").style.color = "black"
	document.getElementById("optionA").style.display = 'block'
	document.getElementById("optionB").style.display = 'block'
	document.getElementById("optionC").style.display = 'block'
	document.getElementById("optionD").style.display = 'block'

		team = teams[counting]
		counting += 1

	if (counting > totalTeams - 1){
		counting = 0

	}

	question(team)

}

function correct(option){
	var correct = correctoption
	if (option == correct){
		document.getElementById(option).style.color = 'green'
		answer(team, maths_questions['subject'], question_number, 1)

	}
	else {
		document.getElementById(option).style.color = 'red'
		answer(team, maths_questions['subject'], question_number, 0)

	}

}

function fiftyfifty(){
	// var current_question = question_number
	var correct_option = correctoption

	var count = 0
	var options = ["optionA","optionB","optionC", "optionD"]
	var wrongoptions = []
	//create a list of wrong options
	while (count <= 3){
		if (options[count] != correctoption)
		wrongoptions.push(options[count])
		count += 1
	}
	
	//choose a random number
	var randomNumber = Math.floor(Math.random(2))
	// select wrong options to remove from the list of wrong options
	document.getElementById(wrongoptions[randomNumber]).style.display = 'none'
	document.getElementById(wrongoptions[randomNumber+1]).style.display = 'none'
}



var downloadTimer = ""
//clear timer if another question is clicked before the time finishes
function clearRemainingTime(){
	clearInterval(downloadTimer)
}

function timer(start, stop){
	clearRemainingTime()

	var timeleft = start
	document.getElementById('time').style.color = 'green'

	downloadTimer = setInterval(function(){
		if(timeleft <= 0){
			clearInterval(downloadTimer)
			document.getElementById('time').innerHTML = 'Time up'
		}

		else{
			if(timeleft == 5){
			document.getElementById('time').style.color = 'red'
			document.getElementById('time').innerHTML = timeleft + ' sec'
			}
			document.getElementById('time').innerHTML = timeleft + ' sec'
		}
		timeleft -= 1
	}, stop)
}

async function question(team){


	var data = {name: 'joseph', team: team}

	const response = await fetch("http://localhost:5000/score",{
		method: 'POST',
		headers: {
			'Content-Type':'application/json'
		},
		body: JSON.stringify(data)
	})
	const responseData = await response.text();
	// console.log(responseData)
	document.getElementById('time').innerHTML = responseData
}

async function answer(team, subject, question_number, score){


	var data = {team: team, subject: subject, question_number: question_number, score: score}

	const response = await fetch("http://localhost:5000/insertscore",{
		method: 'POST',
		headers: {
			'Content-Type':'application/json'
		},
		body: JSON.stringify(data)
	})
	const responseData = await response.text();
	// console.log(responseData)
	document.getElementById('time').innerHTML = responseData
}





async function plotgraph(){
	var mylabels = teams
	var mydata = []
	//replace the data below with a fetch request to get scores from the api
	// var values = [55, 40, 40, 24, 35, 20, 25, 50, 22];

	// for (let i = 0; i < mylabels.length; i++){
	// 	mydata.push(values[i])
	// 	}
	await get_scores_json(mylabels)
	document.getElementById('time').innerHTML = " 1st "+ my_scores[teams[0]] * 5 +" 2nd "+ my_scores[teams[1]] +" 3rd "+ my_scores[teams[2]]+" 4th "+ my_scores[teams[3]]+" 5th "+ my_scores[teams[4]]
	for (let i = 0; i < mylabels.length; i++){
		mydata.push(my_scores[teams[i]] * 5)
		}
	// get_scores_json(mylabels)
	const data = {
	  labels: mylabels,
	  datasets: [
	    {
	      label: 'scores',
	      data: mydata,
	      backgroundColor: 'rgba(0, 123, 255, 0.5)',
	      borderColor: 'rgba(0, 123, 255, 1)',
	      borderWidth: 1
	    }
	  ]
	};

	const config = {
	  type: 'bar',
	  data: data,
	  options: {}
	};

	// Create the chart
	const myChart = new Chart(document.getElementById('myChart'), config);
}

async function plotgraph1(){
	var mylabels = round2teams
	var mydata = []
	//replace the data below with a fetch request to get scores from the api
	// var values = [55, 40, 40, 24, 35, 20, 25, 50, 22];

	// for (let i = 0; i < mylabels.length; i++){
	// 	mydata.push(values[i])
	// 	}
	await get_scores_json(mylabels)
	// document.getElementById('time').innerHTML = " 1st "+ my_scores[teams[0]] * 5 +" 2nd "+ my_scores[teams[1]]
	for (let i = 0; i < mylabels.length; i++){
		mydata.push(my_scores[round2teams[i]] * 5)
		}
	const data = {
	  labels: mylabels,
	  datasets: [
	    {
	      label: 'scores',
	      data: mydata,
	      backgroundColor: 'rgba(0, 123, 255, 0.5)',
	      borderColor: 'rgba(0, 123, 255, 1)',
	      borderWidth: 1
	    }
	  ]
	};

	const config = {
	  type: 'bar',
	  data: data,
	  options: {}
	};

	// Create the chart
	const myChart = new Chart(document.getElementById('myChart1'), config);
}


function positioning(){
	//fetch positions from api
	var schools = [teams[0],teams[2], teams[4]]
	var positions = [92, 78, 67]
	document.getElementById('firstposition').innerHTML = "First Position = "+schools[0]+" with a total of "+ positions[0]+" points"
	document.getElementById('secondposition').innerHTML = "First Position = "+schools[1]+" with a total of "+ positions[1]+" points"
	document.getElementById('thirdposition').innerHTML = "First Position = "+schools[2]+" with a total of "+ positions[2]+" points"
}

var my_scores = {}
async function get_scores_json(teams){
	// var teams = ['teamA','teamB','teamC']
	// var my_scores = {}

	await get_scores(teams)

	// var values = [55, 40, 40, 24, 35, 20, 25, 50, 22];

	// for (let i = 0; i < mylabels.length; i++){
	// 	mydata.push(values[i])
	// 	}

	// document.getElementById('time').innerHTML = "first "+ my_scores[teams[0]] * 5 +" second "+ my_scores[teams[1]] +" third "+ my_scores[teams[4]]


}
async function get_scores(teams){

	var data = {teams: teams}

	const response = await fetch("http://localhost:5000/get_scores",{
		method: 'POST',
		headers: {
			'Content-Type':'application/json'
		},
		body: JSON.stringify(data)
	})
	my_scores = await response.json()
	// document.getElementById('time').innerHTML = maths_questions['1a']

}

var my_sorted_scores = {}
var sorted_scores = []
async function get_sorted_scores(teams){

	var data = {teams: teams}

	const response = await fetch("http://localhost:5000/get_sorted_scores",{
		method: 'POST',
		headers: {
			'Content-Type':'application/json'
		},
		body: JSON.stringify(data)
	})
	my_sorted_scores = await response.json()
	// document.getElementById('time').innerHTML = maths_questions['1a']

}

async function round2_teams(){
	await get_sorted_scores(teams)
	sorted_scores = my_sorted_scores['scores']
	

}