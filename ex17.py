from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying %s to %s" % (from_file, to_file)

#try to do this with one line
in_file = open(from_file)
indata = in_file.read()

print "The input file is %d bytes long" %len(indata)

print "Does the output file exist? %r" % exists(to_file)

print "Ready. Hit ENTER to coninue, CTRL-C to quit."
raw_input(">")

out_file = open(to_file, 'w')
out_file.write(indata)

print "Finished"

out_file.close()
in_file.close()