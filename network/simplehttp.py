#!/usr/local/bin/python3

import http.client

h = http.client.HTTPConnection('www.google.com')
h.request("GET", "/")
data = h.getresponse()
print(data.code)
print(data.headers)