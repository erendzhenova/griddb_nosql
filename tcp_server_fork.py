import os
import socket
import sys

server_socket = socket.socket()
server_socket.bind(('0.0.0.0', 2222))
server_socket.listen(10)

while True:
    client_socket, remote_address = server_socket.accept()
    child_pid = os.fork()
    if child_pid == 0:
        data = client_socket.recv(1024)
        client_socket.send(data)
        if not data or data == 'close': # Закрывает соединение при получении сообщения с текстом close
            client_socket.close()
        client_socket.send(data)
        sys.exit()
    else:
        client_socket.close()

server_socket.close()
