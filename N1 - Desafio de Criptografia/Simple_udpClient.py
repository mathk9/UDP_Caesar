from socket import *
from caesar import Caesar

serverName = "192.168.0.71" # IPv4 // ::1 IPv6
serverPort = 12500
clientSocket = socket(AF_INET, SOCK_DGRAM) # AF_INET6
print("UDP Client\n")
ce = Caesar()
while 1:
    message = input("Input message: ")
    if message == "exit":
        break
    else:
        
        message = ce.encrypt(message, 4)
        print(message)
    clientSocket.sendto(bytes(message,"utf-8"), (serverName, serverPort))
clientSocket.close()
