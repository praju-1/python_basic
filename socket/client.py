#!/usr/bin/python

#This is tcp_client.py script

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket successfully created")
# Get current machine name
host = socket.gethostname()	 
# Client wants to connect to server's
port = 1234	          
# connecting to server address
s.connect((host,port))
# 1024 is bufsize or max amount of data to be received at once
print (s.recv(1024))		           
s.close()
