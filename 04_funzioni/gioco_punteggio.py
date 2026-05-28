"""
GESTIONE PUNTEGGIO E ISOLAMENTO DELLE VARIABILI (SCOPE)
Autore: @nickname

Lo Scope delle variabili (Locali vs Globali)
Un classico errore dei principianti è pensare che una variabile modificata dentro una funzione cambi anche all'esterno. Questo esercizio evidenzia il problema.
Questo esercizio serve a spiegare perché è preferibile passare il punteggio come argomento e riassegnare il valore di ritorno nel programma principale (punteggio = aggiungi_punti(punteggio, 10)) invece di usare la parola chiave global, che rende il codice difficile da mantenere.
"""

"""
=================================
COSO UTILIZZO VARIABILI GLOBALI (DA NON FARE):

# Definizione della variabile GLOBALE
punteggio = 0

def aggiungi_punti(punti):
    """
    #Riceve un parametro numerico e lo somma al punteggio globale.
    #Mostra anche la creazione di una variabile locale isolata.
    """
    # Usiamo 'global' per dire a Python di modificare la variabile fuori dalla funzione
    global punteggio
    punteggio += punti

    # Questa è una VARIABILE LOCALE. Esiste SOLO dentro questa funzione.
    info_funzione = "Sto elaborando l'aggiunta dei punti..."
    print(f"[Dentro aggiungi_punti] -> info_funzione: '{info_funzione}'")


def azzera_punteggio():
    """
    #Azzera il punteggio globale portandolo a 0.
    """
    global punteggio
    punteggio = 0
    print("[Dentro azzera_punteggio] -> Il punteggio globale è stato azzerato.")


def avvia_dimostrazione():
    """
    #Funzione principale che esegue il programma e dimostra
    #l'isolamento delle variabili.
    """
    print("--- STATO INIZIALE ---")
    print(f"Punteggio globale all'inizio: {punteggio}")

    print("\n--- 1. TEST AGGIUNTA PUNTI ---")
    print("Eseguo: aggiungi_punti(25)")
    aggiungi_punti(25)
    print(f"Punteggio globale attuale: {punteggio}")

    print("\n--- 2. DIMOSTRAZIONE ISOLAMENTO (SCOPE) ---")
    print("Tento di stampare la variabile 'info_funzione' dall'esterno...")

    # NOTA: La riga sotto è commentata appositamente. Se la decommenti, il programma crasha!
    # print(info_funzione)

    print("RISULTATO: Errore bloccato! Se attivassimo il codice, Python risponderebbe con:")
    print(">> NameError: name 'info_funzione' is not defined")
    print("Questo accade perché 'info_funzione' è totalmente ISOLATA e non esiste qui fuori.")

    print("\n--- 3. TEST AZZERAMENTO ---")
    azzera_punteggio()
    print(f"Punteggio globale alla fine: {punteggio}")
=====================
"""


"""
CASO UTILIZZO CON VARIABILE IN RETURN (PREFERITO):
"""

def aggiungi_punti(punteggio_attuale, punti):
    """
    Riceve il punteggio attuale e i punti da aggiungere.
    Restituisce il nuovo punteggio calcolato, senza modificare variabili globali.
    """
    nuovo_punteggio = punteggio_attuale + punti

    # Questa è una VARIABILE LOCALE. Esiste SOLO dentro questa funzione.
    info_funzione = "Sto elaborando l'aggiunta dei punti..."
    print(f"[Dentro aggiungi_punti] -> info_funzione: '{info_funzione}'")

    return nuovo_punteggio


def azzera_punteggio():
    """
    Restituisce semplicemente 0 per azzerare il punteggio nel flusso principale.
    """
    print("[Dentro azzera_punteggio] -> Viene restituito 0 per l'azzeramento.")
    return 0


def avvia_dimostrazione():
    """
    Funzione principale che gestisce lo STATO del punteggio localmente
    e dimostra l'isolamento delle variabili.
    """
    # Ora 'punteggio' è una variabile LOCALE a questa funzione. Non c'è nulla di globale.
    punteggio = 0

    print("--- STATO INIZIALE ---")
    print(f"Punteggio all'inizio: {punteggio}")

    print("\n--- 1. TEST AGGIUNTA PUNTI ---")
    print("Eseguo: punteggio = aggiungi_punti(punteggio, 25)")

    # Passiamo il punteggio attuale e sovrascriviamo la variabile con il nuovo valore restituito
    punteggio = aggiungi_punti(punteggio, 25)
    print(f"Punteggio attuale: {punteggio}")

    print("\n--- 2. DIMOSTRAZIONE ISOLAMENTO (SCOPE) ---")
    print("Tento di stampare la variabile 'info_funzione' dall'esterno...")

    # NOTA: Se decommenti la riga sotto, il programma crasha ancora.
    # print(info_funzione)

    print("RISULTATO: Errore bloccato! Se attivassimo il codice, Python risponderebbe con:")
    print(">> NameError: name 'info_funzione' is not defined")
    print("Questo accade perché 'info_funzione' è totalmente ISOLATA e non esiste qui fuori.")

    print("\n--- 3. TEST AZZERAMENTO ---")
    print("Eseguo: punteggio = azzera_punteggio()")

    # Riceviamo lo 0 dalla funzione e aggiorniamo la variabile locale
    punteggio = azzera_punteggio()
    print(f"Punteggio alla fine: {punteggio}")


# AVVIO DEL PROGRAMMA
if __name__ == "__main__":
    avvia_dimostrazione()