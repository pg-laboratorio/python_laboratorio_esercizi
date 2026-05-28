# FUNZIONI DI GESTIONE DATI (DIZIONARI)

def mostra_rubrica(rubrica):
    """
    Stampa a schermo tutti i contatti presenti nel dizionario.

    Args:
        rubrica (dict): Il dizionario contenente i contatti (Chiave: Nome, Valore: Numero).

    Returns:
        None: La funzione esegue solo stampe a schermo.
    """
    print("\n --- RUBRICA CONTATTI ---")
    if len(rubrica) == 0:
        print("La tua rubrica è vuota.")
    else:
        # Il metodo .items() ci permette di estrarre contemporaneamente
        # sia la chiave (nome) sia il valore (numero) ad ogni giro del ciclo
        for nome, numero in rubrica.items():
            print(f"{nome}: {numero}")
    print("---------------------------")


def aggiungi_o_aggiorna_contatto(rubrica, nome, numero):
    """
    Inserisce un nuovo contatto o aggiorna il numero di uno esistente.

    Args:
        rubrica (dict): Il dizionario da modificare.
        nome (str): La chiave del dizionario (il nome del contatto).
        numero (str): Il valore associato alla chiave (il numero di telefono).

    Returns:
        None: Il dizionario viene modificato direttamente.
    """
    # Se la chiave esiste già, Python sovrascrive il valore.
    # Se non esiste, crea la nuova coppia chiave-valore.
    rubrica[nome] = numero
    print(f"Contatto '{nome}' salvato con successo!")


def cerca_contatto(rubrica, nome):
    """
    Cerca un contatto tramite la sua chiave (nome) e ne mostra il valore.

    Args:
        rubrica (dict): Il dizionario in cui effettuare la ricerca.
        nome (str): Il nome da cercare.

    Returns:
        None: Stampa il risultato direttamente a video.
    """
    # Usiamo l'operatore 'in' per verificare se la CHIAVE esiste nel dizionario.
    # Questo controllo evita il temuto errore 'KeyError' se il nome non esiste!
    if nome in rubrica:
        print(f"Contatto Trovato -> {nome}: {rubrica[nome]}")
    else:
        print(f"Il nome '{nome}' non è presente in rubrica.")


# FUNZIONI DI INTERFACCIA (MENU E APP)

def mostra_menu():
    """
    Stampa il menu delle opzioni disponibili.

    Args:
        Nessuno.

    Returns:
        None
    """
    print("\n=== MENU RUBRICA ===")
    print("1. Mostra tutti i contatti")
    print("2. Aggiungi / Modifica un contatto")
    print("3. Cerca un contatto per nome")
    print("4. Esci")
    print("====================")


def app_rubrica():
    """
    Funzione principale che orchestra l'applicazione della rubrica.

    Args:
        Nessuno.

    Returns:
        None
    """
    # Inizializziamo il dizionario con dei dati di partenza
    mia_rubrica = {
        "Alice": "333-1234567",
        "Bob": "347-9876543"
    }

    print("Benvenuto nella tua Rubrica Telefonica!")

    while True:
        mostra_menu()
        scelta = input("Scegli un'opzione (1-4): ")

        if scelta == "1":
            mostra_rubrica(mia_rubrica)

        elif scelta == "2":
            nome = input("Inserisci il nome del contatto: ").strip()
            numero = input("Inserisci il numero di telefono: ").strip()

            if nome != "" and numero != "":
                aggiungi_o_aggiorna_contatto(mia_rubrica, nome, numero)
            else:
                print(" Nome o numero non validi! Operazione annullata.")

        elif scelta == "3":
            nome_da_cercare = input("Chi vuoi cercare? ").strip()
            cerca_contatto(mia_rubrica, nome_da_cercare)

        elif scelta == "4":
            print("\n Chiusura rubrica. Alla prossima!")
            break

        else:
            print(" Opzione non valida! Inserisci un numero da 1 a 4.")



# AVVIO DEL PROGRAMMA
if __name__ == "__main__":
    app_rubrica()



"""
Note:
L'operatore in controlla le CHIAVI, non i valori: Quando scriviamo if nome in rubrica, Python va a cercare solo tra i nomi (le chiavi). Non guarda i numeri di telefono.

Niente duplicati per le chiavi: Se usi aggiungi_o_aggiorna_contatto inserendo un nome già esistente (es. "Alice") ma con un numero nuovo, il vecchio numero verrà sovrascritto. Non avrai mai due chiavi "Alice" identiche.

Il metodo .items(): È il modo più elegante per ciclare nei dizionari perché estrae una coppia alla volta, spacchettandola direttamente in due variabili separate (nel nostro caso nome e numero).

"""