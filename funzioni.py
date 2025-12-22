# ======================================
# MODULO – FUNZIONI IN PYTHON
# ======================================
# COS'È UNA FUNZIONE?
# Una funzione è un blocco di codice che:
# - ha un nome
# - può ricevere dati (parametri)
# - può restituire un risultato (return)
# - serve per NON ripetere codice

# --------------------------------------
# STRUTTURA GENERALE
# def nome_funzione(parametri):
#     istruzioni
#     return valore


# --------------------------------------
# FUNZIONE SENZA PARAMETRI
def stampa_menu():
    print("1 - Gioca")
    print("2 - Esci")


print("Stampa di un semplice menu inserito in una funzione")
stampa_menu()


# --------------------------------------
# FUNZIONE CON PARAMETRI
def saluta(nome: str):
    print(f"Ciao {nome}")


print("Funzione che saluta una persona")
saluta("Marco")


# --------------------------------------
# FUNZIONE CON RETURN
def sommaNumeri(a: int, b: int) -> int:  # -> indica il tipo di ritorno
    risultato = a + b
    return risultato


print("Funzione che sonna due numeri")
x = sommaNumeri(5, 3)
print(x)


# --------------------------------------
# DIFFERENZA PRINT vs RETURN
def somma_print(a: int, b: int):  # metodo
    print(a + b)


def somma_return(a: int, b: int) -> int:  # funzione
    return a + b


print("Differenza tra funzione e metodo")
somma_print(2, 3)
y = somma_return(2, 3)
print(y)


# --------------------------------------
# FUNZIONE CON LOGICA
def pari_o_dispari(n: int) -> str:
    if n % 2 == 0:
        return "pari"
    else:
        return "dispari"


print("Funzione che dice se un numero è pari o dispari")
print(pari_o_dispari(7))


# --------------------------------------
# FUNZIONI E INPUT
def leggi_numero_input() -> int:
    return int(input("Inserisci un numero: "))


print("funzione che legge un numerod a input")
n = leggi_numero_input()
print(n)


# ======================================
# ESEMPIO COMPLETO CALCOLATRICE
def somma(a: float, b: float) -> float:
    # commento su più righe valido per creare la documentazione
    """
    Restituisce la somma di due numeri
    """
    return a + b


def sottrazione(a: float, b: float) -> float:
    """
    Restituisce la differenza tra due numeri
    """
    return a - b


def moltiplicazione(a: float, b: float) -> float:
    """
    Restituisce il prodotto di due numeri
    """
    return a * b


def divisione(a: float, b: float) -> float:
    """
    Restituisce il quoziente tra due numeri.
    ATTENZIONE: divisione per zero
    """
    if b == 0:
        return 0
    return a / b


def leggi_numero(messaggio: str) -> float:
    """
    Legge un numero da tastiera e lo converte in float
    """
    return float(input(messaggio))


# --------------------------------------
# MAIN
# In Python il main non è obbligatorio,
# ma lo usiamo per chiarezza didattica
def main():
    while True:
        print("\n--- CALCOLATRICE ---")
        print("1 - Somma")
        print("2 - Sottrazione")
        print("3 - Moltiplicazione")
        print("4 - Divisione")
        print("0 - Esci")

        scelta: int = int(input("Scelta: "))

        if scelta == 0:
            print("Uscita dal programma")
            break

        if scelta < 0 or scelta > 4:
            print("Scelta non valida")
            continue

        a = leggi_numero("Inserisci il primo numero: ")
        b = leggi_numero("Inserisci il secondo numero: ")

        if scelta == 1:
            risultato = somma(a, b)
        elif scelta == 2:
            risultato = sottrazione(a, b)
        elif scelta == 3:
            risultato = moltiplicazione(a, b)
        elif scelta == 4:
            risultato = divisione(a, b)

        print(f"Risultato = {risultato}")


# --------------------------------------
# AVVIO DEL PROGRAMMA
main()
