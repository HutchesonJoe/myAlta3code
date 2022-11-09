#!/usr/bin/env python3
my_list = [ "192.168.0.5", 5060, "UP" ]
#display the first item on the list
print("The first item in the list (IP): " + my_list[0])
#display the second item on the list
print("The second item in the list (port): " + str(my_list[1]))
#display the last item on the list
print("The last item in the list (state): " + my_list[2])
iplist = [ 5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh" ]
#display only the IP address
print("IP addresses: " + iplist[3] + " and"  + iplist[4])
print("IP addresses: ", iplist[3], " and", iplist[4])
print(f"IP addresses: {iplist[3]}, and {iplist[4]}")
