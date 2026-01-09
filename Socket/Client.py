import socket

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Crea un socket TCP
    client_socket.connect(('localhost', 12345)) # Connette al server

    message = "Ciao dal client!"
    client_socket.sendall(message.encode()) # Invia il messaggio al server

    data = client_socket.recv(1024).decode() # Riceve la risposta dal server
    print(f"Risposta dal server: {data}")

    client_socket.close() # Chiude la connessione

if __name__ == "__main__": 
    start_client # Avvia il client
