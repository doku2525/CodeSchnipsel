import socket
import json

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print(f"Beginne ...")
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1025)
            if not data:
                break
            command = data.decode()
            if command == "QUIT":
                conn.sendall(b"Beende Programm")
                print(f"Beende Programm")
                break
            elif command == "get_data":
                data = json.dumps({"message": "Hello from server!", "number": 42})
                conn.sendall(data.encode())
                print(f"Anfrage vom Client bearbeitet und Antwort gesendet")
            else:
                conn.sendall(b"Unknown command")
