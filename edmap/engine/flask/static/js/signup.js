const myname = document.getElementById('inputname')
const email = document.getElementById('inputemail')
const password = document.getElementById('inputpassword')
const form = document.getElementById('login')
let errorElement = document.getElementById('error')



form.addEventListener('submit', (e) =>{
    let messages = []
    if (myname.value === '' || myname.value == null){
        // messages.push('Name is required')
        e.preventDefault()
        errorElement.innerText = "Name is required!"
        // errorElement.style.color = "green"
    }
    else if (email.value == '' || email.value == null){
        // messages.push('email is required')
        e.preventDefault()
        errorElement.innerText = "Email is required!"
        
    }
    else if (password.value === '' || password.value == null){
        // messages.push('password is required')
        e.preventDefault()
        errorElement.innerText = "Password is required!";
        // errorElement.style.color = "green";
    }
    else {
        errorElement.style.color = "green"
        errorElement.innerText = "Proceed to login"
    }

})
