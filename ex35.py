from sys import exit

def gold_room():
	print """This room is full of gold. How much do you take? 
(Enter a number, don't be greedy!)"""

	next = raw_input("> ")
	try:
    		how_much = int(next)
	except ValueError:
    		dead("Man, learn to type a number.")

	if how_much < 50:
		print "Nice, you're not greedy! You win!"
		exit(0)
	else:
		dead("You greedy bastard!")

def bear_room():
	print "There is a bear in here."
	print "The bear has a bunch of honey."
	print "The fat bear is in front of another door."
	print "How are you gunna move the bear? (take honey or taunt bear)"
	bear_moved = False

	while True:
		next = raw_input("> ")

		if next == "take honey":
			dead("The bear looks at you, then slaps your face off.")
		elif next == "taunt bear" and not bear_moved:
			print "The bear has moved from the door. You can go through it now. (open door)"
			bear_moved = True
		elif next == "taunt bear" and bear_moved:
			dead("The bear gets pissed off and chews off your leg.")
		elif next == "open door" and bear_moved:
			gold_room()
		else:
			print "I got no idea what that means."

def cthulhu_room():
	print "Here you see the great evil Cthulhu."
	print "He, it, whatever, stares at you, and you go insane."
	print "Do you flee for your life, or do you eat your head? (flee or head)"

	next = raw_input(">")

	if "flee" in next:
		start()
	elif "head" in next:
		dead("Well that was tasty!")
	else:
		cthulhu_room()

def dead(why):
	print why, "Good job!"
	exit(0)

def start():
	print "You are in a dark room."
	print "There is a door to your right, and a door to your left."
	print "Which one do you take? (left or right)"

	next = raw_input(">")

	if next == "left":
		bear_room()
	elif next == "right":
		cthulhu_room()
	else:
		dead("You stumble around the room until you starve.")

start()




















