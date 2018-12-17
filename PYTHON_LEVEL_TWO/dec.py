def new_dec(func):

	def wrap_func():
		print("code here before executing func")
		func()
		print("func has been called")

	return wrap_func


@new_dec 		# this single line
def func_needs_dec():
	print("This func needs decorator!")  # means the same as

# func_needs_dec = new_dec(func_needs_dec)   #this line here

func_needs_dec()

