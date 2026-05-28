# FUNZIONI DI GESTIONE DATI (ROTTA NAVALE)


def mostra_rotta(diario_bordo):
    """
    Mostra a schermo la rotta navale attuale e le coordinate immutabili di ogni tappa.

    Args:
        diario_bordo (list): Lista di tuple, dove ogni tupla contiene i dati della tappa.

    Returns:
        None: La funzione esegue solo stampe a schermo.
    """
    print("\n --- DIARIO DI BORDO: ROTTA ATTUALE ---")
    if len(diario_bordo) == 0:
        print("Nessuna rotta tracciata. La nave è in porto.")
    else:
        for tappa in diario_bordo:
            nome_porto = tappa[0]
            # Estraiamo la sotto-tupla delle coordinate
            coordinate = tappa[1]
            stato = tappa[2]

            # coordinate[0] è la Latitudine, coordinate[1] è la Longitudine
            print(f"{nome_porto} ({coordinate[0]}°N, {coordinate[1]}°E) -> Stato: [{stato}]")
    print("-----------------------------------------")


def aggiungi_tappa(diario_bordo, nome_porto, lat, lon):
    """
    Crea una nuova tappa con coordinate immutabili e la inserisce nella rotta.

    Args:
        diario_bordo (list): La lista della rotta da aggiornare.
        nome_porto (str): Il nome del punto di attracco.
        lat (str): La latitudine geografica.
        lon (str): La longitudine geografica.

    Returns:
        None: Modifica la lista originale in-place.
    """
    # Creiamo una tupla specifica per le coordinate GPS (Immutabile)
    coordinate_gps = (lat, lon)

    # Creiamo la tupla della tappa intera, impostando lo stato iniziale a "Pianificata"
    nuova_tappa = (nome_porto, coordinate_gps, "Pianificata")

    # Aggiungiamo la tappa alla rotta (la lista può crescere!)
    diario_bordo.append(nuova_tappa)
    print(f"️ Tappa '{nome_porto}' inserita correttamente nelle carte nautiche.")


def naviga_a_tappa(diario_bordo, nome_porto):
    """
    Cerca una tappa nella rotta e ne aggiorna lo stato in 'Raggiunta'.
    Poiché le tuple sono immutabili, per cambiare lo stato dobbiamo
    sostituire l'intera tupla della tappa dentro la lista.

    Args:
        diario_bordo (list): La lista della rotta.
        nome_porto (str): Il nome del porto in cui la nave è arrivata.

    Returns:
        None
    """
    trovato = False

    # Usiamo un ciclo basato sull'indice per poter sostituire l'elemento nella lista
    for i in range(len(diario_bordo)):
        tappa_corrente = diario_bordo[i]

        if tappa_corrente[0] == nome_porto:
            # Recuperiamo le coordinate fisse dalla vecchia tappa
            coordinate_salvate = tappa_corrente[1]

            # Ricreiamo la tupla con lo stato aggiornato
            tappa_aggiornata = (nome_porto, coordinate_salvate, "RAGGIUNTA")

            # Sostituiamo la vecchia tupla con quella nuova nella lista
            diario_bordo[i] = tappa_aggiornata
            print(f"Ancora gettata a '{nome_porto}'! Diario aggiornato.")
            trovato = True
            break

    if not trovato:
        print(f"Il porto '{nome_porto}' non è presente nella rotta pianificata.")



# FUNZIONI DI INTERFACCIA (MENU E APP)

def mostra_menu():
    """
    Stampa il pannello di controllo del timone.

    Args: Nessuno | Returns: None
    """
    print("\n=== TIMONE DI NAVIGAZIONE ===")
    print("1. Visualizza registro di rotta")
    print("2. Aggiungi nuova rotta/porto")
    print("3. Registra arrivo in un porto")
    print("4. Rientra in porto (Esci)")
    print("=============================")


def app_dirario_viaggio_nave():
    """
    Orchestratore principale del viaggio in nave.

    Args: Nessuno | Returns: None
    """
    # La rotta iniziale: una lista che contiene tuple annidate
    rotta_nave = [
        ("Genova", ("44.40", "8.94"), "RAGGIUNTA"),
        ("Isola d'Elba", ("42.77", "10.23"), "Pianificata")
    ]

    print("Capitano, i sistemi di navigazione sono pronti.")

    while True:
        mostra_menu()
        scelta = input("Comando (1-4): ").strip()

        if scelta == "1":
            mostra_rotta(rotta_nave)

        elif scelta == "2":
            porto = input("Nome del porto/isola: ").strip()
            latitudine = input("Latitudine (es. 40.71): ").strip()
            longitudine = input("Longitudine (es. -74.00): ").strip()

            if porto != "" and latitudine != "" and longitudine != "":
                aggiungi_tappa(rotta_nave, porto, latitudine, longitudine)
            else:
                print("Coordinate o nome mancanti. Impossibile tracciare la rotta.")

        elif scelta == "3":
            arrivo = input("In quale porto sei arrivato? ").strip()
            naviga_a_tappa(rotta_nave, arrivo)

        elif scelta == "4":
            print("\n Navi in porto. Sistemi spenti. Riposati, Capitano!")
            break
        else:
            print("Comando sconosciuto. Timone fuori controllo!")



# AVVIO DEL PROGRAMMA
if __name__=="main":
    app_dirario_viaggio_nave()