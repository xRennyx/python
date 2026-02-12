import socket   # Import del modulo socket per la comunicazione client-server

# Indirizzo e porta del server
HOST = "localhost"   # Il server ascolta sul computer locale
PORT = 12345         # Porta scelta per la comunicazione

# Creazione della socket TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Associazione della socket all'indirizzo e alla porta
server_socket.bind((HOST, PORT))

# Il server si mette in ascolto (massimo 1 client)
server_socket.listen(1)

print("Server avviato. In attesa di connessione...")

# Accetta la connessione di un client
conn, addr = server_socket.accept()
print("Client connesso:", addr)

# Ricezione dei dati inviati dal client (massimo 4096 byte)
dati = conn.recv(4096).decode()

# Suddivide la stringa ricevuta in righe (una per ogni giorno)
righe = dati.strip().split("\n")

# Lista per salvare tutte le temperature
temperature = []

# Contatore dei giorni validi analizzati
giorni = 0

# Analisi di ogni riga ricevuta
for riga in righe:
    try:
        # Separazione dei campi: data, temperatura ore 12, temperatura ore 24
        data, t12, t24 = riga.split(";")

        # Conversione delle temperature da stringa a float
        t12 = float(t12)
        t24 = float(t24)

        # Salvataggio delle temperature nella lista
        temperature.append(t12)
        temperature.append(t24)

        # Incremento del numero di giorni validi
        giorni += 1
    except:
        # Se la riga è malformata, viene ignorata
        pass

# Calcolo del numero totale di rilevazioni
num_rilevazioni = len(temperature)

# Controllo se sono stati ricevuti dati validi
if num_rilevazioni > 0:
    # Calcolo della temperatura media complessiva
    media = sum(temperature) / num_rilevazioni

    # Calcolo della temperatura massima
    massimo = max(temperature)

    # Calcolo della temperatura minima
    minimo = min(temperature)

    # Preparazione della risposta da inviare al client
    risposta = (
        f"Numero giorni analizzati: {giorni}\n"
        f"Numero rilevazioni totali: {num_rilevazioni}\n\n"
        f"Temperatura media: {media:.2f} °C\n"
        f"Temperatura massima: {massimo} °C\n"
        f"Temperatura minima: {minimo} °C"
    )
else:
    # Messaggio nel caso in cui non ci siano dati validi
    risposta = "Nessun dato valido ricevuto."

# Invio della risposta al client
conn.sendall(risposta.encode())

# Chiusura della connessione con il client
conn.close()

# Chiusura della socket del server
server_socket.close()

print("Connessione chiusa.")