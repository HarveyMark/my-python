# Declare variables, make a variable equal to an equation of other variables
cars = 100
spaceInCar = 4.0
drivers = 30
passengers = 90
carsNotDriven = cars - drivers
carsDriven = drivers
carpoolCap = carsDriven * spaceInCar
averagePassenger = passengers / carsDriven

#The print staements that show the answer to the equations, and print variables
print "There are", cars, "available."
print "There are only", drivers, "drivers available."
print "There will be", carsNotDriven, "empty cars today."
print "We can transport", carpoolCap, "people today."
print "We have", passengers, "people to transport today."
print "we need to put about", averagePassenger, "in each car."

# I still don't fully understand this, but it's neat.
print "Hey %s there." % "You."
print "This is a %s" % "test."
