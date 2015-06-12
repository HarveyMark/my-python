from sys import argv

script, filename = argv

#This confirms if the user wants to truncate the file.
print "We're going to erase %r." % filename
print "If you don't want to do that, hit CTRL-C (^C)"
print "If you want to erase it, hit RETURN."

raw_input("?")

#This opens the file , 'w' is a command used to write.
print "Opening the file..."
target = open(filename, 'w')

#This deletes the file.
print "Truncating the file... Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

#Here the user can re-write the file.
line1 = raw_input("Line 1: ")
line2 = raw_input("Line 2: ")
line3 = raw_input("Line 3: ")

print "I'm going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

#ALLWAYS CLOSE THE FILE!
print "And finally, we close the file."
target.close()