import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = 'localhost'
port = 12345

client_socket.connect((host, port))

message = client_socket.recv(1024).decode('utf-8')
print(f"Message from server: {message}")


def user_input(prompt):
    _input = ""
    while len(_input) == 0:
        _input = input(prompt)

    return _input


while True:

    response = f"{user_input('please enter a name:')}!"
    client_socket.send(response.encode('utf-8'))

    message = client_socket.recv(1024).decode('utf-8')
    print(f"Message from server: {message}")


