# Esercizio 6 - Try / Except / Else / Finally
#
# Scrivi una funzione apri_file(nome) che prova ad aprire un file
# di testo e ne stampa il contenuto.
# Usa:
#   - except  → per gestire il caso in cui il file non esiste
#   - else    → per stampare "Lettura completata" se non ci sono errori
#   - finally → per stampare sempre "Operazione terminata"
#
# Esempio di output se il file esiste:
#   <contenuto del file>
#   Lettura completata.
#   Operazione terminata.
#
# Esempio di output se il file NON esiste:
#   Errore: il file 'inesistente.txt' non esiste.
#   Operazione terminata.


def apri_file(nome):
    try:
        f = open(nome, "r", encoding="utf-8")
        contenuto = f.read()
        f.close()
    except FileNotFoundError:
        print(f"Errore: il file '{nome}' non esiste.")
    else:
        print(contenuto)
        print("Lettura completata.")
    finally:
        print("Operazione terminata.")


# --- Test ---
# Per testare il caso positivo, crea un file chiamato "dati.txt"
# nella stessa cartella dello script, poi decommenta la riga:
# apri_file("dati.txt")

apri_file("inesistente.txt")
