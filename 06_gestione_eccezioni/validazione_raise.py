# Esercizio 7 - Validazione con Raise
#
# Scrivi una funzione imposta_eta(eta) che accetta un'età come parametro.
# Se il valore non rispetta le regole, solleva manualmente un ValueError
# con un messaggio chiaro.
# Regole:
#   - deve essere un numero intero
#   - non può essere negativo
#   - non può superare 120
#
# Poi testa la funzione chiamandola dentro un blocco try/except.
#
# Esempio di output atteso:
#   imposta_eta(17)   → Età impostata: 17
#   imposta_eta(-5)   → Errore: l'età non può essere negativa.
#   imposta_eta(150)  → Errore: età non realistica.


def imposta_eta(eta):
    if not isinstance(eta, int):
        raise ValueError("L'età deve essere un numero intero.")
    if eta < 0:
        raise ValueError("L'età non può essere negativa.")
    if eta > 120:
        raise ValueError("Età non realistica: il valore massimo è 120.")
    print(f"Età impostata: {eta}")


# --- Test ---
valori_da_testare = [17, -5, 150, 0, "venti", 120]

for v in valori_da_testare:
    try:
        imposta_eta(v)
    except ValueError as e:
        print(f"Errore per il valore {repr(v)}: {e}")
