"""
CONVERTITORE VALUTA (EURO -> DOLLARI)
Autore: @nickname

print VS return
Questo esercizio serve a scardinare l'abitudine di usare print dentro le funzioni, dobbiamo usare il valore di ritorno per i calcoli successivi.
"""

# Costante per il tasso di cambio fisso (1 Euro = 1.08 Dollari)
TASSO_CAMBIO = 1.08

def converti_euro_in_dollari(importo_euro):
    """
    Riceve un importo in euro e restituisce l'importo convertito in dollari.

    args:
    - importo_euro (float): la cifra in euro da convertire

    return:
    - float: l'importo convertito in dollari
    """
    return importo_euro * TASSO_CAMBIO

def mostra_menu():
    """Mostra le istruzioni del programma"""
    print("\n")
    print("-- Convertitore Euro ➔ Dollaro --")
    print("Opzioni:")
    print("- Inserisci un importo numerico (es. 50 o 12.50)")
    print("- q : chiudere il programma")
    print("\n")

def avvia_convertitore():
    """
    Funzione principale per la gestione dell'input utente e della conversione
    """
    while True:
        mostra_menu()

        # Gestione input utente
        scelta_utente = input("Inserisci l'importo in Euro: ").strip()

        # Condizione chiusura programma
        if scelta_utente.lower() == 'q':
            print("\nChiusura in corso... Arrivederci!")
            break

        # Validazione input utente
        euro = float(scelta_utente)
        if euro < 0:
            print("Errore: L'importo non può essere negativo!")
            continue


        # Invocazione della funzione e calcolo del risultato
        dollari = converti_euro_in_dollari(euro)

        # Stampa finale del risultato
        print("\n--- Risultato Conversione ---")
        print(f"Importo inserito: {euro:.2f} €")
        print(f"Importo convertito: {dollari:.2f} $")
        print(f"Tasso di cambio applicato: {TASSO_CAMBIO}")
        print("-----------------------------")

# Avvio effettivo del programma
if __name__ == "__main__":
    avvia_convertitore()