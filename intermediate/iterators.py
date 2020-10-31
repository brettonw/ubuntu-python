#! /usr/bin/env python3.8

# iterators
class IterDemo:
	def __init__(self):
		self.alphabet = "abcdefghijklmnopqrstuvwxyz"
		self.i = 0
	def  __iter__(self):
		return self;
	def __next__(self):
		if self.i > len(self.aplhabet):
			raise StopIteration
		letter = self.alphabet[self.i]
		self.i = self.i + 1
		return letter

demo = IterDemo()
for i in demo:
	print (i)


def main():
	for i in sys.argv:
		print (i)
	return

main ()
