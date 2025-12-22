# LISTE : sono variabili in cui posso memorizzare più di un dato
# alla volta. Gli elementi della lista devono essere racchiusi in parentesi [] e suddivisi
# da una , . NB: gli elementi della lista partono dalla posizione 0.
# Lista Python si comporta come un vettore dinamico (dynamic array o ArrayList in Java/C#),
# non sono statici poich+ possono memorizzare varibili di tipo diverso
# ES: voglio memorizzare in una lista gli eroi di Clash Royale
eroi_clash = ["Re degli Scheletri", "Regina degli Arcieri", "Cavaliere d'Oro"]
# NB: se non usassi le liste dovre procedere in questa maniera:
eroe1 = "Re degli Scheletri"
eroe2 = "Regina degli Arcieri"
eroe3 = "Cavaliere d'Oro"
# Le liste mi permettono di inserire elementi diversi tra loro
tipologia_carte_clash = ["Comuni", "Rare", "Epiche", "Leggendarie", "Eroi"]
informazioni_carta = [
    "Nome",
    "Elisir",
    "Potenza di attacco",
    "Stelle",
    "Vita",
    "immagine",
]
informazioni_carta_valori = [
    "Domatore",
    4,
    421,
    "2 stelle",
    34.5,
    "☻",
]  # testi, interi, decimali
print(
    informazioni_carta_valori
)  # mi stampa ["Domatore", 4, 421, "2 stelle", 34.5, "☻"]
# STAMPA DI UN ELEMENTO DELLA LISTA
print(informazioni_carta_valori[5])  # mi stampa ☻
print(informazioni_carta_valori[0])  # mi stampa Domatore
