print("####### 11-1 ##########")

import socket

address = ('localhost', 6789)
max_size = 1000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(address)

client.send(b'time')
data = client.recv(max_size)

print(data)
print(data.decode('utf-8'))
client.close()

print("####### 11-2 ##########")
import zmq

host = '127.0.0.1'
port = 6790

context = zmq.Context()
client = context.socket(zmq.REQ)
client.connect("tcp://%s:%s" % (host, port))

request_bytes = "time".encode('utf-8')
client.send(request_bytes)
reply_bytes = client.recv()
print(reply_bytes.decode('utf-8'))

print("####### 11-3 ##########")
import xmlrpc.client

proxy = xmlrpc.client.ServerProxy("http://localhost:6791/")
now = proxy.this_time()

print(now)

print("####### 11-4 ##########")
import redis
conn = redis.Redis()

chocos = ['choco1','choco2','choco3']
for choco in chocos:
    msg = choco.endoce('utf-8')
    conn.rpush('chocos',msg)
    
conn.rpush('chocos','quit'.encode('utf-8'))
conn.close()
