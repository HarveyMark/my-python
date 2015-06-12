#ex.16.py study drill
from sys import argv

scrpit, new_file = argv

print "Let's read %r." % new_file
target = open(new_file, 'r')
print target.read()

#Don't forget to close it!
target.close()