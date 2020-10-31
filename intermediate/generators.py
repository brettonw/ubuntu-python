#! /usr/bin/env python3.8

# generators

def CustomRange(last):
	i = 0
	while i < last:
		yield i
		i += 1

for i in CustomRange(10):
	print(i)
