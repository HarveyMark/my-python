def counting_up():
	i = 0
	numbers = []
	print "Where do you want to end? (This number will not appear in the count)"
	x = int(raw_input(">"))
	print "How much would you like to increment by?"
	a = int(raw_input(">"))
	
	while i < x:
		#print "At the top, i is %d." % i
		numbers.append(i)

		i = i + a
		#print "Numbers now: ", numbers
		#print "At the bottom, i is %d." % i

		print "Your numbers: ", numbers
		for num in numbers:
			print num
counting_up()

