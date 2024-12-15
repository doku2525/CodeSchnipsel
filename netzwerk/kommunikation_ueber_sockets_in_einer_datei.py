import socket
import threading
import json
import time

from decoratoren.vereinfache_meine_try_except_bloecke import mein_test_mit_prognose, test

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)
BUFFER_SIZE = 1024
CLIENT_INDENT = 8


def prozess_server(ip_adresse: str, port_nr: int, name: str = 'SERVER'):
    """ socket.socket()
          family: AddressFamily => socket.AF_INET = IPv4-Sockets, socket.AF_INET6 -> IPv6-Sockets
          type: SocketKind => socket.SOCK_STREAM = TCP-Sockets, socket.SOCK_DGRAM = UDP-Sockets """
    with socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM) as s:
        print(f"{name}: Beginne mit der Arbeit")
        socket_opt = socket.SOL_SOCKET, socket.SO_REUSEADDR, 1
        s.setsockopt(*socket_opt)  # Optionen im Socket setzen. Schnelles Aufrufen
        # PORT > 1023 = nicht-privilegierte Ports. siehe z.B. Port 80 fuer HTTP etc.
        s.bind((ip_adresse, port_nr))       # Binde den Socket zu der Adresse
        s.listen()                 # "Lausche" am Socket, ob ueber die mit dem Socket verbundene Adresse kommen
        conn, addr = s.accept()    # Akzeptiere alle Verbindungsanfragen. Bis eine Anfrage kommt, geht es nicht weiter.
        # Jetzt sind Server und Client miteinander verbunden und der Austausch von Daten kann beginnen
        anfragen = 0
        with conn:
            print(f"{name}: Verbunden ueber Adresse {addr}")
            while True:
                data = conn.recv(BUFFER_SIZE)
                if not data:
                    break
                command = data.decode()
                if command == "QUIT":
                    conn.sendall(b"Beende Programm")
                    print(f"{name}: Befehl zum Beenden des Programms vom Client {addr} erhalten!")
                    break
                elif command == "get_data":
                    data = json.dumps({"message": "Hallo vom server!", "number": (anfragen := anfragen + 1)})
                    conn.sendall(data.encode())
                    print(f"{name}: Datenanfrage Nummer {anfragen} vom Client {addr} bearbeitet und Daten gesendet")
                else:
                    conn.sendall(b"Unbekanntes Kommando")
    print(f"{name}: Beende die Arbeit!")


def prozess_client(ip_adresse: str, port_nr: int, name: str = 'Client'):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        print("\t" * CLIENT_INDENT + f"{name}: Beginne mit der Arbeit")
        s.connect((ip_adresse, port_nr))     # Verbindung mit dem Socket unter der Adresse herstellen  connect() vs bind()
        # Jetzt sind Server und Client miteinander verbunden und der Austausch von Daten kann beginnen
        remote_ip, remote_port = s.getpeername()
        print("\t" * CLIENT_INDENT + f"{name}: Bin verbunden mit {remote_ip} {remote_port}")
        for x in range(5):
            print("\t" * CLIENT_INDENT + f"{name}: Frage Daten an")
            s.sendall(b"get_data")      # Sende Daten als ByteString. Kurzform fuer "get_data".encode()
            data = s.recv(BUFFER_SIZE)      # Empfange Daten
            if data:
                received_string = data.decode()  # Dekodiere die empfangenen Daten von ByteString zu String
                response = json.loads(received_string)    # Konvertiere String zu JSON, da Server JSON geschickt hat
                print("\t" * CLIENT_INDENT + f"{name}: Erhaltene Daten => {response}")
            time.sleep(0.5)

        print("\t" * CLIENT_INDENT + f"{name}: Sende QUIT")
        s.sendall(b"QUIT")
        data = s.recv(BUFFER_SIZE)
        if data:
            response = data.decode()
            print("\t" * CLIENT_INDENT + f"{name}: Letzte Nachricht vom SERVER <<{response}>>")
    print("\t" * CLIENT_INDENT + f"{name}: Beende die Arbeit!")


@mein_test_mit_prognose(True)
def verbinde_server_mit_client_eins():
    server_thread = threading.Thread(target=prozess_server, kwargs={'ip_adresse': HOST, 'port_nr': PORT})
    server_thread.start()
    client_thread = threading.Thread(target=prozess_client, args=(HOST, PORT))
    client_thread.start()


IPAdresse = tuple[str, int]


def erzeuge_socket_server(ip_adresse: str, port_nr: int, name: str = 'SERVER'
                          ) -> tuple[socket.socket, IPAdresse, str]:
    with socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM) as s:
        print("\t" * CLIENT_INDENT + f"{name}: Beginne mit der Arbeit")
        socket_opt = socket.SOL_SOCKET, socket.SO_REUSEADDR, 1
        s.setsockopt(*socket_opt)
        s.bind((ip_adresse, port_nr))
        s.listen()
        return s.accept() + (name,)


def erzeuge_socket_client(ip_adresse: str, port_nr: int, name: str = 'Client'
                          ) -> tuple[socket.socket, str]:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        print("\t" * CLIENT_INDENT + f"{name}: Beginne mit der Arbeit")
        s.connect((ip_adresse, port_nr))
        remote_ip, remote_port = s.getpeername()
        print("\t" * CLIENT_INDENT + f"{name}: Bin verbunden mit {remote_ip} {remote_port}")
        return s, name


@mein_test_mit_prognose(True)
def versuche_socket_server_und_socket_client_zu_erzeugen():
    server_thread = threading.Thread(target=erzeuge_socket_server, kwargs={'ip_adresse': HOST, 'port_nr': PORT})
    client_thread = threading.Thread(target=erzeuge_socket_client, args=(HOST, PORT))
    server_thread.start()
    time.sleep(0.5)
    client_thread.start()

# TODO #########################
#   Bis hier erfolgreich


def client_sende_und_empfange(server: socket.socket, befehl: str, buffer_size: int = 1024) -> str:
    server.sendall(befehl.encode())  # Sende Daten als ByteString
    data = server.recv(buffer_size)  # Empfange Daten
    return data.decode() if data else ''


def kommuniziere_mit_server(socket_server: socket.socket, name: str = 'Client') -> None:
    remote_ip, remote_port = socket_server.getpeername()

    print("\t" * CLIENT_INDENT + f"{name}: Bin verbunden mit {remote_ip} {remote_port}")
    for x in range(5):
        print("\t" * CLIENT_INDENT + f"{name}: Frage Daten an")
        response = json.loads(client_sende_und_empfange(socket_server, "get_data", BUFFER_SIZE))
        print("\t" * CLIENT_INDENT + f"{name}: Erhaltene Daten => {response}")
        time.sleep(0.5)

    print("\t" * CLIENT_INDENT + f"{name}: Sende QUIT")
    response = client_sende_und_empfange(socket_server, 'QUIT', BUFFER_SIZE)
    print("\t" * CLIENT_INDENT + f"{name}: Letzte Nachricht vom SERVER <<{response}>>")
    print("\t" * CLIENT_INDENT + f"{name}: Beende die Arbeit!")


kommandos = {
    'QUIT': [lambda: 'Beende Programm',
             lambda: f"{name}: Befehl zum Beenden des Programms vom Client {ipadress} erhalten!"],
    'get_data': [lambda: json.dumps({"message": "Hallo vom server!", "number": anfragen}),
                 lambda: f"{name}: Datenanfrage Nummer {anfragen} vom Client {ipadress} bearbeitet und Daten gesendet"]
}


def server_empfange_kommando(client: socket.socket, buffer_size: int = 1024) -> str:
    data = client.recv(buffer_size)
    return data.decode() if data else ''


def server_sende_daten(client: socket.socket, daten: str) -> str:
    client.sendall(daten.encode())
    return daten


def kommuniziere_mit_client(connection: socket.socket, ipadress: IPAdresse, name: str = 'SERVER') -> None:
    with connection:
        print(f"{name}: Verbunden ueber Adresse {ipadress}")
        kommando = True
        while kommando:
            daten, output = kommandos.get(server_empfange_kommando(connection, BUFFER_SIZE), "Unbekanntes Kommando")
            kommando = server_sende_daten(connection, daten())
            print(output()) if kommando else None
    print(f"{name}: Beende die Arbeit!")


@mein_test_mit_prognose(True)
def versuche_socket_server_und_socket_client_kommunizieren_zu_lassen():
    server_thread = threading.Thread(target=erzeuge_socket_server, kwargs={'ip_adresse': HOST, 'port_nr': PORT})
    client_thread = threading.Thread(target=erzeuge_socket_client, args=(HOST, PORT))
    server_thread.start()
    time.sleep(0.5)
    client_thread.start()

# IPAdresse = tuple[str, int]
#
#
#
#
#
# def server_daten_verfuegbar(connection: socket.socket) -> bool:
#     """Überprüft, ob Daten für die Verbindung verfügbar sind."""
#     return connection.recv(1) != b''
#
#
# def server_empfange_daten(connection: socket.socket) -> str:
#     """Empfängt Daten von der Verbindung und decodiert sie."""
#     daten = connection.recv(BUFFER_SIZE)
#     return daten.decode()
#
#
# def server_sende_daten(connection: socket.socket, daten: str) -> None:
#     """Sendet Daten über die Verbindung."""
#     connection.sendall(daten.encode())
#
#
# def sende_daten_an_client(connection: socket.socket, ipadress: IPAdresse, daten: str) -> str:
#     connection.sendall(daten.encode())
#
#


if __name__ == '__main__':
    verbinde_server_mit_client_eins()
    # versuche_socket_server_und_socket_client_zu_erzeugen()

