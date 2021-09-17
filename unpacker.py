#!/bin/python3

import os
import subprocess

# os.system("cp ./../starwars.zip .")

while True :
	output = subprocess.check_output("ls *.zip", shell=True)
	output=str(output.decode("utf-8"))
	print(output,"starwars.zip\n")
	os.system("unzip {0}".format(output))
	os.system("rm {0}".format(output))
	if (output=="flag.zip\n"):
		print("\n\n\nHere's your flag : ",end="")
		os.system("cat flag.txt")
		exit(0)

	

