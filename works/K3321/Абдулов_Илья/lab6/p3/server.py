import socket

with socket.socket() as sock:
    sock.bind(('', 9090))
    sock.listen(1)

    conn, addr = sock.accept()

    with open("index.html") as f:
        data = f.read()
        conn.send(data.encode())
