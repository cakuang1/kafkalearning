## Producer API
import socket

# Methods

c = socket.socket()
def createtopic(topicname,host,port):

    c.connect((host,port))
    args = ['producer.py','createtopic',topicname]
    data = pickle.dumps(args)     
    s.send(data)
    print (s.recv(1024).decode())


def deletetopic(topicname,host,port):
    c.connect((host,port))
    args = ['producer.py','deletetopic',topicname]
    data = pickle.dumps(args)     
    s.send(data)
    print (s.recv(1024).decode())

def add(  ):
    


def delete():
