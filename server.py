
from http import client
from pydoc_data.topics import topics
import socket
import pickle

from sympy import python         
import broker
import sys



producerargs = ['add','delete','createtopic','deletetopic']
clientargs = ['subscribe']


# next create a socket object
s = socket.socket()        
print ("Socket successfully created")
 
HOST = "127.0.0.1"
# reserve a port on your computer in our
# case it is 12345 but it can be anything
port = 12345               
 
#Bind our socket object to an ip address and the port number
s.bind((HOST, port))        
 
# put the socket into listening mode/enables the server to accept connection
s.listen(5)             


brokerobject = broker.broker(HOST + str(port))

print("Broker created")




# a forever loop until we interrupt it or
# an error occurs
while True:
 
# Establish connection with client. Returns a socket object and a tuple 
  print('Waiting for producer/consumer')
  c, addr = s.accept()    
  print ('Got connection from', addr )

  recieved = c.recv(1024)
  data = pickle.loads(recieved)
  # Producer
  if data[0] == 'producer.py' and (len(data) == 3 or len(data) == 4) and (data[1] in producerargs):
    if data[1] == 'createtopic': # createtopic argument
      if data[2] in brokerobject.topic.keys():
        c.send("Topic {} is already created".format(data[2]).encode())
      else:
        brokerobject.addtopic(data[2])
        c.send("Topic {} created".format(data[2]).encode())
    elif data[2] == 'deletetopic': #deletetopic argument
      if data[2] in brokerobject.topic.keys():
        brokerobject.deletetopic(data[2])
        c.send("Topic {} is deleted".format(data[2]).encode())
      else:
        c.send("Topic {} is not available".format(data[2]).encode())
    elif data[1] == 'add': # add argument
      if data[2] in brokerobject.topic.keys():
        brokerobject.addtopic(data[2],data[3])
      else:
        c.send("Topic {} is not available".format(data[2]).encode())
          
    elif data[1] == 'delete': #delete argument
      if data[2] in brokerobject.topic.keys():
        brokerobject.deletetopic(data[2],data[3])
      else:
        c.send("Topic {} is not available".format(data[2]).encode())
    
  
  elif data[0] == 'consumer.py': 
    if data[1] == 'subscribe':  #Subscribe arguement
      if data[2] not in brokerobject.topic.keys():
        c.send("Topic {} is not available".format(data[2]).encode())
      else:
            
  else:
    c.send('Please try again'.encode())

  c.send('Thank you for connecting'.encode())
  
    # Close the connection with the client
  c.close()





