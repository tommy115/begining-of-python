import zmq

host = '127.0.0.1'
port = 6789

context = zmq.Context()
server = context.socket(zmq.REP)
server.bind("tcp://{0}:{1}".format(host,port))

while True:
    request_bytes = server.recv()
    request_str = request_bytes.decode('utf-8')
    print("That voice in my head says: {0}".format(request_str))
    reply_str = "Stop saying: {0}".format(request_str)
    reply_bytes = bytes(reply_str, 'utf-8')
    server.send(reply_bytes)

