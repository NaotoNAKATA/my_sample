# -*- coding: utf-8 -*-

import sys

if __name__ == "__main__":
	param = sys.argv
	print "Hello:" + param[0]

	# File read
	f = open(param[0],"r")
	for row in f:
		print row
	f.close()

	#File write
	f = open("out.txt","w")
	f.write("Python write file sample")
	f.close()

