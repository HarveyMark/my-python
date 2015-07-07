from sys import exit

def dead(why):
	print why, "You lose!"
	exit(0)

def start():
	print """
You are the Dalai Lama. Three men aproach you, they are are your advisors, and they are here to answer your questions. """
	raw_input(">")
	print "The advisors do not speak that language."
	corn_feild()

def corn_feild():
	print """
You fall asleep, and wake up. You are a small boy in a cornfield, with a bloody knife in your hands, and a dead woman at your feet. 
What do you do? (enter cornfield, run)
"""
	next = raw_input(">")

	if "enter cornfield" in next:
		print """
You run into the cornfield, but the sound of vicious barking dogs stops you in your tracks.
What do you do? (stand and fight, run more)
			  """
		next = raw_input(">")
		if "stand and fight" in next:
			print "You bravley stand your ground, and die fighting the dogs."
			end()
		elif "run more" in next:
			print "You try to out run the hounds, but they catch you, and tear you to shreds."
			end()
		else:
			print "That's not a choice!"
			corn_feild()
	elif "run" in next:
		shed()
	else:
		print "That's not a choice!"
		corn_feild()

def shed():
	print """
You turn around to run, but you notice a shed about ten feet from where you're standing. Dogs are barking, and from the sound of it, they're getting closer by the second.
What do you do? (fight the dogs, enter the shed)"""
	next = raw_input(">")
	if "fight the dogs" in next:
		print "You bravley stand your ground, and die fighting the dogs."
		end()
	elif "enter the shed" in next:
		print """
You use your knife to pry the ruster lock off the old shed, and walk in. You notice a small metal gear on a shelf, and decide to pocket it. Finding nothing more of interest, you exit the shed, and notice a house in the 
distance.
What do you do? (back to cornfeild, go to house)
"""
	else:
		print "That's not an choice!"
		shed()
	next = raw_input(">")
	if "back to cornfeild" in next:
		print """
You try to run back to the cornfeild, but the dogs catch you first. You don't make it.
"""
		end()
	elif "go to house" in next:
		house()
	else:
		print "That's not an option!"
		shed()

def house():
	print """
You start to aproach the house, and notice that a light is on in the right window on the second story. The front door is hanging open, and a ladder is laying against the side of the house. 
What do you do? (enter the front door, use the ladder)
"""
	next = raw_input(">")

	if "use the ladder" in next:
		print """
You grab the ladder, and lean it up against the old building clumsily to reachthe illuminated window. Unfortunatley, you make too much noise, and a man hears you. He leans out the window with a 12 gauge shot guns, and ends your life.
"""
		end()
	elif "enter the front door" in next:
		print """
You enter the house, and notice a set of stairs on your left that lead to the second floor, and what appears to be a dining room on your right. 
What do you do? (stairs, dining room)"""
	else:
		print "That's not an option!"
		house()

	next = raw_input(">")
	if "stairs" in next:
			print """
You try to quietly walk up the old steps, but the creek with every movement. A dog starts barking in the dining room, and rushes toward you, but before he can reach you, a blast from a shotgun hits you in the chest. It knocks you off your feet, and out of existence."""
			end()
	elif "dining room" in next:
			dining_room()
	else:
		print "That's not an option!"
		house()

def dining_room():
	print """
You enter the dining room, and see a dog quietly sleeping by the doorway. Before it wakes up, you quetly slit it's throat, and find a small brass key hanging from it's collar. You pocket it, and look up to find a long table, set with fine china and plates. But some of the silverware looks more like machinery than fine china, so you decide to pocket it. You then see an odd fireplace at the far side of the room, with a strange lever next to it. 
What do you do? (pull the lever, examine silverware)"""
	next = raw_input(">")	
	if "pull the lever" in next:
		print """
Curiousity consumes you, and you pull the lever. The fireplace starts to make a loud noise, and you turn around to check the door, hoping no one came to investigate. A man rounds the corner, wielding a gun, but before you can say anyhting, he fires, and you black out. """
		end()
	elif "examine silverware" in next:
		print """
You examine the odd silverware, and decide to pocket it, it might come in hand later. You turn around to go explore upstairs, the fireplace and the lever can wait."""
		upstairs()
	else:
		print "That's not an option!"
		dining_room()

def upstairs():
	print """
You quietly walk up the stairs. Once you make it to the top, you see a brightly lit room on your left with an open door, and a closed door on your right, with no light peeking through the cracks.
What do you do? (enter bright room, open dark door) """
	next = raw_input(">")
	if "open dark door" in next:
		print """
You open the door, but you find that it's old an worn, so th hinges squeak loudly. You hear a woman inside the room scream, but before you can do anything, you see  a flash of light, and feel a pain in your back."""
		end()

	elif "enter bright room" in next:
		print """
You quietly enter the bright room, and see an old man slumoed over in a chair, gazing hopelessly out a window, with a shotgun accross his lap. Silently, you creep up behind him, and slit his throat, guiding his body to the ground to quiet his fall. You set down your knife, and pick up the shotgun, two shells still in the barrel. You walk accross the hall to the dark door, and kick it open. A once sleeping woman is now awake, and screaming. Out of fear, you raise your gun, and blast a hole in her chest."""
		time_machine()
	else:
		print "That's not an option!"
		upstairs()

def time_machine():
	print """
You fumble your hands along the walls until you find the light switch. Once light has flooded the room, you notice a small locked chest in the corner. You remember the key you snagged off the dog's collar, and quickly use it to unlock the mysteious box. Inside, you find blueprints, with the words "Time Machine" printed accross the top. You put them into your now crowded pockets. What do you do now? (leave the farm, back to the lever)"""
	next = raw_input(">")
	if "leave the farm" in next:
		print """
You empty your pockets, drop the gun, and run. You run from the house, you run from the farm, and you don't stop until you see flashing sirens behind you. A police officer approaches you, and upon seeing that you're covered in blood, promptly arrests you. You are put on trial for the murder of 3 people and a dog, and are found guily, and killed."""
		end()
	elif "back to the lever" in next:
		"""
You return to the fireplace, and pull the lever. The fireplace makes a loud noise, and then rises into the ceiling, revieling a strange looking machcine that closely resembles the one drawn on the blueprints. You pull out the instructions, and notice that pieces of the machine are missing... The pieces that are in your pockets! You grab them, and study the blueprints. After you fit the final piece back into the machine, it starts to whirl, and a blue light appears you step in."""
		you_won()
	else:
		print "That's not an option!"
		time_machine()

def end():
	print """
You fall asleep, and wake up. You are the Dalai Lama. Three men aproach you, but before they can speak, a man wielding a gun rushes in, and kills you.
You lose."""
	exit(0)

def you_won():
	print """
You appear infront of the Dalai Lama. Three men walk in, but before they can speak, a man with a gun walks in. Sensing danger, you raise your shotgun, and kill him.
YOU WON! YOU SAVED THE DALAI LAMA!"""

start()
