#! /usr/bin/env python3.8

# interpreter.py

# delimiter |
def main():
	numTokens = []
	strTokens = []
	userData = input("Insert Delimited Data: ")
	splitData = userData.split (sep="|")
	for i in splitData:
		i = i.strip()
		if i.isnumeric():
			numTokens.append(i)
		else:
			strTokens.append(i)
	print ("String Tokens: {}\nNumeric Tokens: {}".format (len(strTokens), len(numTokens)))
	return

main ()

