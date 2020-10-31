#! /usr/bin/env python3.8

#  Strings
def main ():
	s1 = "You said '{}'."
	prompt = input ("What do you want to say? ")
	print (s1.format (prompt))
	return

main()
