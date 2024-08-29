import threading


class GamePlay(threading.Thread):
    def __init__(self, _socket, address, server, player, cards):
        super().__init__()
        self.client_socket = _socket
        self.client_address = address
        self.player = player
        self.ready = threading.Event()
        self.server = server
        self.cards = cards

    def run(self):
        while True:
            print(f"Waiting for {self.player.name}'s turn...")
            self.ready.wait()
            print(f"{self.player.name}'s turn has started.")
            message = (f"Current card: {self.cards.discard_pile[-1]}" + "\n" +
                       f"Your turn to play, {self.player.name}!" + "\n" +
                       "Your cards: " + str(self.player.players_cards) + "\n")
            self.client_socket.sendall(message.encode('utf-8'))

            # Wait to receive the client's move/response
            data = self.client_socket.recv(1024).decode('utf-8')
            if not data:
                print(f"Connection lost with {self.client_address}")
                break  # Exit if the connection is lost

            print(f"Received from client {self.client_address}: {data}")
            # printing the first card in the player's hand
            print(f"First card in player's hand: {self.player.players_cards[0]}")
            card_index = int(data)
            var = self.player.players_cards[card_index]
            print(f"Card played: {var}")
            self.cards.discard_pile.append(var)
            self.player.players_cards.remove(var)

            # Notify the server that this player's turn is complete
            self.server.notify_done(self)

        # Clean up after the loop ends (if the client disconnects)
        self.client_socket.close()
