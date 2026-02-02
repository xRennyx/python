import socket
import threading

# Definizione funzione istanza di servizio
def serviceInstance(conn, addr):
    # Disponibilità iniziale
    disponibilita = 10
    print(f"Connessione stabilita con {addr}")

    while True:
        # Ricezione richiesta dal client
        data = conn.recv(1024).decode()
        if not data:
            break

        # Estrazione città di partenza e arrivo
        partenza, arrivo = data.split(",")

        # Logica di disponibilità
        if disponibilita > 0:
            risposta = f"Disponibilità confermata per tratta {partenza} -> {arrivo}. Posti rimasti: {disponibilita}"
            disponibilita -= 1
        else:
            risposta = "Nessuna disponibilità"

        # Invio risposta al client
        conn.send(risposta.encode())

        # Se finisce la disponibilità si chiude la connessione
        if disponibilita == 0:
            break

    conn.close()
    print(f"Connessione terminata con {addr}")

def start_server():
    # Inizializzazione lato server della socket su porta 12345
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 12345))
    server_socket.listen(5)

    print("Server in ascolto sulla porta 12345...")

    # Loop che accetta continuamente nuove connessioni
    while True:
        conn, addr = server_socket.accept()

        # Creazione thread per il client
        client_thread = threading.Thread(
            target=serviceInstance,
            args=(conn, addr)
        )
        client_thread.start()

# Chiamata della funzione 'start_server' in main
if __name__ == "__main__":
    start_server()
