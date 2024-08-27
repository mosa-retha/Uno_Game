import threading
import socket


class GamePlay(threading.Thread):
    def __init__(self, _socket, address):
        super().__init__()
        self.socket = _socket
        self.client_address = address
        self.player = player
        self.ready = threading.Event()
        self.server = server

    def run(self):
        start = True
        print("Welcome to UNO!")

        while start:
            self.ready.wait()
            message = "Your turn to play!" + self.player.name
            self.client_socket.sendall(message.encode())
            data = self.client_socket.recv(1024).decode('utf-8')
            print(f"Received from client: {data}")
            self.server.notify_done(self)


