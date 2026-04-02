'''
Dati tre bastoncini, è possibile formare un triangolo solo se ogni lato è minore della somma degli altri due.
Scrivi un programma che riceva tre lunghezze e determini se è possibile costruire un triangolo, stampando "Si" o "No".

DATI INPUT:
tre lunghezze inserite dall'utente (lato_a, lato_b, lato_c)

DATI OUTPUT:
stampa "Si" o "No"

Passaggi:
- Chiedo all'utente di inserire le tre lunghezze
- se lato_a < lato_b + lato_c e lato_b < lato_a + lato_c e lato_c < lato_a + lato_b
    stampo "Si"
altrimenti stampo "No"

'''
#Chiedo all'utente di inserire le tre lunghezze
lato_a = float(input("Inserisci la lunghezza del 1° lato: "))
lato_b = float(input("Inserisci la lunghezza del 2° lato: "))
lato_c = float(input("Inserisci la lunghezza del 3° lato: "))

#se lato_a < lato_b + lato_c e lato_b < lato_a + lato_c e lato_c < lato_a + lato_b
if lato_a < lato_b + lato_c and lato_b < lato_a + lato_c and lato_c < lato_a + lato_b:
#stampo "Si"
    print("Si")
#altrimenti stampo "No"
else:
    print("No")
