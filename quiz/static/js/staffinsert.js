// async function data_for_insert_question(){
// 	var subject = document.getElementById("subject").value
// 	var question_number = document.getElementById("question_number").value
// 	var question = document.getElementById("question").value
// 	var optionA = document.getElementById("optionA").value
// 	var optionB = document.getElementById("optionB").value
// 	var optionC = document.getElementById("optionC").value
// 	var optionD = document.getElementById("optionD").value
// 	var correct = "option"+document.getElementById("answer").value

// 	var data = {
// 		subject: subject,
// 		question_number: question_number,
// 		question: question,
// 		optionA: optionA,
// 		optionB:optionB,
// 		optionC: optionC,
// 		optionD: optionD,
// 		correct_option: correct_option
// 	}

// 	await insert_questions(data)


// }

var text = ""
async function insert_question(){
	var subject = document.getElementById("subject").value
	var question_number = document.getElementById("question_number").value
	var question = document.getElementById("question").value
	var optionA = document.getElementById("optionA").value
	var optionB = document.getElementById("optionB").value
	var optionC = document.getElementById("optionC").value
	var optionD = document.getElementById("optionD").value
	var correct = "option"+document.getElementById("answer").value

	var data = {
		subject: subject,
		question_number: question_number,
		question: question,
		optionA: optionA,
		optionB:optionB,
		optionC: optionC,
		optionD: optionD,
		correct: correct
	}

	// var data = {teams: teams}

	const response = await fetch("http://localhost:5000/insert_question",{
		method: 'POST',
		headers: {
			'Content-Type':'application/json'
		},
		body: JSON.stringify(data)
	})
	text = await response.text()

	const refresh = document.getElementById('insert_q')
	refresh.addEventListener('click', function(event){
		event.preventDefault();
		location.reload();
	})

}