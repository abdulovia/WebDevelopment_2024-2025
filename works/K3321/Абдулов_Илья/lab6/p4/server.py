import socket
import threading

clients = []

def handle_client(conn):
    nickname = conn.recv(1024).decode()
    clients.append(conn)
    print(f"{nickname} connected")
    
    try:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            message = f"{nickname}: {data.decode()}"
            print(message)
            for client in clients:
                if client != conn:
                    client.send(message.encode())
    except:
        pass
    finally:
        clients.remove(conn)
        conn.close()
        print(f"{nickname} disconnected")

sock = socket.socket()
sock.bind(('', 5555))
sock.listen(5)
print("Server is running...")

while True:
    conn, addr = sock.accept()
    threading.Thread(target=handle_client, args=(conn,)).start()