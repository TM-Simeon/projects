var correctoption = ""
var question_number = 0
var phy_questions = {};
var eng_questions = {};
var counting = 0
var team = ''
var teams = ['teamA', 'teamB', 'teamC', 'teamD', 'skcc']
var totalTeams = teams.length

var maths_questions = {
	"question1": "The distribution of electrons into the energy levels or sublevels of an atom is called...",
	"1a": "electric transfer",
	"1b": "electronic transfer",
	"1c": "electronic configuration",
	"1d": "electronic circuit",
	"1correct":"optionC",
	"question2": "what do we have here, lets actually put more than that here?",
	"2a": "nothing",
	"2b": "something small",
	"2c": "something",
	"2d": "something big",
	"2correct": "optionA",
	"question3":"superlions scored TWO goals in the first half",
	"3instructions":"put instructions here",
	"3a":"Did superLions score any goal in the second half?",
	"3b":"Did superStars score any goal in the first half?",
	"3c":"Did superLions score any goal in the first half?",
	"3d":"Did superLions score any goal at all?",
	"3correct":"optionC"
	
};
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
	question_number == e

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
	}
	else {
		document.getElementById(option).style.color = 'red'
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

// fetch("http://localhost:5000/test")
// 	.then(response => response.text())
// 	.then(data => document.getElementById('time').innerHTML = data)

// var data = {name: 'joseph', email: 'joseph1@gmail.com'}

// fetch("http://localhost:5000/score", {
// 	method: 'POST',
// 	headers: {
// 		'Content-Type': 'application/json'
// 	},
// 	body: JSON.stringify(data)
// })
// 	.then(response => response.text())
// 	.then(data => document.getElementById('time').innerHTML = data)
// 	.catch(error => document.getElementById('time').innerHTML = error);



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