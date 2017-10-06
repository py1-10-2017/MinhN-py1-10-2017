def pump(pumpType, ball="air"): #optional parameters
	print "pumping " + ball

# pump("regular")
# #function greet(){ # js equivalent of defining a function
	
# }

# For all numbers between 100 and 100000 test that number for whether it is prime or a perfect square. If it is a prime number print "Foo". If it is a perfect square print "Bar". If it is neither print "FooBar". Do not use the python math library for this exercise. For example, if the number you are evaluating is 25, you will have to figure out if it is a perfect square. It is, so print "Bar".

# This assignment is extra challenging! Try pair programming and pulling up a white board.
4, 9 ,25, 36, 49, 64, 81
num = 10
perfect_sq_arr = []
while (num*num < 100000):
	perfect_sq_arr.append(num*num)
	num += 1 # num = num + 1

# print arr
for x in xrange(100, 200):
	print x
	found = False
	for i in xrange(0, len(perfect_sq_arr)):
		if perfect_sq_arr[i] == x:
			found = True
	if found == True:
		print "bar"
	prime = True
	for i in xrange(2,x/2):
		if x % i == 0:
			prime = False
	if prime == True:
		print "foo"
	if prime != True and found != True:
		print "foobar"

# print string

for x in xrange(0,13):
	if x == 0:
		x=1
		print "x ",
	else:
		if x < 10:
			print str(x) + " ",
		else:
			print x,

	for i in xrange(1,13):
		len_of_largest = len(str(i * 12))
		len_of_curr = len(str(i*x))
		# print len_of_largest,
		if len_of_largest == 2 and len_of_curr == 1:
			print "",
		elif len_of_largest == 3 and len_of_curr == 1:
			print " ",
		elif len_of_largest == 3 and len_of_curr == 2:
			print "", 
		print i*x,
	print ""