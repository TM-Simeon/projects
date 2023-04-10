const email = document.getElementById('inputemail')
const form = document.getElementById('login')
const selectLevel = document.getElementById('selectLevel')
let errorElement = document.getElementById('error')



form.addEventListener('submit', (e) =>{
    let messages = []
  
    if (email.value == '' || email.value == null){
        // messages.push('email is required')
        e.preventDefault()
        errorElement.innerText = "Email is required!"
		errorElement.style.color = "red"
        
    }
    else if (selectLevel.selectedIndex == 0){
        // messages.push('password is required')
        e.preventDefault()
        errorElement.innerText = "Please select level!"
        errorElement.style.color = "red"
    }
    else {
        errorElement.style.color = "green"
        errorElement.innerText = "Proceed to Login"
    }

})