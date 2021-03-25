#!/usr/bin/env python3

from xmlrpc.client import ServerProxy


try:
    # Transport: HTTP, Encoding: XML
    client = ServerProxy('http://localhost:8080/api/rpc/xml')
except:
    print('Error: Could not connect to server!')

print('add(2, 3)', client.add(2, 3))
print("upper('hello')", client.upper('hello'))
print("reverse('live')", client.reverse('live'))
print("swap({'left': 'right'})", client.swap({'left': 'right'}))