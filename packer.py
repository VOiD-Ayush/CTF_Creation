#!/bin/python3

import os
import string    
import random # define the random module  

# os.system("zip flag.zip flag.txt")

current_zip="flag.zip"

for i in range(1000):
	ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k = i%10))    
	os.system("zip {0}.zip {1}".format(ran,current_zip))
	os.system("rm {0}".format(current_zip))
	current_zip="{0}.zip".format(ran)

# zip flag.zip flag.txt
