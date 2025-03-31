import socket

with socket.socket() as sock:
    sock.connect(('localhost', 9090))

    while True:
        data = sock.recv(1024)
        if not data:
            break
        print(data.decode())
