"""
PROGETTO
CONSEGNA:
Il sistema gestionale del museo d'arte contemporanea della nostra città ha bisogno di aiuto.
Gli serve un programma che, dato il numero di persone del gruppo che svolge la
visita, calcoli in automatico il prezzo complessivo.
Considera che il prezzo di un biglietto è un fisso di 10€.

DATI INPUT:
- Numero di persone (numero_persone)

DATI OUTPUT:
- Prezzo complessivo (prezzo_totale)

ALTRE VARIABILI:
- COSTANTE prezzo di un biglietto = 10€ (PREZZO_BIGLIETTO)
  NB: i nomi delle costanti si scrivono in MAIUSCOLO

PASSAGGI RISOLUTIVI:
- impostiamo la costante PREZZO_BIGLIETTO = 10
- chiediamo in input numero_persone
- calcoliamo prezzo_totale = numero_persone * PREZZO_BIGLIETTO
- mandiamo in output prezzo_totale
"""
# - impostiamo la costante PREZZO_BIGLIETTO = 10
PREZZO_BIGLIETTO = 10

# - chiediamo in input numero_persone
# NB: input() restituisce SEMPRE una stringa, quindi devo convertirla con int()
numero_persone = int(input("Inserisci il numero di persone: "))

# - calcoliamo prezzo_totale = numero_persone * PREZZO_BIGLIETTO
prezzo_totale = numero_persone * PREZZO_BIGLIETTO

# - mandiamo in output prezzo_totale
print(f"Il prezzo totale è {prezzo_totale} €")
