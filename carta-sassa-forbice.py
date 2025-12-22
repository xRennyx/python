# ESERCIZIO: gioco della morra cinese
# creo l'arte per il nostro videogioco
import random # importo la libreria così il computer sceglie a caso sasso, carta, forbici
sasso = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

carta = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

forbici = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
# creo una lista con le tre immagini
immagini = [sasso, carta, forbici] # le variabili CONTENGONO l'immagine associata
# chiedo al giocatore di inserire la propria scelta
giocatore = int(input("Cosa scegli? 0 sasso, 1 carta, 2 forbici. \n"))
# controllo che il giocatore abbia inserito un valore valido
if giocatore >= 3 or giocatore < 0:
    print("Hai inserito un valore non valido, GAME OVER!")
else: # ho inserito un valore valido quindi posso giocare
    print("Giocatore: ")
    print(immagini[giocatore]) # visualizzo la scelta del giocatore
    # devo far entrare in gioco il computer
    computer = random.randint(0,2) # assegno un numero casuale al computer
    print("Computer: ")
    print(immagini[computer]) # visualizzo la scelta del computer

    # devo eseguire tutti i controlli per decidere chi ha vinto
    if giocatore == 0 and computer == 2:
        print("HAI VINTO! 🤩")
    elif computer == 0 and giocatore == 2:
        print("HAI PERSO! 😭")
    elif computer > giocatore:
        print("HAI PERSO! 😤")
    elif giocatore > computer:
        print("HAI VINTO! 😍")
    elif computer == giocatore:
        print ("PAREGGIO! 😓")
    else:
        print("errore di sistema")
