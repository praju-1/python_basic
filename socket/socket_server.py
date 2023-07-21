#!/usr/bin/python3

#This is tcp_server.py script

import socket

# creating socket object
s = socket.socket()		   
# getting current machine name 
host = socket.gethostname()	  
# port number for connection
port = 1234		              

# bind with address
s.bind((host,port))	

print (" Waiting for connection... ")
# listen for cnnections
s.listen(5)	
print(" Socket is listening ")		         

while True:
	# connect and accept from client
	conn,addr = s.accept()	         
	print ('Got Connection from', addr)
	msg = "server saying Hi..."
	conn.send(msg.encode())
	# close the connection
	conn.close()		    

