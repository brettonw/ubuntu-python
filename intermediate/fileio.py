#! /usr/bin/env python3.8

import sys

#f = open("test.dat", "w")
#f.write("This is a test string\n")
#f.close()

# f.open("blarg.jpg", "rb")

f = open ("test.dat", "r")
f.seek(0)
line = f.readline()
f.close()

def main():
	for i in sys.argv:
		print (i)
	return

main ()
