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
        print ("Errore saldo insufficiente")
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
            print(f"Il tuo saldo attuale è {saldo}")

        elif scelta == '2':
            in_importo = float(input("Inserisci importo versamento: "))
            saldo = versa (in_importo, saldo)










