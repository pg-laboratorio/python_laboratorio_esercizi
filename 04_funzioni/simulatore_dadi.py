"""
SIMULATORE DADI
Autore: @vostro_nickname
"""
import random

def lancia_dado():
    """
    Genera un numero casulae tra 1 e 6 (simula un dado a sei facce)
    return: numero_dado (int)
    """
    numero_dado = random.randint(1, 6)
    return numero_dado

def mostra_menu():
    """ Mostra le opzioni disponibili"""
    print("\n")
    print("-- Lancia dadi --")
    print("r : lancia dadi")
    print("q : chiudere il programma")
    print("\n")


def simulatore_dadi():
    """ Gestisce il ciclo principale e interaazione con l'utente"""
    while True:
        # richiamiamo la funzione per mostrare il menu
        mostra_menu()
        comando = input("Cosa vuoi fare? ").lower()

        #interruzione programma
        if comando == 'q':
            print("\nChiusura in corso... Arrivederci!")
            break

        elif comando == 'r':
            dado1 = lancia_dado()
            dado2 = lancia_dado()
            print(f"\nDado 1: {dado1}")
            print(f"Dado 2: {dado2}")
            print(f"Totale: {dado1 + dado2}\n")

        else:
            print("\nComando non valido, usa 'r' o 'q'")
            continue


if __name__ == "__main__":
    simulatore_dadi()