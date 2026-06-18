# Esercizio 3 - Accesso Sicuro a una Lista
#
# Scrivi una funzione elemento(lista, indice) che restituisce
# l'elemento alla posizione indicata.
# Se l'indice non esiste, restituisce la stringa "indice non valido".
#
# Nota: gli indici negativi in Python sono validi (es. -1 = ultimo elemento),
# quindi non sollevano IndexError.
#
# Esempio di output atteso:
#   elemento(frutti, 1)   → "pera"
#   elemento(frutti, 10)  → "indice non valido"
#   elemento(frutti, -1)  → "banana"


def elemento(lista, indice):
    try:
        return lista[indice]
    except IndexError:
        return "indice non valido"


# --- Test ---
frutti = ["mela", "pera", "banana"]

print(elemento(frutti, 0))   # mela
print(elemento(frutti, 1))   # pera
print(elemento(frutti, -1))  # banana
print(elemento(frutti, 10))  # indice non valido
print(elemento(frutti, -5))  # indice non valido
