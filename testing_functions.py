def about_you(name, age, highschool):
	print "So, your name is %s, you're %s years old, and you went to %s. \n Cool!" % (name, age, highschool)

print "So, what's your name?"
name = raw_input(">")

print "How old are you?"
age = raw_input(">")

print "Where did you go to highschool?"
highschool = raw_input(">")
about_you(name, age, highschool)