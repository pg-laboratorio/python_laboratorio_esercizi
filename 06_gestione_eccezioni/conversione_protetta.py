# Esercizio 2 - Conversione con Protezione
#
# Scrivi una funzione converti_intero(s) che converta una stringa
# in numero intero.
# Se la stringa non è un numero valido, stampa un messaggio di errore
# e restituisce 0.
#
# Esempio di output atteso:
#   converti_intero("42")    → 42
#   converti_intero("ciao")  → stampa errore, restituisce 0
#   converti_intero("3.14")  → stampa errore, restituisce 0


def converti_intero(s):
    try:
        return int(s)
    except ValueError:
        print(f"Errore: '{s}' non è un numero intero valido.")
        return 0


# --- Test ---
print(converti_intero("42"))    # 42
print(converti_intero("ciao"))  # errore + 0
print(converti_intero("3.14")) # errore + 0
print(converti_intero("-7"))    # -7
