import socket 
import threading

host = 'localhost'
port = 12345

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(2)
print(f'Server started on {host}:{port}')

clients = []
nicknames = []

def broadcast(message):
    for client in clients:
        client.send(message)


def handle_client(client):
    while True: 
        try:         
            message = client.recv(1024)
            broadcast(message)
        except: 
               index = clients.index(client)
               clients.remove(client)
               nickname = nicknames[index]
               broadcast(f'{nickname} has left the chat.'.encode('utf-8'))
               nicknames.remove(nickname)
               break


def receive():
            while True:
                client, address = server.accept()
                print(f'Connected with {str(address)}')

                client.send('NICK'.encode('utf-8'))
                nickname = client.recv(1024).decode('utf-8')
                nicknames.append(nickname)
                clients.append(client)

                print(f'Nickname of the client is {nickname}')
                broadcast(f'{nickname} has joined the chat.'.encode('utf-8'))
                client.send('Connected to the server!'.encode('utf-8'))
                client.send(f' Welcome in the chat {nickname}!'.encode('utf-8'))

                thread = threading.Thread(target=handle_client, args=(client,))
                thread.start()

print('Server is listening...')
receive()                