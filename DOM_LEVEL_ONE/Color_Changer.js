function changeColor(curColor) {
	switch (curColor) {
		case "red":
			document.querySelector("h1").style.color = "blue";
			break;
		case "blue":
			document.querySelector("h1").style.color = "green";
			break;
		case 'green':
			document.querySelector("h1").style.color = 'red';
			break;

    default:
      break;
  }
}

setInterval("changeColor()", 1000, document.querySelector("h1").style.color);