'''
Scrivere un programma ScrivoScrivoScrivo che chiede all’utente di inserire un numero maggiore o uguale a zero e stampa il messaggio “sto ciclando” un numero di volte pari al numero inserito dall’utente. Se il valore inserito dall’utente e negativo il programma stampa un messaggio di errore.

PROGETTO

OBIETTIVO
Stampare 'sto ciclando' un numero di volte maggiore o uguale a 0

DATI INPUT
- il numero di volte che stampare (numero_cicli)

DATI OUTPUT
- la stringa 'sto ciclando'
- messaggio di errore

PASSAGGI:
- chiedere il numero di volte che voglio stampare
- verifichiamo cher sia >= 0
- se vero:
    - ciclo for da 0 fino a numero_cicli
    - stampa 'sto ciclando'
'''
# chiedere il numero di volte che voglio stampare
numero_cicli = int(input("Inserisci un numero >= 0: "))
# verifichiamo cher sia >= 0
if numero_cicli < 0:
    print("Errore, hai inserito un numero inferiore a 0")
else:
    for i in range(0, numero_cicli):
        print(f"{i} Sto ciclando")




