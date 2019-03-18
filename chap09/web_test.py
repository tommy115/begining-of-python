import urllib.request as ur
url = 'https://raw.githubusercontent.com/koki0702/introducing-python/master/dummy_api/fortune_cookie_random1.txt'
conn = ur.urlopen(url)
print("###########print connection########")
print(conn)

data = conn.read()
print("###########print read data########")
print(data)

print("###########print status########")
print(conn.status)

print("###########print Content-Tyoe########")
print(conn.getheader('Content-Type'))

print("###########print header########")
for key, value in conn.getheaders():
    print(key, value)
