import zmq
from datetime import datetime 

#address = ('localhost', 6790)
#host = 'localhost'
host = '127.0.0.1'
port = 6790
max_size = 1000

#server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#server.bind(address)

#server.listen(5)

context = zmq.Context()
server = context.socket(zmq.REP)
server.bind("tcp://%s:%s" % (host, port) )

#client, addr = server.accept()
#data = client.recv(max_size)
#client_data = data.decode('utf-8')

while True:
    request = server.recv()
    request_str = request.decode('utf-8')
    
    if request_str.find("time") != -1:
        this_localtime = datetime.now().isoformat()
        server.send(this_localtime.encode('utf-8'))
    else:
        print("cannot find time")
    
