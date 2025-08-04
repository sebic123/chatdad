import socket

s =  socket.socket()
print('Socket created')


s.bind(('localhost',12345))

s.listen(2)
print('Waiting for connection...')


while True:
  c, addr = s.accept()
  print('Got connection from', addr)

  c.send(bytes('Thank you for connecting', 'utf-8'))
   
  c.close()