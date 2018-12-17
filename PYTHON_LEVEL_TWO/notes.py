# exceptions

try:
	f = open("simple.txt", 'r')
	f.write("Test data to be written")
except IOError:
	print("Oppsn")