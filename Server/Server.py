from concurrent.futures import ThreadPoolExecutor
import socket

from Domain.Cards import Cards
from Domain.Player import Player
from Domain.Dealer import Dealer
from GamePlay import GamePlay


class Server:
    """Server class that listens for incoming connections and starts the game."""

    def __init__(self):
        self.current_client_index = 0
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = 'localhost'
        self.port = 12345
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(2)
        self.executor = ThreadPoolExecutor(max_workers=2)
        self.clients = []
        self.cards = Cards()

    def start_server(self):
        """Start the server and listen for incoming connections."""
        print(f"Server listening on {self.host}:{self.port}...")
        while True:
            client_socket, addr = self.server_socket.accept()
            print(f"Got a connection from {addr}")

            message = "Welcome to UNO!" + "\n"
            client_socket.send(message.encode('utf-8'))

            data = client_socket.recv(1024).decode('utf-8')

            print(f"Received from client: {data}")

            player = Player(data)
            game_play = GamePlay(client_socket, addr, self, player, self.cards)
            self.executor.submit(game_play.run)

            self.clients.append(game_play)

            if len(self.clients) == 2:
                print("Game is starting")
                self.deal()
                self.start_round()

    def start_round(self):
        """Start a new round."""
        if self.clients:
            current_client = self.clients[self.current_client_index]
            print(f"Starting turn for {current_client.player.name} (index: {self.current_client_index})")
            current_client.ready.set()
        else:
            print("No clients connected.")

    def notify_done(self, client):
        """Notify the server that the client is done with their turn."""
        print(f"{client.player.name} has finished their turn.")
        client.ready.clear()
        self.current_client_index += 1
        if self.current_client_index == len(self.clients):
            self.current_client_index = 0
        print(f"Next client index: {self.current_client_index}")
        self.start_round()
        print("start_round was called successfully.")

    def deal(self):
        """Deal cards"""
        dealer = Dealer([client.player for client in self.clients], self.cards)
        dealer.deal_cards()
        for client in self.clients:
            client.client_socket.sendall(f"Your cards: {client.player.players_cards}".encode('utf-8'))


if __name__ == '__main__':
    server = Server()
    server.start_server()
