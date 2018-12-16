$('h1').on('mouseenter', function () {
	$(this).toggleClass('turnRed')
})


$('input').eq(1).on('click', function () {
	$('.container').slideUp(3000);
})