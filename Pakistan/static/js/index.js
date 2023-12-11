const carouselItems = document.querySelectorAll(".carousel-item");
let currentItem = 0;
setInterval(() => {
    if (currentItem >= carouselItems.length - 1) {
        currentItem = 0;
    } else {
        currentItem++;
    }
    carouselItems.forEach((item) => {
        item.classList.remove("active");
    });
    carouselItems[currentItem].classList.add("active");
}, 3000);
function showDiv(divNumber) {
    var div1 = document.getElementById('div1');
    var div2 = document.getElementById('div2');
    var div3 = document.getElementById('div3');

    if (divNumber === 1) {
        div1.style.display = 'block';
        div2.style.display = 'none';
        div3.style.display = 'none';
    }
    else if (divNumber === 2) {
        div1.style.display = 'none';
        div2.style.display = 'block';
        div3.style.display = 'none';
    }
    else if (divNumber === 3) {
        div1.style.display = 'none';
        div2.style.display = 'none';
        div3.style.display = 'block';
    }
}
function toggleDiv() {
  var myDiv = document.getElementById("myDiv");
  if (myDiv.style.display === "none") {
    myDiv.style.display = "block";
  } else {
    myDiv.style.display = "none";
  }
}
function hideDiv2() {
    var myDiv2 = document.getElementById("myDiv2");
    myDiv2.style.display = "none";
}
function showDiv2() {
    var myDiv2 = document.getElementById("myDiv2");
    myDiv2.style.display = "block";
}
function hideDiv3() {
    var myDiv3 = document.getElementById("myDiv3");
    myDiv3.style.display = "none";
}