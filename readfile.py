#!/usr/bin/python3

import os

file = open('/etc/passwd', "r")
lines = file.readlines()

for i in lines:
    frag = i.split(":")

sol = [frag[0], frag[-1]]

print("user: ", str(sol[0]), "Shell: ", str(sol[1]))

file.close()
