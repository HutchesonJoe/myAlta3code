#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   if, elif, else - A simple program using conditionals to make a decision."""

drink = input("What is your morning drink of choice?")

if drink == "coffee":
    print("I also like " + drink)
elif drink == "tea":
    print("I often fancy a cup of " + drink)
else:
    print("I have no opinion regarding " + drink)


