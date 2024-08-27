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

            thread = GamePlay(client_socket, addr, self, Player(data))
            thread.start()

            with self.lock:
                self.clients.append(thread)

            if len(self.clients) == 2:
                print("Game is starting")
                self.deal()
                self.start_round()

    def start_round(self):
        with self.lock:
            if self.clients:
                current_client = self.clients[self.current_client_index]
                current_client.ready.set()

    def notify_done(self, client):
        """Called by a client handler when it's done with its turn."""
        with self.lock:
            # Move to the next client
            client.ready.clear()
            self.current_client_index = (self.current_client_index + 1) % len(self.clients)
            self.start_round()

    def deal(self):
        cards = Cards()
        dealer = Dealer([client.player for client in self.clients], cards)
        dealer.deal_cards()
        for client in self.clients:
            client.client_socket.sendall(f"Your cards: {client.player.players_cards}".encode('utf-8'))


if __name__ == '__main__':
    server = Server()
    server.start_server()
