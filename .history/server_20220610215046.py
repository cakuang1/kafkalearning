## Utilize socker programming

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


print ("Socket successfully created")


port = 12345 


s.bind(('', port))        
print ("socket binded to %s" %(port))


if __name__ == '__'


