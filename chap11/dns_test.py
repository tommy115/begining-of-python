import socket

sample_host = 'www.crappytaxidermy.com'
print(socket.gethostbyname(sample_host))
print(socket.gethostbyname_ex(sample_host))

print(socket.getaddrinfo(sample_host, 80))
print(socket.getaddrinfo(sample_host, 80, socket.AF_INET, socket.SOCK_STREAM))

print(socket.getservbyname('http'))
print(socket.getservbyport(80))
