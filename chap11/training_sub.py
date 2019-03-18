import redis
import time
conn = redis.Redis()

print('choco starting')
while True:
    msg = conn.blpop('chocos')
    if not msg:
        break
    val = msg[1].decode('utf-8')
    if val == 'quit':
        break
    time.sleep(0.5)
    print('enveloped', val)
    rest_list = conn.lrange('chocos', 0, -1)
    print(len(rest_list))
    

print('enveloped all chocos')
