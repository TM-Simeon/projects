// function login(){
// 	window.location.href=dashboard.assign("dashboard")
// }


const email = document.getElementById('inputemail')
const password = document.getElementById('inputpassword')
const form = document.getElementById('login')
let errorElement = document.getElementById('error')



form.addEventListener('submit', (e) =>{
    let messages = []
  
    if (email.value == '' || email.value == null){
        // messages.push('email is required')
        e.preventDefault()
        errorElement.innerText = "Email is required!"
		errorElement.style.color = "red"
        
    }
    else if (password.value === '' || password.value == null){
        // messages.push('password is required')
        e.preventDefault()
        errorElement.innerText = "Password is required!"
        errorElement.style.color = "red"
    }
    else {
        errorElement.style.color = "green"
        errorElement.innerText = "Login Processing"
    }

})