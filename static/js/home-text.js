// Wrap every letter in a span
// var textWrapper = document.querySelector('.ml11 .letters');
// textWrapper.innerHTML = textWrapper.textContent.replace(/([^\x00-\x80]|\w)/g, "<span class='letter'>$&</span>");

// anime.timeline({loop: false})
//   .add({
//     targets: '.ml11 .line',
//     scaleY: [0,1],
//     opacity: [0.5,1],
//     easing: "easeOutExpo",
//     duration: 700
//   })
//   .add({
//     targets: '.ml11 .line',
//     translateX: [0, document.querySelector('.ml11 .letters').getBoundingClientRect().width + 10],
//     easing: "easeOutExpo",
//     duration: 700,
//     delay: 100
//   }).add({
//     targets: '.ml11 .letter',
//     opacity: [0,1],
//     easing: "easeOutExpo",
//     duration: 600,
//     offset: '-=775',
//     delay: (el, i) => 34 * (i+1)
//   }).add({
//     targets: '.ml11',
//     opacity: 0,
//     duration: 1000,
//     easing: "easeOutExpo",
//     delay: 50000
//   });



  //aboutpage//
  




function autoType(elementClass, typingSpeed){
  var thhis = $(elementClass);
  thhis.css({
    "position": "relative",
    "display": "inline-block"
  });
  thhis.prepend('<div class="cursor" style="right: initial; left:0;"></div>');
  thhis = thhis.find(".text-js");
  var text = thhis.text().trim().split('');
  var amntOfChars = text.length;
  var newString = "";
  thhis.text("|");
  setTimeout(function(){
    thhis.css("opacity",1);
    thhis.prev().removeAttr("style");
    thhis.text("");
    for(var i = 0; i < amntOfChars; i++){
      (function(i,char){
        setTimeout(function() {        
          newString += char;
          thhis.text(newString);
        },i*typingSpeed);
      })(i+1,text[i]);
    }
  },1500);
}

$(document).ready(function(){
  // Now to start autoTyping just call the autoType function with the 
  // class of outer div
  // The second paramter is the speed between each letter is typed.   
  autoType(".type-js",200);
});