import socket
sock = socket.socket()
ip_port = ('127.0.0.1',8080)

sock.bind(ip_port)
sock.listen(5)


while True:
    print('server waiting...')
    conn, addr = sock.accept()

    client_data = conn.recv(1024)
    print(client_data)
    conn.send(b'123123')

    conn.close()


