# This line declares a string, and uses format characters. 
x = "There are %d types of people." % 10

# These lines declare variables, and then uses those variables with format charactes.
binary = "binary"
do_not = "don't"
y = "Those who know %s, and those who %s." % (binary, do_not) 

# These two lines print the above lines.
print x
print y

#These two lines reprint the above, but with an extra string.
print "I said: %r." % x
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny? %r"

print joke_evaluation % hilarious

# This is how to print two seperate strings
w = "This is the left side of..."
e = "A string with a right side."

print w + e


