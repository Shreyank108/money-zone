
var user_dash=document.querySelector("#user_dash")

document.querySelector("#affli").addEventListener('click',function(){ 
    user_dash.style.display="block"
})

var cancel =document.querySelector("#dashcancel")
cancel.addEventListener('click',function(){ 
    user_dash.style.display='none'
})

document.querySelector("#certi h3").addEventListener('click',function(){ 
    document.querySelector("#certi").style.display="none";
})
document.querySelector("#cert").addEventListener('click',function(){ 
    document.querySelector("#certi").style.display="block";
})