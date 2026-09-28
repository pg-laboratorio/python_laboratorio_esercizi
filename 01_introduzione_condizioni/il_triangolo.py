"""
PROGETTO
CONSEGNA:
Dati tre bastoncini, è possibile formare un triangolo solo se ogni lato è
minore della somma degli altri due.
Scrivi un programma che riceva tre lunghezze e determini se è possibile
costruire un triangolo, stampando "Sì" o "No".

DATI INPUT:
- Le tre lunghezze inserite dall'utente (lato_a, lato_b, lato_c)

DATI OUTPUT:
- Messaggio "Sì" oppure "No"

PASSAGGI RISOLUTIVI:
- chiedo all'utente le tre lunghezze
- se lato_a < lato_b + lato_c E lato_b < lato_a + lato_c E lato_c < lato_a + lato_b
    stampo "Sì"
- altrimenti
    stampo "No"

NB: l'operatore logico "and" è vero solo se TUTTE le condizioni sono vere.
    Basta che una sola sia falsa e il triangolo non si può costruire.
"""
# - chiedo all'utente le tre lunghezze
lato_a = float(input("Inserisci la lunghezza del 1° lato: "))
lato_b = float(input("Inserisci la lunghezza del 2° lato: "))
lato_c = float(input("Inserisci la lunghezza del 3° lato: "))

# - se tutte e tre le condizioni sono vere stampo "Sì"
if lato_a < lato_b + lato_c and lato_b < lato_a + lato_c and lato_c < lato_a + lato_b:
    print("Sì")
# - altrimenti stampo "No"
else:
    print("No")
