# Import socket module 
import socket                
  
# Create a socket object 
s = socket.socket()          
  
# Define the port on which you want to connect 
port = 12345                
  
# connect to the server on local computer 
s.connect(('127.0.0.1', port)) 

# receive data from the server 
print (s.recv(1024).decode()) 
print ("Chat session started : \n")

str1 = input(">>> [Client] : ")

while(str1!="bye"):
	s.send(str.encode(str1))
	print (">>> [Server] :",s.recv(1024).decode()) 
	str1 = input(">>> [Client] : ")

s.send(str.encode(str1))
print ("\nChat session ended")

# close the connection
s.close() 