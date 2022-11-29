#!/usr/bin/env python3
## create file object in "r"ead mode
count = 0
filename = input("What is the name of the file to load? ")
with open("vlanconfig.cfg", "r") as configfile:
    ## readlines() creates a list by reading target
    ## file line by line
    configlist = configfile.readlines()
    # this is not working how I want it to : (
    count = enumerate(configfile)

## file was just auto closed (no more indenting)

## each item of the list now has the "/n" characters back
print(configlist, count)
