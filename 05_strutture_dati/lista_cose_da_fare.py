# 1. FUNZIONI DI GESTIONE DATI (LISTE)

def mostra_lista(lista_task):
    """
    Stampa a schermo tutti gli elementi della lista in modo ordinato.

    Args:
        lista_task (list): La lista contenente le stringhe degli impegni.

    Returns:
        None: La funzione non restituisce dati, esegue solo stampe a schermo.
    """
    print("\n --- LA TUA TO-DO LIST ---")
    if len(lista_task) == 0:
        print("Evviva! Non hai impegni rimasti.")
    else:
        for impegno in lista_task:
            print(f"- {impegno}")
    print("----------------------------")


def aggiungi_impegno(lista_task, nuovo_impegno):
    """
    Aggiunge un nuovo impegno in coda alla lista.

    Args:
        lista_task (list): La lista a cui aggiungere l'elemento.
        nuovo_impegno (str): Il testo del nuovo impegno da inserire.

    Returns:
        None: La lista viene modificata direttamente (in-place),
              quindi non c'è un valore di ritorno.
    """
    lista_task.append(nuovo_impegno)
    print(f"+ '{nuovo_impegno}' aggiunto con successo!")


def completa_impegno(lista_task, impegno_fatto):
    """
    Rimuove un impegno dalla lista dopo aver verificato che esista.

    Args:
        lista_task (list): La lista da cui rimuovere l'elemento.
        impegno_fatto (str): Il testo esatto dell'impegno da completare.

    Returns:
        None: La lista viene modificata direttamente, non restituisce dati.
    """
    if impegno_fatto in lista_task:
        lista_task.remove(impegno_fatto)
        print(f"V '{impegno_fatto}' completato e rimosso!")
    else:
        print(f" Impossibile rimuovere: '{impegno_fatto}' non è in lista.")


# 2. FUNZIONI DI INTERFACCIA (MENU E APP)

def mostra_menu():
    """
    Stampa il menu testuale con le opzioni disponibili per l'utente.

    Args:
        Nessuno.

    Returns:
        None: Esegue solo la stampa del menu grafico.
    """
    print("\n=== MENU DI GESTIONE ===")
    print("1. Mostra tutti gli impegni")
    print("2. Aggiungi un impegno")
    print("3. Completa (rimuovi) un impegno")
    print("4. Esci dal programma")
    print("========================")


def app_to_do_list():
    """
    Funzione principale che orchestra l'applicazione. Inizializza la lista,
    gestisce il ciclo continuo (while) e smista l'input dell'utente.

    Args:
        Nessuno.

    Returns:
        None: Controlla il flusso dell'applicazione fino alla sua chiusura.
    """
    # Inizializziamo la lista all'interno dell'applicazione
    miei_impegni = ["Studiare Python", "Fare la spesa"]

    print("Benvenuto nel tuo Gestore di Impegni Personale!")

    while True:
        mostra_menu()
        scelta = input("Scegli un'opzione (1-4): ")

        if scelta == "1":
            mostra_lista(miei_impegni)

        elif choix := scelta == "2":
            nuovo = input("Cosa devi fare di nuovo? ")
            if nuovo.strip() != "":
                aggiungi_impegno(miei_impegni, nuovo)
            else:
                print(" Non puoi aggiungere un impegno vuoto!")

        elif scelta == "3":
            if len(miei_impegni) == 0:
                print(" La lista è già vuota, non c'è nulla da completare.")
            else:
                da_rimuovere = input("Scrivi l'esatto nome dell'impegno completato: ")
                completa_impegno(miei_impegni, da_rimuovere)

        elif scelta == "4":
            print("\n Programma terminato. Buona giornata!")
            break  # Interrompe il ciclo while uscendo dall'applicazione

        else:
            print(" Scelta non valida! Inserisci un numero da 1 a 4.")



# AVVIO DEL PROGRAMMA
if __name__ == "__main__":
    app_to_do_list()


"""
Nota:
quasi tutte queste funzioni hanno Returns: None.
Questo succede perché in Python le funzioni che servono solo a stampare qualcosa (come mostra_menu) o che modificano un oggetto mutabile esistente (come le liste in aggiungi_impegno) non hanno bisogno di usare la parola chiave return per rispedire un dato indietro. Python, di default, assegna loro come ritorno il valore speciale None.

"""