'''
CONSEGNA
Definire lo username per l'utente di un servizio Web.
Lo username dell'utente è costruito concatenando le prime tre lettere del cognome, le prime tre del nome e le ultime due cifre della data di nascita.
Si vuole anche che lo username sia scritto con le lettere tutte minuscole.

PROGETTO
OBIETTIVO: Definire l'username per l'utente di un servizio web a partire dai dati personali

DATI INPUT: nome, cognome e data di nascita dell'utente

DATI OUTPUT: l'username per l'utente con le prime tre lettere del nome e cognome + le ultime due cifre della data di nascita

PASSAGGI:
- chiedo all'utente di inserire il nome, cognome e data di nascita
- prendo le prime tre cifre del nome, cognome
- prendo le ultime due cifre della data di nascita
- l'username lo trasformo in minuscolo
- stampo l'username completo
'''
#chiedo all'utente di inserire il nome, cognome e data di nascita
nome = input("Inserisci il tuo nome: ")
cognome = input("Inserisci il tuo cognome: ")
data = input("Inserisci la tua data di nascita: ")
#prendo le prime tre cifre del nome, cognome
#prendo le ultime due cifre della data di nascita
username = nome[0:3] + cognome[0:3]  + data[-2:]
#l'username lo trasformo in minuscolo
username = username.lower()
#stampo l'username completo
print (f"Il tuo username è: {username}")
