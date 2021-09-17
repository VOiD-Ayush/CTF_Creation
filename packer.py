#!/bin/python3

import os
r = open('./wd.txt','r').read()

words=r.splitlines()

# os.system("zip flag.zip flag.txt")

current_zip="flag.zip"

for word in words:
	os.system("zip {0}.zip {1}".format(word,current_zip))
	os.system("rm {0}".format(current_zip))
	current_zip="{0}.zip".format(word)

# zip flag.zip flag.txt  
