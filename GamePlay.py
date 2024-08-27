import threading
import socket


class GamePlay(threading.Thread):
    def __init__(self, _socket, address):
        super().__init__()
        self.socket = _socket
        self.client_address = address

    def run(self):
        start = True
        print("Welcome to UNO!")
        while start:
            message = "what do you want to do?\n"
            self.socket.send(message.encode('utf-8'))
            data = self.socket.recv(1024).decode('utf-8')
            print(data)
