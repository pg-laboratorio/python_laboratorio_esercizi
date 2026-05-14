"""
SIMULATORE BANCOMAT
"""

def versa (importo, saldo_attuale):
    """
    Aggiugere l'importo versato al saldo
    args: importo (float), saldo_attuale (float)
    return: nuovo_saldo (float)
    """
    nuovo_saldo = saldo_attuale + importo
    return nuovo_saldo

def preleva (importo, saldo_attuale):
    """
    Sottrarre l'importo versato al saldo,
    verificano la disponibilità
    args: importo (float), saldo_attuale (float)
    return: nuovo_saldo (float)
    """
    if saldo_attuale < importo:
        print ("Saldo insufficiente")
        return saldo_attuale
    else:
        nuovo_saldo = saldo_attuale - importo
        return nuovo_saldo


def mostra_menu():
    """ Mostra le opzioni disponibili"""
    print("\n")
    print("-- Bancomat --")
    print("1 : visualizza saldo")
    print("2 : versa")
    print("3 : preleva")
    print("q : chiudere il programma")
    print("\n")

def bancomat():
    """
    Gestione applicazione bancomat
    """
    saldo = 0.0 #inizializzo il saldo

    while True:
        mostra_menu()
        scelta = input("Scegli un'opzione (1,2,3,q): ")

        if scelta == 'q':
            print("\nChiusura in corso... Arrivederci!")
            break

        elif scelta == '1':
            print(f"\nIl tuo saldo attuale è {saldo}")

        elif scelta == '2':
            importo_in = float(input("Inserisci l'importo da versare: "))
            if importo_in > 0:
                # Sovrascrive il saldo vecchio con quello nuovo calcolato dalla funzione
                saldo = versa(importo_in, saldo)
                print(f"Versamento completato. Nuovo saldo: {saldo}€")
            else:
                print("\n[ERRORE] L'importo da versare deve essere maggiore di zero.")

        elif scelta == '3':
            importo_out = float(input("Inserisci l'importo da prelevare: "))
            if importo_out > 0:
                # Sovrascrive il saldo aggiornandolo con l'esito del prelievo
                saldo = preleva(importo_out, saldo)
                print(f"Prelievo completato. Nuovo saldo: {saldo}€")
            else:
                print("\n[ERRORE] L'importo da prelevare deve essere maggiore di zero.")

        else:
            print("\n[ERRORE] Scelta non valida! Inserisci un'opzione corretta.")
            continue

# Avvio effettivo del programma
if __name__ == "__main__":
    bancomat()


