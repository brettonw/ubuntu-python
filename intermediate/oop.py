#! /usr/bin/env python3.8

# classes
type(str)

class MyCustomClass():
	# member variables
	myCustomList = [1,2,3,4]
	name= ''
	age = 0

	# private functions
	def__init__(self, name, age):
		self.name= name
		self.age = age
		return

	# public functions
	def customFunction(self):
		print ("Name: {}, Age: {}".format (self.name, self.age))

object1 = MyCustomClass("John", 25)
print (object1.myCustomList)
object1.customFunction()


def main():
	for i in sys.argv:
		print (i)
	return

main ()
