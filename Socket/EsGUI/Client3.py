import socket               # Modulo per la comunicazione tramite socket
import tkinter as tk        # Modulo per creare l'interfaccia grafica
from tkinter import messagebox   # Per mostrare finestre di errore/informazione

# Indirizzo e porta del server
HOST = "localhost"   # Server in esecuzione sul computer locale
PORT = 12345         # Porta su cui il server è in ascolto

# Funzione richiamata quando si preme il pulsante "Invia dati"
def invia_dati():
    # Recupera il testo inserito dall'utente nella TextBox
    dati = text_input.get("1.0", tk.END).strip()

    # Controllo se il campo di input è vuoto
    if dati == "":
        messagebox.showerror("Errore", "Inserisci i dati delle temperature")
        return

    try:
        # Creazione della socket TCP lato client
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connessione al server usando indirizzo e porta
        client_socket.connect((HOST, PORT))

        # Invio dei dati al server
        client_socket.sendall(dati.encode())

        # Ricezione della risposta elaborata dal server
        risposta = client_socket.recv(4096).decode()

        # Pulizia dell'area di output
        text_output.delete("1.0", tk.END)

        # Visualizzazione della risposta del server nella GUI
        text_output.insert(tk.END, risposta)

        # Chiusura della connessione con il server
        client_socket.close()
    except:
        # Messaggio di errore se il server non è raggiungibile
        messagebox.showerror("Errore", "Impossibile connettersi al server")

# ---------------- GUI ----------------

# Creazione della finestra principale
root = tk.Tk()

# Titolo della finestra
root.title("Invio Temperature Giornaliere – Stazione Meteo")

# Frame per organizzare gli elementi grafici
frame = tk.Frame(root, padx=15, pady=15)
frame.pack()

# Etichetta che spiega il formato dei dati da inserire
tk.Label(frame, text="Inserisci i dati (data;temp12;temp24):").pack()

# Area di testo per l'inserimento dei dati
text_input = tk.Text(frame, width=45, height=8)
text_input.pack(pady=5)

# Pulsante per inviare i dati al server
btn = tk.Button(frame, text="Invia dati", command=invia_dati)
btn.pack(pady=10)

# Etichetta per l'area dei risultati
tk.Label(frame, text="Risultati dal server:").pack()

# Area di testo per visualizzare la risposta del server
text_output = tk.Text(frame, width=45, height=8, state="normal")
text_output.pack()

# Avvio del ciclo principale dell'interfaccia grafica
root.mainloop()