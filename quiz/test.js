let myAudio = document.getElementById('audio')
myAudio.play()


let mysound = new Audio('song.mp3')

function playsound(){
  mysound.play()
}
function pausesound(){
  mysound.pause()
}

function stopsound(){
  mysound.pause()
  mysound.currentTime = 0
}