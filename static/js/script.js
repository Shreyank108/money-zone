// gsap.fromTo('child',{
// scrollTrigger:{
//     trigger:'parent',
//     scrub:true,
//     markers:true,
//     start:'top 50%',
//     end:'top 0%',
// },
// })

// page 2 animations
window.addEventListener("resize", function () {
  "use strict";
  window.location.reload();
});
function init() {
  gsap.registerPlugin(ScrollTrigger);
  const locoScroll = new LocomotiveScroll({
    el: document.querySelector("#main"),
    smooth: true,
  });
  locoScroll.on("scroll", ScrollTrigger.update);
  ScrollTrigger.scrollerProxy("#main", {
    scrollTop(value) {
      return arguments.length
        ? locoScroll.scrollTo(value, 0, 0)
        : locoScroll.scroll.instance.scroll.y;
    },
    getBoundingClientRect() {
      return {
        top: 0,
        left: 0,
        width: window.innerWidth,
        height: window.innerHeight,
      };
    },
    pinType: document.querySelector("#main").style.transform
      ? "transform"
      : "fixed",
  });
  ScrollTrigger.addEventListener("refresh", () => locoScroll.update());
  ScrollTrigger.refresh();
}
init();
var tl = gsap.timeline();
tl.to("#page2", {
  scrollTrigger: {
    trigger: "#page1",
    scroller: "#main",
    pin: true,
    scrub: true,
  },
  width: "100%",
  top: "0%",
  height: "100vh",
});
// page 2 animations ended
// nav ki katha
// Setting up the Variables
var bars = document.getElementById("nav-action");
var nav = document.getElementById("nav");

//setting up the listener
bars.addEventListener("click", barClicked, false);

//setting up the clicked Effect
function barClicked() {
  bars.classList.toggle("active");
  nav.classList.toggle("visible");
}

// nav ki katha ka nth
var ul = document.querySelector("#cont1-box ul");
var ul2 = document.querySelector("#cont2-box ul");
var ul3 = document.querySelector("#cont3-box ul");
var cont1_box = document.querySelector("#cont1-box");
document.querySelector("#cont1").addEventListener("click", function () {
  cont1_box.style.display = "block";
  ul.style.color = "white";
  cont1_box.style.zIndex = 99;
  cont1_box.style.filter = "drop-shadow(5px 0px 15px orange)";
});
var cancel = document
  .querySelector("#cancel1")
  .addEventListener("click", function () {
    cont1_box.style.display = "none";
    ul.style.color = "transparent";
  });

var cont2_box = document.querySelector("#cont2-box");
document.querySelector("#cont2").addEventListener("click", function () {
  cont2_box.style.display = "block";
  ul2.style.color = "white";
  cont2_box.style.zIndex = 99;
  cont2_box.style.filter = "drop-shadow(5px 0px 15px orange)";
});
var cancel2 = document
  .querySelector("#cancel2")
  .addEventListener("click", function () {
    cont2_box.style.display = "none";
    ul2.style.color = "transparent";
  });

var cont3_box = document.querySelector("#cont3-box");
document.querySelector("#cont3").addEventListener("click", function () {
  cont3_box.style.display = "block";
  cont3_box.style.zIndex = 99;
  ul3.style.color = "white";
  cont3_box.style.filter = "drop-shadow(5px 0px 15px orange)";
});
var cancel3 = document
  .querySelector("#cancel3")
  .addEventListener("click", function () {
    cont3_box.style.display = "none";
    ul3.style.color = "transparent";
  });
var page4 = document.querySelector("#page4");
var log2 = document.querySelector("#log2");
var duo2 = document.querySelector("#duo2");
var account = document.querySelector("#account1");
account.addEventListener("click", function () {
  page4.style.display = "block";
});
var cancel1 = document.querySelector("#can1");
cancel1.addEventListener("click", function () {
  page4.style.display = "none";
});

var cancel2 = document.querySelector("#can2");
cancel2.addEventListener("click", function () {
  page4.style.display = "none";
});

var dont = document.querySelector("#dont");
var already = document.querySelector("#already");
dont.addEventListener("click", function () {
  log2.style.zIndex = -1;
  duo2.style.zIndex = 99;
});
already.addEventListener("click", function () {
  duo2.style.zIndex = -1;
  log2.style.zIndex = 99;
});

var upper = document.querySelector("#up");

upper.addEventListener("click", function () {
  document.querySelector("#pokbox").style.display = "block";
});

var don = document.querySelector("#cancelne");
don.addEventListener("click", function () {
  document.querySelector("#pokbox").style.display = "none";
});
