#! /usr/bin/env python3.8

# exceptions

class CustomException (Exception):
	print("Exception Found")

def main():
	list1 = [1, 2, 3, 4, 5]
	try:
		for i in range(6):
			if  i % 3 ==  1:
				raise CustomException
			print (list1[i])
	except IndexError:
		print ("Index out of range")
