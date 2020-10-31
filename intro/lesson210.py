#! /usr/bin/env python3.8

#  Lists

list1 = [1, 2, 3, 4]
help (list1)

dir (list1)
list1.append (5)
list1.pop()
list1.clear ()

# slicing
from=0
to=4
step=1
list1[from:to:step]
# slices don't modify lists



def main ():
	
	s1 = "You said '{}'."
	prompt = input ("What do you want to say? ")
	print (s1.format (prompt))
	return

main()

