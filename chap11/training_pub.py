print("####### 11-4 ##########")
import redis
conn = redis.Redis()

chocos = ['choco1','choco2','choco3']
for choco in chocos:
    msg = choco.encode('utf-8')
    conn.rpush('chocos',msg)
    
conn.rpush('chocos','quit'.encode('utf-8'))

