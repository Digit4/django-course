function playbtn()
{
	var all_btns = document.querySelectorAll("button.btn-light");
	for (var i = 0; i < all_btns.length; i++) {
		all_btns[i].innerHTML = " ";
	};
}

function clear_boxes()
{
	var cells = document.querySelectorAll("#fixwidth");
	for (eachcell in cells) {
		console.log(eachcell)
	}
}

function change_state(nm)
{
	var cell_num = document.querySelector("button[name="+nm+"]");
	if (cell_num.innerHTML == " ") {
		cell_num.innerHTML = "X";
		} else if (cell_num.innerHTML == "X") {
		cell_num.innerHTML = "O";
		} else if (cell_num.innerHTML == "O") {
		cell_num.innerHTML = " ";
		} 
}