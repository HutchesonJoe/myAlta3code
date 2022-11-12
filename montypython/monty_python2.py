#!/usr/bin/env python3

round = 0

while True:
    round = round + 1
    print('Finish the movie title, "Monty Python\'s The Life of ______"')
    answer = input("Your guess-->")

    if answer.lower()=="brian":
        print("Correct! Well done.")
        break
    elif round==3:
        print("Loser.")
        break
    else: 
        print("Sorry, Loser, try again!")

