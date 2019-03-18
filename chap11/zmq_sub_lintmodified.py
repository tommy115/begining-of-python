'''
zmq のサブスクライバテスト
'''
import zmq

HOST = '127.0.0.1'
PORT = 6789

ctx = zmq.Context()
sub = ctx.socket(zmq.SUB)
sub.connect('tcp://%s:%s' % (HOST, PORT))
topics = ['maine coon', 'persian']

for topic in topics:
    sub.setsockopt(zmq.SUBSCRIBE, topic.encode('utf-8'))

while True:
    cat_bytes, hat_bytes = sub.recv_multipart()
    cat = cat_bytes.decode('utf-8')
    hat = hat_bytes.decode('utf-8')
    print('subscribe: %s wears a %s' % (cat, hat))
