import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 43523  # The port used by the server


s = socket.socket()
s.bind(HOST,43523)


s.connect(HOST,12345)













