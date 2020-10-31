
#! /usr/bin/env python3.8

#  Dictionaries
dict1 = {1:2. 3:4, 5:6}
dict1[3]

dir(dict1)

for i in dict1.keys():
	print (i)
	print dict1[i]

for k in dict1.keys():
	print ("{}:{}".format (k, dict1[k]))


def main ():
	
	s1 = "You said '{}'."
	prompt = input ("What do you want to say? ")
	print (s1.format (prompt))
	return

main()

