#   Author: Cameron Simmons
#   Date: 1/7/2025
#   Verison: 1
#   Last modified: 1/7/2025
#   Description: This code will ask a user to input a value of an IP and will break it down to the network address, broadcast address, and subnet 

# Gets the IP address entered and splits in to a list 
# ['192', '168', '59', '126']

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
    ipAddress = ip_address.split(".")
    return ipAddress
#
## As long as 
def binaryConvert(value):
     bits = ""      # 0

     while value != 0:
     
          remainderBinary = value % 2 
          value = value // 2
          
          bits += str(remainderBinary)
     return bits

## Reverse string
def switch(x):
     return x [::-1]


# Start of the program 
first_binary  =  0
remainder = "" # 0
bitSpace = 0b11111111


print(" \n")
print("Welcome please enter your ip address below")
print(" \n")
ipAddress = getIP()

firstOctet  = int(ipAddress[0])
firstBinaryStr = binaryConvert(firstOctet)
firstBinaryStr = switch(firstBinaryStr)
print("")
print(firstBinaryStr)
print("")

secondOctet = int(ipAddress[1])
secondBinaryStr =binaryConvert(secondOctet)
secondBinaryStr = switch(secondBinaryStr)
print("")
print(secondBinaryStr)
print("")

#
thirdOctet  = int(ipAddress[2])

thirdBinaryStr = binaryConvert(thirdOctet)
thirdBinaryStr = switch(thirdBinaryStr)
print(thirdBinaryStr)
print("")
print(thirdBinaryStr)
print("")

#
fourthOctet = int(ipAddress[3])
fourthBinaryStr = binaryConvert(fourthOctet)
fourthBinaryStr = switch(fourthBinaryStr)
print("")
print(fourthBinaryStr)
print("")

first = int(firstBinaryStr, 2)## Important for the binary conversion 
#firstBinaryStr = firstBinaryStr & bitSpace

#test = & bitSpace

value = first & bitSpace


print(f"{value:08b}")


#print(firstBinaryStr +"|" + secondBinaryStr +"|"+ thirdBinaryStr +"|"+ fourthBinaryStr)
