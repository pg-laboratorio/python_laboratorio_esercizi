# Esercizio 1 - Divisione Sicura
#
# Completa la funzione in modo che non vada in crash
# quando il divisore è zero.
# Usa try/except per gestire l'errore e restituisci None in quel caso.
#
# Esempio di output atteso:
#   dividi(10, 2)  → 5.0
#   dividi(10, 0)  → None  (stampa un messaggio di errore)


def dividi(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Errore: non si può dividere per zero!")
        return None


# --- Test ---
print(dividi(10, 2))   # 5.0
print(dividi(10, 0))   # None
print(dividi(7, 2))    # 3.5
