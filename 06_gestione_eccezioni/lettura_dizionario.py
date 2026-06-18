# Esercizio 5 - Lettura da Dizionario
#
# Hai un dizionario di voti degli studenti.
# Scrivi una funzione voto_studente(dizionario, nome) che restituisce
# il voto dello studente cercato.
# Se il nome non è presente nel dizionario, gestisci l'eccezione
# e restituisce la stringa "studente non trovato".
#
# Esempio di output atteso:
#   voto_studente(voti, "Sara")   → 9
#   voto_studente(voti, "Elena")  → "studente non trovato"


def voto_studente(dizionario, nome):
    try:
        return dizionario[nome]
    except KeyError:
        return "studente non trovato"


# --- Test ---
voti = {"Luca": 8, "Sara": 9, "Marco": 6}

print(voto_studente(voti, "Luca"))   # 8
print(voto_studente(voti, "Sara"))   # 9
print(voto_studente(voti, "Elena"))  # studente non trovato
print(voto_studente(voti, "marco"))  # studente non trovato (attenzione: maiuscole!)
