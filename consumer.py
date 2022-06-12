import socket
import sys
import pickle





HOST = "127.0.0.1"  # The server's hostname or IP address







def connect():
    s = socket.socket()
    s.connect((HOST,12345))
    arguments = sys.argv
    data = pickle.dumps(arguments)    
    s.send(data)

    print (s.recv(1024).decode())






if __name__ == '__main__':
    connect()














