# ======================================
# MODULO 4 – CICLI
# ======================================
# Un ciclo serve a RIPETERE delle istruzioni.
# In Python esistono due cicli principali:
# - for
# - while

# --------------------------------------
# CICLO FOR
# Il ciclo for viene usato quando sappiamo
# quante volte ripetere qualcosa.

# Esempio: stampare i numeri da 0 a 4
print("Numeri da 0 a 4 ")
for i in range(5):
    print(i)

# --------------------------------------
# COS'È range()
# range(start, stop, step)
# start -> valore iniziale (incluso)
# stop -> valore finale (ESCLUSO)
# step -> incremento


# Numeri da 1 a 10
print("Numeri da 1 a 10 ")
for i in range(1, 11):
    print(i)

# Numeri pari
print("Numeri pari")
for i in range(0, 11, 2):
    print(i)


# --------------------------------------
# CICLO WHILE
# Il ciclo while ripete finché una condizione è vera.
# Si usa quando NON sappiamo quante volte ripetere.

print("COUNTDOWN")
contatore = 0
while contatore < 5:
    print(contatore)
    contatore += 1
print("BOOOOOM!")

# --------------------------------------
# DIFFERENZA FOR vs WHILE
# for -> ripetizioni note
# while -> ripetizioni dipendenti da una condizione

# --------------------------------------
# DO-WHILE (SIMULATO)
# Python NON ha il do-while.
# Lo simuliamo con while True e break.

print("inserisci numero maggiore di 0")
while True:
    n = int(input("Inserisci un numero (>0): "))
    if n > 0:
        break
print("Numero valido inserito")


# --------------------------------------
# CICLI E CONTATORI
print("Somma di 3 numeri")
somma = 0
for i in range(3):
    n = int(input("Numero: "))
    somma += n
print(f"Somma = {somma}")


# --------------------------------------
# CICLO SU LISTE
# Il for può scorrere direttamente una lista
numeri = [10, 20, 30, 40]
print("Stampo numeri della lista")
for n in numeri:
    print(n)

# --------------------------------------
# ESERCIZIO 2 – Somma fino a zero
# Chiedere numeri finché l'utente inserisce 0
print("Somma fino a zero")
somma = 0
while True:
    n = int(input("Numero: "))
    if n == 0:
        break
    somma += n
print(f"Somma totale: {somma}")


# --------------------------------------
# ESERCIZIO – Media voti
voti = [6, 7, 8, 5, 9]
print("Media voti di una lista: ")
somma = 0
for v in voti:
    somma += v
print(somma / len(voti))

# --------------------------------------
# ESERCIZIO – Indovina il numero
import random

n = random.randrange(1, 101)  # perchè 101 NON è compreso
tentativi = 5
print("Indovina il numero!!")
for i in range(tentativi):  # sono 5 tentativi quindi devo ciclare 5 volte
    print("Tentativo numero", i + 1, "di ", tentativi)  # perchè i parte da 0
    numero = int(input("Inerisci il numero: "))
    if numero == n:  # hai indovinato il numero
        print("Complimenti hai indovinato 😍")
        break  # forziamo l'uscita del ciclo visto che abbiamo già indovinato
    elif numero < n:  # se il numero è più basso di quello pensato dal computer
        print("Il numero da indovinare è più grande ⬆️")
    else:
        print("Il numero da indovinare è più piccolo ⬇️️")
else:  # è associato al for e non all'if e viene eseguito SOLO SE non ho usato
    # il break
    print("Hai esaurito i tentativi a disposizione, GAME OVER 💀, il numero era", n)
