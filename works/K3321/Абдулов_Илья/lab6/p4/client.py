import socket
import threading

def receive(client):
    while True:
        try:
            data = client.recv(1024).decode()
            print(data)
        except:
            print("Disconnected")
            client.close()
            break

client = socket.socket()
client.connect(('localhost', 5555))

nickname = input("Nickname: ")
client.send(nickname.encode())

threading.Thread(target=receive, args=(client,)).start()

while True:
    msg = input()
    if msg.lower() == 'exit':
        break
    client.send(msg.encode())

client.close()