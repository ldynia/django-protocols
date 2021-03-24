#!/usr/bin/env python3


from xmlrpc.client import ServerProxy

# Transport: HTTP
client = ServerProxy('http://localhost:8080/api/rpc/xml')

# Encoding: XML
print('add(2, 3)', client.add(2, 3))
print("upper('hello')", client.upper('hello'))
print("reverse('live')", client.reverse('live'))
print("swap({'a' : 'one', 'b': 'two'})", client.swap({'a' : 'one', 'b': 'two'}))