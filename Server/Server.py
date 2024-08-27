import socket
import threading

from Domain.Cards import Cards
from Domain.Player import Player
from Domain.Dealer import Dealer
from GamePlay import GamePlay


class Server:
    def __init__(self):
        self.current_client_index = 0
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = 'localhost'
        self.port = 12345
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(2)
        self.lock = threading.Lock()
        self.clients = []

    def start_server(self):
        print(f"Server listening on {self.host}:{self.port}...")
        while True:
            client_socket, addr = self.server_socket.accept()
            print(f"Got a connection from {addr}")

            message = "Welcome to UNO!" + "\n"
            client_socket.send(message.encode('utf-8'))

            data = client_socket.recv(1024).decode('utf-8')

            print(f"Received from client: {data}")

    thread = GamePlay(client_socket, addr)
    thread.start()
