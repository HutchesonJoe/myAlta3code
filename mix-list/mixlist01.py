#!/usr/bin/env python3

#create a list containing three items
my_list = ["192.168.0.5", 5060, "UP"]

#return the first item in the list
print("The first item in the list (IP): " + my_list[0])

#return the second item in the list
print("The second item in the list (port): " + str(my_list[1]))

#return the third item on the list
print("The third item on the list (state): " + my_list[2])

iplist = [ 5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh" ]

print("IP addresses: " + iplist[3] + ", and " + iplist[4])

print("IP addresses:", iplist[3], ", and", iplist[4])

print(f"IP addresses: {iplist[3]}, and {iplist[4]}")

