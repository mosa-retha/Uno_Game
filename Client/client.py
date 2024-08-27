import socket

from Client.client_helper import ClientHelper


def user_input(prompt):
    _input = ""
    while len(_input) == 0:
        _input = input(prompt)

    return _input


class Client:
    def __init__(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host, port = 'localhost', 12345
        self.connect_to_server(host, port)

    def connect_to_server(self, host, port):
        self.client_socket.connect((host, port))

    def start(self):
        client_helper = ClientHelper(client.client_socket)
        client_helper.start()
        while True:
            response = f"{user_input('please enter a name:')}!"
            self.client_socket.send(response.encode('utf-8'))


if __name__ == '__main__':
    client = Client()
    client.start()

