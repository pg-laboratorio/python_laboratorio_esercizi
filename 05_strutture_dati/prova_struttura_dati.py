"""
===============
LISTE
Immagina una lista come una serie di scatole numerate. Ogni scatola ha un numero d'ordine (l'indice), che parte sempre da 0. Le liste sono mutabili, il che significa che puoi aggiungere, togliere o cambiare gli elementi in corsa.
===============
"""
# --- Creazione e Indicizzazione ---
studenti = ["Alice", "Bob", "Charlie"]

# Accedere agli elementi tramite indice
primo_studente = studenti[0]  # "Alice"
ultimo_studente = studenti[-1] # "Charlie" (l'indice negativo parte dal fondo)

# --- Metodi di Modifica ---
studenti.append("Diana")       # Aggiunge "Diana" alla fine: ["Alice", "Bob", "Charlie", "Diana"]
studenti.insert(1, "Elena")    # Inserisce "Elena" all'indice 1: ["Alice", "Elena", "Bob", "Charlie", "Diana"]
studenti.remove("Bob")         # Cerca "Bob" e lo elimina: ["Alice", "Elena", "Charlie", "Diana"]

# --- Iterazione e condizioni ---
print("Studenti con un nome più lungo di 4 lettere:")
for studente in studenti:
    if len(studente) > 4:
        print(f"- {studente}")


"""
===============
TUPLE
Le tuple sono identiche alle liste, ma con una differenza fondamentale: sono immutabili. Una volta create, non puoi modificarle, aggiungere elementi o rimuoverli. Si usano per proteggere i dati da modifiche accidentali o per rappresentare record fissi.
===============
"""
# --- Caso d'uso 1: Coordinate geografiche (GPS) ---
# Se le coordinate cambiassero, cambieresti luogo! La tupla garantisce l'integrità.
posizione_milano = (45.4642, 9.1900)
print(f"Latitudine: {posizione_milano[0]}, Longitudine: {posizione_milano[1]}")

# --- Caso d'uso 2: Record fissi (es. dati di un profilo) ---
utente_sistema = ("mario_rossi", "Amministratore", "2026-05-28")

# Nota: Se provassi a fare `utente_sistema[1] = "Utente Semplice"`, Python bloccherà il programma.



"""
===============
DIZIONARI
Sono delle coppie vhiave-valore. Nei dizionari si usano delle chiavi personalizzate (spesso stringhe). È come una rubrica telefonica: cerchi il Nome (chiave) per trovare il Numero (valore).
===============
"""
# --- Creazione di un Dizionario ---
smartphone = {
    "marca": "Apple", #marca <-chiave   Apple <-valore
    "modello": "iPhone 15",
    "prezzo": 999.99,
    "disponibile": True
}

# Accedere a un valore tramite la sua chiave
print(smartphone["modello"]) # Output: iPhone 15

# --- Metodi del Dizionario ---
chiavi = smartphone.keys()     # Restituisce l'elenco delle chiavi
valori = smartphone.values()   # Restituisce l'elenco dei valori

# --- Iterazione con .items() ---
# Questo metodo restituisce sia la chiave che il valore contemporaneamente nel ciclo for
print("\nSpecifiche tecniche:")
for chiave, valore in smartphone.items():
    print(f"- {chiave.capitalize()}: {valore}")



"""
===============
LISTE DI DIZIONARI
Sono strutture annidate -> una lista che contiene una serie di dizionari.
===============
"""
# Un finto database di un negozio di videogiochi
catalogo_giochi = [
    {"titolo": "Zelda: TotK", "piattaforma": "Switch", "prezzo": 69.99},
    {"titolo": "Cyberpunk 2077", "piattaforma": "PC", "prezzo": 29.99},
    {"titolo": "Elden Ring", "piattaforma": "PS5", "prezzo": 59.99}
]

# Come iterare dentro una struttura annidata
print("Giochi in offerta (sotto i 60€):")

for gioco in catalogo_giochi:
    # 'gioco' è un dizionario a ogni passaggio del ciclo
    if gioco["prezzo"] < 60.00:
        print(f"{gioco['titolo']} per {gioco['piattaforma']} costa solo {gioco['prezzo']}€!")


