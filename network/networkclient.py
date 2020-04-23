#!/usr/local/bin/python3
import socket

# make sure to run `ncl -l 5555` to listen to port
host='localhost'

# family = internet, type = stream, which means TCP
mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr=(host,5555)
mysocket.connect(addr)

try:
  msg=b"hi, this is a test\n" #array of bits
  mysocket.sendall(msg)
except socket.errno as e:
  print("Socket error", e)
finally:
  mysocket.close()
