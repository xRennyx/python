import socket

def start_client():
    # Inizializzazione lato client della socket su porta 12345
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))

    # Logica di richiesta al server
    while True:
        # Inserimento città di partenza e arrivo
        partenza = input("Inserisci la città di partenza: ")
        arrivo = input("Inserisci la città di arrivo: ")

        # Creazione messaggio (formato semplice)
        richiesta = partenza + "," + arrivo

        # Invio richiesta al server
        client_socket.sendall(richiesta.encode())

        # Ricezione risposta dal server
        risposta = client_socket.recv(1024).decode()
        print("Risposta dal server:", risposta)

        # Condizione di uscita (facoltativa, dipende dal server)
        if risposta.lower() == "nessuna disponibilità":
            break

    # Chiusura connessione
    client_socket.close()

# Chiamata della funzione 'start_client' in main
if __name__ == "__main__":
    start_client()
