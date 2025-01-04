#   Author: Cameron Simmons
#   Date: 1/3/2025
#   Verison: 1
#   Last modified: 1/3/2025
#   Description: This code will ask a user to input a value of an IP and will break it down to the network address, broadcast address, and subnet 
def getIP ():    
    octet_one = int(input("Enter the first octet of the ip address: "))
    while (octet_one) < 0 or (octet_one) > 255:
         octet_one = int(input("The value you have entered its not in the range of an octet please re-enter the value: "))
    octet_two = int(input("Enter the second octet of the ip address: "))
    while (octet_two) < 0 or (octet_two) > 255:
         octet_two = int(input("The value you have entered its not in the range of an octet please re-enter the value: "))
    octet_three = int(input("Enter the third octet of the ip address: "))
    while (octet_three) < 0 or (octet_three) > 255:
         octet_three = int(input("The value you have entered its not in the range of an octet please re-enter the value: "))
    octet_four = int(input("Enter the fourth octet of the ip address: "))
    while (octet_four) < 0 or (octet_four) > 255:
         octet_four = int(input("The value you have entered its not in the range of an octet please re-enter the value: "))
    
    octet_dot = "."

    ip_address = str((str(octet_one) + octet_dot + str(octet_two) + octet_dot + str(octet_three) + octet_dot + str(octet_four)))
    byte = ip_address.split(".")
    return byte

# Start of the program 

print(" \n")
print("Welcome please enter your ip address below")
print(" \n")
byte = getIP()
print(byte)
