pumped_up = False
def pump(typeOfPump, ball="air", require_needle=False):
	print "pumping " + ball + " with " + typeOfPump + " pump"
	print "done pumping"
	pumped_up = True
	# def deflate(): # scoping
	# 	print "deflating a ball"
	# deflate()

pump("hand")

# Write a program that prints all the prime numbers and all the perfect squares for all numbers between 100 and 100000.

# For all numbers between 100 and 100000 test that number for whether it is prime or a perfect square. If it is a prime number print "Foo". If it is a perfect square print "Bar". If it is neither print "FooBar". Do not use the python math library for this exercise. For example, if the number you are evaluating is 25, you will have to figure out if it is a perfect square. It is, so print "Bar".

# This assignment is extra challenging! Try pair programming and pulling up a white board.
# 57
# 2 -> 26

for x in xrange(100,1000):
	print x
	square = False
	for i in xrange(10, x):
		if i * i == x:
			print "perfect square"
			square = True
			break
		elif i * i > x:
			print "not a perfect square"
			break
	if square == False:
		prime = True
		for i in xrange(2, x/2):
			if x % i == 0:
				prime = False
				break
		if prime == True:
			print "prime"


