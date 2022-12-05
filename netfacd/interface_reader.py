#!/usr/bin/env python3
import netifaces

print(netifaces.interfaces())

for i in netifaces.interfaces():
        print('\n**************Details of Interface - ' + i + ' *********************')
        try: # this is anew line, you also need to indent the code before this line by 4 whitespaces
            print('MAC: ', end='') # This print statement will always print MAC without an end of line
            print(netifaces.ifaddresses(i)[netifaces.AF_LINK][0]['addr']) #Prints the MAC address
            print('IP: ', end='') # This print statement will always print IP without an end of line
            print(netifaces.ifaddresses(i)[netifaces.AF_INET][0]['addr'])
        except:
            print('Could not collect adapter information') # Print an error message


