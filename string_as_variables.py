# When declaring strings, you can use " " or ' '.
myName = 'Harvey Mark'
myAge = 20 # Not a lie
myHeight = 75.0 #inches
myWeight = 180 #pounds
myEyes = "Blue"
myTeeth = "White"
myHair = "Brown"
inchesToFeet = myHeight / 12.0

print "Lets's talk about %s." % myName
print "He is %d feet tall." % inchesToFeet
print "He's %d punds heavy." % myWeight
print "He's got %s eys and %s hair." % (myEyes, myHair)
print "His teeth are usually %s, depending on the coffee." % myTeeth
print "if I add %s, %s, and %s I get %s." % (myAge, myHeight, myWeight, myAge + myHeight + myAge)