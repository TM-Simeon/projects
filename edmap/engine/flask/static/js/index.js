const swiper = new Swiper('.swiper', {
  // Optional parameters
  // direction: 'vertical',
  autoplay: {
    delay: 3000,
    disableOnInteraction: false,
  },
  loop: true,

  // If we need pagination
  pagination: {
    el: '.swiper-pagination',
    clickable: true,
  },

  // Navigation arrows
  navigation: {
    nextEl: '.swiper-button-next',
    prevEl: '.swiper-button-prev',
  },

  // And if we need scrollbar
  // scrollbar: {
  //   el: '.swiper-scrollbar',
  // },
});

window.addEventListener("scroll", function(event){
  var scroll = this.scrollY;
  if(scroll > 100){
    document.getElementById("ontop").style.backgroundColor = "#d6b38b";
  }
  else{
    document.getElementById("ontop").style.backgroundColor = "transparent";
  }
  // console.log("here");
});