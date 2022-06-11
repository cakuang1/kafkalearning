import socket            
import broker




#Create broker


# next create a socket object
s = socket.socket()        
print ("Socket successfully created")
 
HOST = "127.0.0.1"
# reserve a port on your computer in our
# case it is 12345 but it can be anything
port = 12345               
 
#Bind our socket object to an ip address and the port number
s.bind((HOST, port))        
print ("socket binded to %s" %(port))
 
# put the socket into listening mode/enables the server to accept connection
s.listen(5)             


broker.broker()
# a forever loop until we interrupt it or
# an error occurs
while True:
 
# Establish connection with client. Returns a socket object and a tuple 
  c, addr = s.accept()    
  print ('Got connection from', addr )
 
  # send a thank you message to the client. encoding to send byte type.
  c.send('Thank you for connecting'.encode())
 
  # Close the connection with the client
  c.close()
   
  # Breaking once connection closed
  break





