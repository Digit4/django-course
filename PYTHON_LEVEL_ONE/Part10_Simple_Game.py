###########################
## PART 10: Simple Game ###
### --- CODEBREAKER --- ###
## --Nope--Close--Match--  ##
###########################

# It's time to actually make a simple command line game so put together everything
# you've learned so far about Python. The game goes like this:

# 1. The computer will think of 3 digit number that has no repeating digits.
# 2. You will then guess a 3 digit number
# 3. The computer will then give back clues, the possible clues are:
#
#     Close: You've guessed a correct number but in the wrong position
#     Match: You've guessed a correct number in the correct position
#     Nope: You haven't guess any of the numbers correctly
#
# 4. Based on these clues you will guess again until you break the code with a
#    perfect match!

# There are a few things you will have to discover for yourself for this game!
# Here are some useful hints:

def num_len_check(x):
	if(x.isnumeric()):
		if (len(x) > 3):
			print("Oops! you've entered too many numbers, please try lesser numbers.")
		elif (len(x) < 3):
			print("You must enter at least 3 numbers, please try more numbers.")
		else:
			return False
	else:
		print("Please Enter numeric values only")
	return True

def num_validity_converstion(num):
	if (num.isnumeric()):
		valid_nums = list(map(int, num))
	return valid_nums

def game_rules(actual_digits, guessed_digits):
	match, close, nope = 0, 0, 0
	for i in guessed_digits:
		flag = False
		for j in actual_digits:
			if (j == i):
				if (guessed_digits.index(i) == actual_digits.index(j)):
					match += 1
					flag = True
					break
				else:
					close += 1
					flag = True
					break
		if (not flag):
			nope += 1

	return [match,close,nope]

# Try to figure out what this code is doing and how it might be useful to you
import random
digits = list(range(10))
random.shuffle(digits)
print(digits[:3])

# Another hint:


# Think about how you will compare the input to the random number, what format
# should they be in? Maybe some sort of sequence? Watch the Lecture video for more hints!
digits_matched = False

while (not digits_matched):
	guess = input("What is your guess? ")
	print(guess)
	if (num_len_check(guess)):
		continue
	guessed_nums = num_validity_converstion(guess)
	print(game_rules(digits,guessed_nums))
	

