// function positioning(){
// 	//fetch positions from api
// 	var schools = [teams[0],teams[2], teams[4]]
// 	var positions = [92, 78, 67]
// 	document.getElementById('firstposition').innerHTML = "First Position = "+schools[0]+" with a total of "+ positions[0]+" points"
// 	document.getElementById('secondposition').innerHTML = "First Position = "+schools[1]+" with a total of "+ positions[1]+" points"
// 	document.getElementById('thirdposition').innerHTML = "First Position = "+schools[2]+" with a total of "+ positions[2]+" points"
// }

var teams = ['teamA', 'teamB', 'teamC', 'ckcc']

var score_data = {}
var sorted_data = {}
var sorted_scores_data = []


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
	var count = sorted_scores_data.length
	// for (let i = 1; i <= count; i++){
	// 	// var position = i + 1
	// 	document.getElementById("p"+ i).innerHTML = i + " position = " + sorted_scores_data[i-1]
	// }
	var j = 1;
	var m = 0
	while (j <= count){
		// for(let k = 1; k <= count; k++)
		var k = 0;

		while (k < count){
			if (sorted_scores_data[j-1] == score_data[teams[k]]){
				document.getElementById('p'+j).innerHTML = j + " position = "+ teams[j-1] + " with total score: " + score_data[teams[j-1]]*5+" points"
			}
			//use this to account for ties in the scores
			while (sorted_scores_data[j-1] == sorted_scores_data[j]){
				m = j + 1
				document.getElementById('p'+m).innerHTML = j + " position = "+ teams[j-1] + " with total score: " + score_data[teams[j-1]]*5+" points"
				j++
			}
			k++
		}

		j++
	}
	// alert("fine")
	// document.getElementById("p1").innerHTML = count
}