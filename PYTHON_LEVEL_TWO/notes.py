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

print(re.findall('is', 'this is a string for it is a is'))

# meta char find

def multi_find(patterns, phrase):
	for pat in patterns:
		print("Searching for pattern {}".format(pat))
		print(re.findall(pat, phrase))
		print("\n")

test = "This is a test string with numbers and stuff 129 40  symbol #$!@#"

testpat = [r"\W+"]  #normal re works similar to re from TOC but for special RE, we can use escape symbols like
				#r'\d' = all the numbers r'\D' = all non numeric values
				#r'\s' sequence of whitespace r'\S' non whitespace
				#r'\w' all alphanumeric r'\W' all non alphanumeric

multi_find(testpat,test)
