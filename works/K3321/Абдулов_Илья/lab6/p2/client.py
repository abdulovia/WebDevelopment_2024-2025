import socket

sock = socket.socket()
sock.connect(('localhost', 9090))

data = sock.recv(1024)
print(data.decode())

params = input('Enter parameters of equation: ')

sock.send(params.encode())

data = sock.recv(1024)
print(data.decode())

sock.close()
