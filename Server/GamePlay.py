import threading


class GamePlay(threading.Thread):
    def __init__(self, _socket, address, server, player):
        super().__init__()
        self.client_socket = _socket
        self.client_address = address
        self.player = player  # Assuming player is an instance of Player
        self.ready = threading.Event()  # Event to control the flow
        self.server = server

    def run(self):
        while True:
            print(f"Waiting for {self.player.name}'s turn...")
            self.ready.wait()  # Wait for the server to signal this player's turn
            print(f"{self.player.name}'s turn has started.")
            message = f"Your turn to play, {self.player.name}!"
            self.client_socket.sendall(message.encode('utf-8'))

            # Wait to receive the client's move/response
            data = self.client_socket.recv(1024).decode('utf-8')
            if not data:
                print(f"Connection lost with {self.client_address}")
                break  # Exit if the connection is lost

            print(f"Received from client {self.client_address}: {data}")

            # Notify the server that this player's turn is complete
            self.server.notify_done(self)

        # Clean up after the loop ends (if the client disconnects)
        self.client_socket.close()
