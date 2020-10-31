#! /usr/bin/env python3.8

#  Strings

def main ():
	name_list = ['joe', 'jimmy', 'bob', 'tim']
	input_var = "Joe"
	for i in name_list:
		if i.lower() == input_var.lower():
			print (i)
	return

main()
