import socket

from GamePlay import GamePlay

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = 'localhost'
port = 12345

server_socket.bind((host, port))

server_socket.listen()

print(f"Server listening on {host}:{port}...")
start = True
while True:
    client_socket, addr = server_socket.accept()
    print(f"Got a connection from {addr}")

    message = "Welcome to UNO!" + "\n"
    client_socket.send(message.encode('utf-8'))


    data = client_socket.recv(1024).decode('utf-8')

    print(f"Received from client: {data}")

    thread = GamePlay(client_socket, addr)
    thread.start()
