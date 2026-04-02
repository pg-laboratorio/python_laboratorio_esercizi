'''
PROGETTO:
CONSEGNA:
Il sistema gestionale del museo d'arte contemporanea della nostra città ha bisogno di aiuto.
Gli serve un programma che, dato il numero di persone del gruppo che svolge la
visita, calcoli in automatico il prezzo complessivo.
Considera che il prezzo di un biglietto è un fisso di 10€.

DATI INPUT:
- Numero di persone (numeroPersone)

DATI OUTPUT:
- Prezzo complessivo biglietto (prezzoTotale)

ALTRE VARIABILI:
- Prezzo COSTANTE di 10€ (PREZZO) #nb: i nomi delle costanti sono in maiuscolo

PASSAGGI:
- settiamo la variabile PREZZO = 10
- chiediamo in input il numeroPersone
- calcoliamo il prezzoTotale = numeroPersone * PREZZO
- mandiamo in ouput il prezzoTotale
'''
# - settiamo la variabile PREZZO = 10
PREZZO = 10
# - chiediamo in input il numeroPersone
numeroPersone = int(input("Inserisci il numero di persone: ")) # Nb: il tipo di dato in input è sempre una stringa, devo fare il casting con int()
# - calcoliamo il prezzoTotale = numeroPersone * PREZZO
prezzoTotale = numeroPersone * PREZZO
# - mandiamo in ouput il prezzoTotale
print(f"Il prezzo totale è {prezzoTotale} €")
