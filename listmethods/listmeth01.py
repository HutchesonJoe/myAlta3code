#!/usr/bin/env python3
#creaate a list
proto = ["ssh", "http", "https"]
#print list
print(proto)
#print third item list 
print(proto[2])

proto.extend("dns") # this line will add d, n, and s
print(proto)

