import socket
import threading

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 12345))

nickname = input("Choose your nickname: ")

def receive():
    while True:
        try: 
            message = client.recv(1024).decode('utf-8')
            if message == 'NICK':
                client.send(nickname.encode('utf-8'))
            else:
                print(message)
        except:
            print("An error occurred!")
            client.close()
            break


def write():
    while True:
        try:
            message = input("")  # Get user input
            if message.lower() == '/quit':  # Add quit command
                client.close()
                break
            full_message = f'{nickname}: {message}'
            client.send(full_message.encode('utf-8'))
        except Exception as e:
            print(f"Error sending message: {e}")
            client.close()
            break


receive_thread = threading.Thread(target=receive)
receive_thread.start()
write_thread = threading.Thread(target=write)
write_thread.start()