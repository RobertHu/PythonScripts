from socket import socket ,AF_INET, SOCK_STREAM
import ssl

s = socket(AF_INET,SOCK_STREAM)
s.connect(('localhost',8888))
c = ssl.wrap_socket(s)
print('connected')
c.send(b'hello')
