#!/usr/bin/python3

file = open('/etc/passwd', "r")
lines = file.readlines()

for line in lines:
	frag = line.split(":")
	print("user: ", frag[0], "Shell: ", frag[-1][:-1])
	
file.close()
