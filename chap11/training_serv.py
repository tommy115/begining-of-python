import socket
from datetime import datetime 
import re

address = ('localhost', 6789)
max_size = 1000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(address)

server.listen(5)

client, addr = server.accept()
data = client.recv(max_size)
client_data = data.decode('utf-8')

if client_data.find("time") != -1:
    this_localtime = datetime.now().isoformat()
    client.sendall(this_localtime.encode('utf-8'))
else:
    print("cannot find time")
    
client.close()
server.close()
