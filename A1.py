# ESERCIZIO: CHI VERRà INTERROGATO?
# Inseriamo i nomi degli studenti in una lista ed estraiamo a caso un nome; il nome che esce
# verrà interrogato.
import random  # importo la libreria per poterla utilizzare

# VERSIONE CON LA LISTA GIò PRONTA DI NOMI O INSERITA DA INPUT
# 1 modo: lista già pronta di nomi
lista_nomi_1 = [
    "Andrea",
    "Gianmarco",
    "Alessandro",
    "Bruno",
    "StefanoS",
    "Michele",
    "Roberto",
    "StefanoZ",
]
# Andrea, Gianmarco, Alessandro, Bruno, StefanoS, Michele, Roberto, StefanoZ

# 2 modo: inserisco da input i nomi
lista_nomi_2 = input("Inserisci i nomi separati da una , :\n")
# suddivido il testo inserito in variabili separate da una ,
lista_nomi_2 = lista_nomi_2.split(", ")  # creo una lista standard utilizzando lo split
# conto quanti elementi ho in lista
numero_studenti = len(lista_nomi_2)  # 8
# generare un numero casuale da 0 a numero studenti -1 (perchè parto da 0)
scelta_studente = random.randint(
    0, numero_studenti - 1
)  # genera un numero casuale tra 0 e 7
# estrapolo dalla lista lo studente che ha il numero uscito dalla funzione random
interrogato = lista_nomi_2[
    scelta_studente
]  # es: esce il numero 3 che corrisponde ad Aldin
print(
    "E' uscito il numero",
    str(scelta_studente),
    "quindi",
    interrogato,
    "sarà interrogato oggi!!!",
)
# --------------------------------------------------------------------------
# VERSIONE CON NUMERO DI REGISTRO
# 1. Chiediamo il numero totale di studenti (es. 21).
input_string = input("Inserisci il numero TOTALE di studenti nel registro (es. 21): ")
# 2. Conversione da stringa a intero (assumiamo che l'input sia corretto)
numero_totale_studenti = int(input_string)

registro_inizio = 1
registro_fine = numero_totale_studenti

# TEORIA: Random.randint()
# random.randint(a, b) genera un numero intero casuale N, dove a <= N <= b.
# Ad esempio, random.randint(1, 21) genera un numero tra 1 e 21 (inclusi).
numero_selezionato = random.randint(registro_inizio, registro_fine)

print(f"Range di selezione utilizzato: da {registro_inizio} a {registro_fine}.")
print(f"E' uscito il numero: {numero_selezionato}.")
print(
    f"Lo studente con il numero di registro {numero_selezionato} sarà interrogato oggi!"
)
