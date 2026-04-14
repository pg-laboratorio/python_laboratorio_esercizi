'''
Scrivi un programma che chieda all'utente il proprio numero di carta di credito
o di telefono (sotto forma di stringa).
Il programma deve nascondere tutte le cifre tranne le ultime 4, sostituendole
con degli asterischi *.
*Esempio: "3331234567" diventa "*****4567".

obbiettivo:
- mascherare il numero di telefono o della carta di credito dell'utente

dati input:
- chiedo all'utente il numero della carta di credito o numero di telefono (numero)

dati output:
- stampare il numero mascherato (numero_mascherato)

passaggi:
- chiedere all'utente il numero di telefono o della carta di credito (numero)

- contare i numeri dati dall'utente tranne gli ultimi 4 len(numero-4) (parte_mascherata)

- contare i numeri visibili (parte_visibile)

- metto insieme i due numeri (parte_completa)

- stampo il numero mascherato

'''
# chiedere all'utente il numero di telefono o della carta di credito (numero)
numero = input("qual'è il tuo numero: ")
# contare i numeri dati dall'utente tranne gli ultimi 4 len(numero-4) (parte_mascherata)
parte_mascherata = '*' * (len(numero) - 4)
# contare i numeri visibili (parte_visibile)
parte_visibile = numero [-4:]
# metto insieme i due numeri
parte_completa = parte_mascherata + parte_visibile
# stampo il numero mascherato
print("il tuo codice è:", parte_completa)