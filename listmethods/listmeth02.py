#!/usr/bin/env python3
proto = ["ssh", "http", "https"]
protoa = ["ssh", "http", "https"]
print(proto)
proto.append("dns") # this line will add "dns" to the end of our list
protoa.append("dns") #this line will add "dns" to the end of our list
print(proto)
proto2 = [ 22, 80, 443, 53 ]
proto.extend(proto2) #pass proto2 as an argument tot he extend method
print(proto)
protoa.append(proto2) # pass proto2 as an argument to the append method
print(protoa)
protoa.reverse()
print(protoa)
count = proto.count("ssh")
#printing how many instance os "ssh" are in the proto list
print(count)
