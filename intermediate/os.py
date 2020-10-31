#! /usr/bin/env python3.8

import os

help (os)

help (os.walk)

help (os.system) # executes in a shell
os.system("pwd")

# tuple, like a list?
tuple1 = (1, 2, 3)
type (tuple1)
tuple[0]
dir(tuple1)


for item1, item2, item3 in os.walk ("."):
	print("{}:{}:{}".format(item1, item2, item3))

def main():
	for i in sys.argv:
		print (i)
	return

main ()
