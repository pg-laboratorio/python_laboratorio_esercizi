# Esercizio 4 - Più Eccezioni Insieme
#
# Scrivi una funzione calcola(a, b) che restituisce a / b.
# Gestisci con messaggi distinti:
#   - il caso in cui a o b non siano numeri validi (ValueError)
#   - il caso in cui b sia zero (ZeroDivisionError)
#
# Esempio di output atteso:
#   calcola("dieci", 2)  → messaggio: non sono numeri
#   calcola(10, 0)       → messaggio: divisione per zero
#   calcola(10, 4)       → 2.5


def calcola(a, b):
    try:
        return float(a) / float(b)
    except ValueError:
        print("Errore: i valori devono essere numeri.")
        return None
    except ZeroDivisionError:
        print("Errore: non puoi dividere per zero.")
        return None


# --- Test ---
print(calcola(10, 4))       # 2.5
print(calcola("dieci", 2))  # errore tipo
print(calcola(10, 0))       # errore divisione
print(calcola("5", "2"))    # 2.5  (le stringhe numeriche vengono convertite)
