#NOT FINISHED

import random

random = random.randit(1, 100)

guess = 0

while guesses < 5:
	guess = int(raw_input("Enter a number from 1 to 100:"))
	guess += 1
	print "You've guessed ", guesses, "times!"

if guess > number:
	print "You guessed too high!"
elif guess < number:
	print "You guessed too low!"

if guess == number:
	guess = str(guesses)

	print "You got it in ", guesses, "guesses!"

if guess != number:
	number = str(number)
	print "The number was: ", number