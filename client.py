import socket

c = socket.socket()
print('trying to connect...')
c.connect(('localhost',12345))
print('Connected to server')
