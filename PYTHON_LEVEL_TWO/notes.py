# exceptions

""" try:
	f = open("simple.txt", 'r')
	f.write("Test data to be written")
except IOError:
	print("Oppsn") """

# regex

import re

patterns = ['term1', 'term2']

text = "this is a string with term1 but not the  other one"

for pat in patterns:
	print("im searching for %s" % pat)
	
	if (re.search(pat, text)):
		print("match")
	else:
		print("no match")

match = re.search('term1', text)

print(match.start())


#splittin strings

splitterm = "@"

email = "user@gmail.com"

print(re.split(splitterm, email))


# find all instances of a pattern

print(re.findall('is','this is a string for it is a is'))