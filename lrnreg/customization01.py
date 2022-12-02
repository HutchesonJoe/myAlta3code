# LAB 50 CHALLENGE 1 SOLUTION
searches= []
print(f"Great! Please enter a string to search for:")

while True:
    searchFor = input("> ")
    if searchFor.lower() == "quit":
        break
    searches.append(searchFor)
    print("Type in another string to search for, or type QUIT to continue:")

print(searches) 
