import socket
import json
import time

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    for x in range(20):
        s.sendall(b"get_data")
        data = s.recv(1025)
        if data:
            response = json.loads(data.decode())
            print(response)
        time.sleep(2)

    s.sendall(b"QUIT")
    data = s.recv(1024)
    if data:
        response = data.decode()
        print(response)
