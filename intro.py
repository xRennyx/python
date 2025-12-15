#comment
'''
comment
'''
#python è un linguaggio interpretato : il codice viene
#eseguito riga per rigo non nella sua interezza (compilatore)
print("ciao") #print serve per stampare a schermo
print(5+3) # stampo direttamente la somma di due numeri 
# variabili: è un contenitore di dati
# è un nome che fa riferimento ad un valore salvato in memoria
'''
NB: Python è un linguaggio non tipizzato
Come si fa a tipizzare in python:
nome_variabile: tipo_di_dato= valore
es. num: int= 18
es. num=18
tipi principali:
int -> numeri interi
float -> numeri decimali
str -> stringhe 
bool -> true/false

CAST(conversione tipo di dato)
es.
x="10" 
y= int(x)
'''
x="10"
y=int(x)
print(y+4)
#input() server a leggere quello che vine scritt osu console
#NB: legge sempre una stringa
nome = input("Come ti chiami: ")#Legge una stringa
eta=int (input("Quanti anni hai?: "))#legge la tringa e la converte in numero
print (f"Ciao {nome}, hai {eta} anni")
#NB: sono viste come vettori, accedono ad ogni carattera attraverso un indice
#t[indice] vado verso destro t[-indice] se vado verso sinistra
#t[0:4] dal primo indice fino all'ultimo NON compreso
