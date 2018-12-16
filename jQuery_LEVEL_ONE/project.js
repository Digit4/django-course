var p1 = prompt("Enter Blue Player's Name:");
var pcol1 = 'rgb(86, 151, 255)';
var p2 = prompt("Enter Red Player's Name");
var pcol2 = "rgb(237, 45, 73)";

var colSize = 7;

var game_on = true;

var table = $('table tr');

function reportWin(rowNum, colNum) {
	console.log("You won starting at this row,col.");
	console.log(rowNum);
	console.log(colNum);
}

function changeColor(rowIndex, colIndex, color) {
	return table.eq(rowIndex).find('td').eq(colIndex).find('button').css('background-color', color);
}

function returnColor(rowIndex, colIndex) {
	return table.eq(rowIndex).find('td').eq(colIndex).find('button').css('background-color');
}

function checkBottom(colIndex) {
	var colorReport = returnColor(5, colIndex);
	for (var row = 5; row >= 0; row--){
		colorReport = returnColor(row, colIndex);
		if (colorReport === 'rgb(128, 128, 128)') {
			return row;
		}
	}
}
function colorMatchCheck(one,two,three,four) {
	return (one === two && one === three && one === four && one !== 'rgb(128, 128, 128)' && one !== undefined);
}

function horizontalWinCheck() {
	for (var row = 0; row < 6; row++) {
		for (var col = 0; col < 4; col++){
			if (colorMatchCheck(returnColor(row, col), returnColor(row, col + 1), returnColor(row, col + 2), returnColor(row, col + 3))) {
				console.log("horiz");
				reportWin(row, col);
				return true;
			}
			else
				continue;
		}
	}
}

function verticalWinCheck() {
	for (var col = 0; col < 7; col++) {
		for (var row = 0; row < 3; row++) {
			if (colorMatchCheck(returnColor(row, col), returnColor(row + 1, col), returnColor(row + 2, col), returnColor(row + 3, col))) {
				console.log("vertic");
				reportWin(row, col);
				return true;
			}
			else
				continue;
		}
	}
}

function diagonalWinCheck() {
	for (var row = 0; row < 6; row++) {
		for (var col = 0; col < 6; col++) {
			if (colorMatchCheck(returnColor(row, col), returnColor(row + 1, col + 1), returnColor(row + 2, col + 1), returnColor(row + 3, col + 1))) {
				console.log("diag-lr");
				reportWin(row, col);
				return true;
			}
			else
				continue;
		}
	}

	for (var row = 0; row < 6; row++) {
		for (var col = 6; col > 0; col--) {
			if (colorMatchCheck(returnColor(row, col), returnColor(row - 1, col + 1), returnColor(row - 2, col + 2), returnColor(row - 3, col + 3))) {
				console.log("diag-rl");
				reportWin(row, col);
				return true;
			}
			else
				continue;
		}
	}
}

var currentPlayer = 1;
var currentName = p1;
var currentColor = pcol1;
$(document).ready(function () {
	if (game_on) {
		$('h2.playerturn').html(currentName + "'s Turn: Pick a column to drop in.");

		$('.board button ').on('click', function () {
			var col = $(this).closest('td').index();

			var bottomAvail = checkBottom(col);
			changeColor(bottomAvail, col, currentColor);
			if (horizontalWinCheck() || verticalWinCheck() || diagonalWinCheck()) {
				$("h2.playerturn").html("Refresh the page to restart playing the game.");
				$('h1').text(currentName.toUpperCase() + " YOU HAVE WON!!!!!!");

				$('h2').fadeOut(1000);
				game_on = false;
			}

			currentPlayer *= -1;
			if (currentPlayer === 1) {
				currentName = p1;
				currentColor = pcol1
			}
			else {
				currentName = p2;
				currentColor = pcol2;
			}
			$("h2.playerturn").html(currentName + "'s Turn: Pick a column to drop in.");

		})
	}
	else {
		
	}
})
