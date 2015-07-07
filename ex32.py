the_count = [1, 2, 3, 4, 5,]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this is the first kind of for-loop going through a list
for stuff in the_count:
	print "This is count %d." % stuff

# same as above.
for fruit in fruits:
	print "A type of fruit: %s" % fruit

# we can go through mixed lists too
# notice we have to use %r because we don't know what's in it
for i in change:
	print "I've got %r." % i

# we can also build lists. start with this.
elements = []

#then use the range funtion to do a 0-5 count 
for anything in range(6):
	print "Adding %d to the list." % anything
	# append is a function that lists understand. 
	elements.append(anything)

#now we can print them out too
for i in elements:
	print "Element was: %d." % i

#testing lists
#the_junk is a name for the contents of the list for this 'for' function.
#if you try to call 'i', it will return the last item in the list of the previous call of 'elements'
for the_junk in elements:
	print "This is %d." % the_junk