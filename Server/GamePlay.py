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
            top_card = self.cards.discard_pile[-1]
            message = (f"Current card: {top_card}" + "\n" +
                       f"Your turn to play, {self.player.name}!" + "\n" +
                       "Your cards: " + str(self.player.players_cards) + "\n")
            self.client_socket.sendall(message.encode('utf-8'))

            # Wait to receive the client's move/response
            data = self.client_socket.recv(1024).decode('utf-8')
            if not data:
                print(f"Connection lost with {self.client_address}")
                break  # Exit if the connection is lost

            print(f"Received from client {self.client_address}: {data}")


            var = self.player.players_cards[int(data)]
            if not top_card.validate_move(var):
                print(f"Invalid move: {var}")
                self.client_socket.sendall("Invalid move. Try again.".encode('utf-8'))
                continue

            print(f"Card played: {var}")
            self.cards.discard_pile.append(var)
            self.player.players_cards.remove(var)

            # Notify the server that this player's turn is complete
            self.server.notify_done(self)

        # Clean up after the loop ends (if the client disconnects)
        self.client_socket.close()

    def validate_move(self, card):
        """Validate the move."""
        if card.validate_move(self.cards.discard_pile[-1]):
            return True
