import socket

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))

    while True:
        partenza = input("Inserisci la città di partenza: ")
        arrivo = input("Inserisci la città di arrivo: ")
        message = f"{partenza};{arrivo}"
        client_socket.send(message.encode())
        data = client_socket.recv(1024).decode()
        print(f"Disponibilità: {data}")

    client_socket.close()

if __name__ == "__main__":
    start_client