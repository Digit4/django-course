#Showcasing different special methods in class

class Book():
	def __init__(self, title, author, pages):
		self.title = title
		self.author = author
		self.pages = pages
	
	def __str__(self):
		return("Title:%s Author:%s Pages:%d" %(self.title,self.author,self.pages))

	def __len__(self):
		return (self.pages)

	def __del__(self):
		print("Delete pages")
	

mybook = Book("LOTR", "J. R. R. Tolkien", 1000)
print(len(mybook))

del(mybook)