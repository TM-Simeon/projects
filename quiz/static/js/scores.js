// function positioning(){
// 	//fetch positions from api
// 	var schools = [teams[0],teams[2], teams[4]]
// 	var positions = [92, 78, 67]
// 	document.getElementById('firstposition').innerHTML = "First Position = "+schools[0]+" with a total of "+ positions[0]+" points"
// 	document.getElementById('secondposition').innerHTML = "First Position = "+schools[1]+" with a total of "+ positions[1]+" points"
// 	document.getElementById('thirdposition').innerHTML = "First Position = "+schools[2]+" with a total of "+ positions[2]+" points"
// }

var teams = ['team1', 'team2', 'team3', 'team4','team5','team6','team7','team8','team9','team10']

var score_data = {}
var sorted_data = {}
var sorted_scores_data = []
var sorted_scores_position = {}


async function get_scores_data(teams){

	var data = {teams: teams}

	const response = await fetch("http://localhost:5000/get_scores",{
		method: 'POST',
		headers: {
			'Content-Type':'application/json'
		},
		body: JSON.stringify(data)
	})
	score_data = await response.json()

}

async function get_sorted_data(teams){

	var data = {teams: teams}

	const response = await fetch("http://localhost:5000/get_sorted_scores",{
		method: 'POST',
		headers: {
			'Content-Type':'application/json'
		},
		body: JSON.stringify(data)
	})
	sorted_data = await response.json()
	// document.getElementById('time').innerHTML = maths_questions['1a']

}

async function positions(){
	await get_scores_data(teams)
	await get_sorted_data(teams)
	sorted_scores_data = sorted_data['scores']
	sorted_scores_position = sorted_data['positions']
	var count = sorted_scores_data.length
	// document.getElementById('p1').innerHTML = sorted_scores_position[sorted_scores_data[3]]
	for(let i = 0; i< teams.length; i++){
		var positionDiv = document.getElementById('positions');
		var h1_1 = document.createElement("h3");
		var text1 = document.createTextNode(teams[i]+": position = " +sorted_scores_position[score_data[teams[i]]]+" with a total of "+score_data[teams[i]]*5+" points");
		h1_1.appendChild(text1);
		positionDiv.appendChild(h1_1);
	}
}

// function findteam()