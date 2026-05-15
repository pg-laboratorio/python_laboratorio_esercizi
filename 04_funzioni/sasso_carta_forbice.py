"""
SASSO CARTA FORBICE
Autore: @nickname
"""
import random

def genera_mossa_computer():
    """
    Genera la mossa del computer
    return: stringa (sasso, carta o forbice)
    """
    numero_casuale = random.randint(1, 3)
    if numero_casuale == 1:
        return "sasso"
    elif numero_casuale == 2:
        return "carta"
    else:
        return "forbice"

def mostra_menu():
    """ Mostra le opzioni disponibili"""
    print("\n")
    print("-- Gioco sasso carta forbice --")
    print("Opzioni")
    print("-sasso")
    print("-carta")
    print("-forbice")
    print("-q : chiudere il programma")
    print("\n")

def determina_vincitore(giocatore, computer):
    """
    Confronta le mosse del giocatore e del computer e determina vincitore.
    args:
    - giocatore (str): la mossa scelta del giocatore
    - computer (str): la mossa scelta dal computer
    return:
    - str: risultato vittoria, pareggio, sconfitta
    """
    if giocatore == computer:
        return "Pareggio"

    elif (giocatore == "forbice" and computer == "carta") or (giocatore == "sasso" and computer == "forbice") or (giocatore == "carta" and computer == "sasso"):
        return "Vittoria"

    else:
        return "Sconfitta"

def gioco_sasso_carta_forbice():
    """
    Funzione principale gestione input utente e gioco
    """
    while True:
        mostra_menu()

        #Gestione input utente
        scelta_utente = input("Iserisci la tua mossa: ").lower()

        #Condizione chiusura programma
        if scelta_utente == 'q':
            print("\nChiusura in corso... Arrivederci!")
            break

        #Validazione input utente
        if scelta_utente != "sasso" and scelta_utente != "carta" and scelta_utente != "forbice":
            print("Mossa non valida!")
            continue

        #Generazione mossa computer
        mossa_computer = genera_mossa_computer()

        print(f"Tu hai scelto: {scelta_utente}")
        print(f"Il computer ha scelto: {mossa_computer}")

        #Calcolo risultato finale
        risultato = determina_vincitore(scelta_utente, mossa_computer)
        print(f"Il risultato è: {risultato}")


# Avvio effettivo del programma
if __name__ == "__main__":
    gioco_sasso_carta_forbice()






