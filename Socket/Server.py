import socket

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Crea un socket TCP
    server_socket.bind(('127.0.0.1', 12345))  # Indirizzo e porta
    server_socket.listen(5)
    print("Server in ascolto sulla porta 12345...")
    while(1):
        conn, addr = server_socket.accept() # Accetta una connessione
        print(f"Connessione stabilita con {addr}")

        data = conn.recv(1024).decode() # Riceve il messaggio dal client
        print(f"Messaggio ricevuto: {data}")

        response = "Ciao dal server!" # Risposta del server
        conn.send(response.encode()) # Invia la risposta al client

        conn.close() # Chiude la connessione
    
    server_socket.close() # Chiude il socket del server                     

if __name__ == "__main__":
    start_server() # Avvia il server
