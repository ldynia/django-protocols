#!/usr/bin/env python3

from xmlrpc.client import ServerProxy

client = ServerProxy('http://localhost:8080/api/rpc')

print('add', client.add(2, 3))
print('upper', client.upper('hello'))
print('reverse', client.reverse('live'))
print('swap', client.swap({'a' : 'one', 'b': 'two'}))
