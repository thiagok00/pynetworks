#!/usr/local/bin/python3
import socket

# use `nc localhost 9898` to send a message
size = 512
host = ''
port = 9898

# family = internet, type = stream, which means TCP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

sock.bind((host, port))
sock.listen(5)

c, addr = sock.accept()
data = c.recv(size)

if data:
  msg = data.decode("utf-8")
  print(f"connection from {addr[0]} : {msg}")
sock.close()
