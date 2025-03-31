import socket

sock = socket.socket()

sock.bind(('', 9090))
sock.listen(1)

conn, addr = sock.accept()

print(f'connected: {addr}')
msg = 'Give me a, b, c to solve quadratic equation!'
conn.send(msg.encode())

data = conn.recv(1024)
data = data.decode("utf-8")
a, b, c = map(float, data.split())
D = b**2 - 4*a*c
if D < 0:
    conn.send(b'No solution!')
elif D == 0:
    x = (-b + D**0.5) / (2*a)
    resp = f'One solution: {x}'
    conn.send(resp.encode('utf-8'))
elif D > 0:
    x1 = (-b + D**0.5) / (2*a)
    x2 = (-b - D**0.5) / (2*a)
    resp = f'Two solutions: {x1}, {x2}'
    conn.send(resp.encode('utf-8'))

conn.close()