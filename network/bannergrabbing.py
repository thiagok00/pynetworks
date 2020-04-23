#!/usr/local/bin/python3
import socket
import re


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('www.microsoft.com',80))

http_get = b"GET / HTTP/1.1\nHost: www.microsoft.com\n\n"
data = ''
try:
  sock.sendall(http_get)
  data = sock.recvfrom(1024)
except socket.error:
  print(socket.errno)
finally:
  sock.close()

strdata = data[0].decode("utf-8")
headers = strdata.splitlines()

print(strdata)
for s in headers:
  if re.search('Server:', s):
    s = s.replace('Server: ', "")
    print(s)
