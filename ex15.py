#The standard 'argv' syntax
from sys import argv

script, filename = argv

#This opens a file
txt = open(filename)

print "Here's your file %r: " % filename 
#This command reads the file and outputs the contents
print txt.read()

#This pulls up the file a second time
print "Type the filename again: "
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()

#This closes the files you opened
txt.close()
txt_again.close()