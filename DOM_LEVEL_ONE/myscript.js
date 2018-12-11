var headone = document.querySelector("#one");
var headtwo = document.querySelector("#two");
var headthree = document.querySelector("#three");

console.log(headone);

headone.addEventListener("mouseover", function () {
	headone.textContent = "Mouse Currently Over";
	headone.style.color = 'blue';
})

headone.addEventListener("mouseout", function () {
	headone.textContent = "HOVER OVER ME";
	headone.style.color = 'black';
})

headtwo.addEventListener("click", function () {
	headtwo.textContent = "Clicked On!";
	headtwo.style.color = "purple";
})

headthree.addEventListener("dblclick", function () {
	headthree.textContent = "I was double clicked!";
	headthree.style.color = "red";
})