import redis

conn = redis.Redis()
print("all keys")
print(conn.keys('*'))
print(conn.mget(conn.keys('*')))

print("each data")
print(conn.get('secret'))
print(conn.get('carats'))
print(conn.get('fever'))

#conn.setnx('secret','icky-icky-icky-ptang-zoop-boing')
