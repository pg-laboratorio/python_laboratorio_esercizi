'''
Scrivi un programma che chieda all'utente una parola
o una frase e poi chieda di inserire una singola lettera
Il programma deve contare quante volte quella specifica lettera compare nella parola/frase
(ignorando la differenza tra maiuscole e minuscole)
e stampare il risultato.
PROGETTO
OBIETTIVO: Contare una lettera in una frase
DATI INPUT:
- la frase dell'utente (testo)
- la lettera da contare (lettera)
DATI OUTPUT:
- numero di volte che la lettera compare nella frase (numero_lettera)
PASSAGGI:
- Settiamo le variabili
- Chiedo in input la frase e la lettera
- Trasformiamo il testo e la lettera in minuscolo
- Ciclo per contare il numero di lettere
    se la lettera da contare corrisponde alla lettera nella frase
        incremeto il numero lettere di 1
- Stampiamo il numero di lettere contate
'''
# Settiamo le variabili
numero_lettera = 0

# Chiedo in input la frase e la lettera
testo = input("Inserisci la frase o parola: ")
lettera_da_contare = input("Inserisci la lettera da contare: ")

# Trasformiamo il testo e la lettera in minuscolo
testo = testo.lower() # nomevariabile.nomemetodo()
lettera_da_contare = lettera_da_contare.lower()

# Ciclo per contare il numero di lettere
for i in testo:
    if i == lettera_da_contare:
        numero_lettera += 1

# Stampiamo il numero di lettere contate
print(f"Il numero di lettere {lettera_da_contare} è: {numero_lettera}")

