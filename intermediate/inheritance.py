#! /usr/bin/env python3.8

# classes
type(str)

class Person():
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
	def printVals(self):
		print ("Name: {}, Age: {}".format (self.name, self.age))

class Employee (Person):
	department = ""
	def __init__)self, name, age, department):
		Person.__init__ (self, name, age)
		self.department = department
	def  printVals (self):
		Person.printVals (self)
		print  ("Department: {}".format (self.department))

emp =  Employee ("John", 45, "Engineering")

emp.printVals()


def main():
	for i in sys.argv:
		print (i)
	return

main ()
