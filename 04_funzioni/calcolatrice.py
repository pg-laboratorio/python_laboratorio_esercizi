"""
CALCOLATRICE
"""

def somma (a, b):
    """ Calcola la somma di due numeri"""
    s = a + b
    return s

def differenza (a, b):
    """ Calcola la differenza tra due numeri"""
    d = a - b
    return d

def moltiplicazione (a, b):
    """ Calcola la moltiplicazione tra due numeri"""
    m = a * b
    return m

def divisione (a, b):
    """ Calcola la divisione tra due numeri"""
    if b == 0:
        return "Errore, denominatore 0"
    else:
        div = a / b
        return div

def mostra_menu():
    """ Mostra le opzioni disponibili"""
    print("\n")
    print("-- Calcolatrice--")
    print("+ : somma")
    print("- : sottrazione")
    print("* : moltiplicazione")
    print("/ : divisione")
    print("q : chiudere il programma")
    print("\n")


def calcolatrice():
    """Gestisce il funzionamento di una calcolatrice"""
    while True:
        mostra_menu()

        scelta = input("Inserisci l'operatore (+, -, *, /) oppure 'q' per chiudere: ")

        if scelta == 'q':
            print("Chiusura in corso...")
            break

        if scelta in ('+','-','*','/'):
            #chiediamo i numeri
            n1 = float(input("Inserisci il primo numero: "))
            n2 = float(input("Inserisci il secondo numero: "))

            if scelta == '+':
                risultato = somma(n1,n2)
                print(f"{n1} + {n2} = {risultato}")

            elif scelta == '-':
                risultato = differenza(n1,n2)
                print(f"{n1} - {n2} = {risultato}")

            elif scelta == '*':
                risultato = moltiplicazione(n1,n2)
                print(f"{n1} * {n2} = {risultato}")

            elif scelta == '/':
                risultato = divisione(n1,n2)
                print(f"{n1} / {n2} = {risultato}")

        else:
            print("scelta non valida!")
            continue #ritorno alla scelta


calcolatrice()





