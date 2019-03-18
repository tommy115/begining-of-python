from xmlrpc.server import SimpleXMLRPCServer
from datetime import datetime

def this_time():
    return datetime.now()

server = SimpleXMLRPCServer(("localhost", 6791))
server.register_function(this_time, "this_time")
server.serve_forever()
