import socket

from wsproto import WSConnection
from wsproto.connection import ConnectionType
from wsproto.events import Request


ws = WSConnection(ConnectionType.CLIENT)

request = Request(host='localhost:8080', target='/')
data = ws.send(request)

print(data)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("localhost", 8080))
sock.send(data)

while True:
    for event in ws.events():
        if isinstance(event, AcceptConnection):
            print('Connection established')
        elif isinstance(event, RejectConnection):
            print('Connection rejected')
        elif isinstance(event, CloseConnection):
            print('Connection closed: code={} reason={}'.format(event.code, event.reason))
            sock.send(ws.send(event.response()))
        elif isinstance(event, Ping):
            print('Received Ping frame with payload {}'.format(event.payload))
            sock.send(ws.send(event.response()))
        elif isinstance(event, TextMessage):
            print('Received TEXT data: {}'.format(event.data))
            if event.message_finished:
                print('Message finished.')
        elif isinstance(event, BytesMessage):
            print('Received BINARY data: {}'.format(event.data))
            if event.message_finished:
                print('BINARY Message finished.')
        else:
            print('Unknown event: {!r}'.format(event))