"""
PROGETTO
CONSEGNA:
Sapendo che in un parcheggio la prima ora costa 2.50 €
mentre tutte le successive costano 1.50 €, scrivere un programma che richieda
in input il numero complessivo delle ore e visualizzi il totale da pagare.

DATI INPUT:
- Numero ore di permanenza (numero_ore)

DATI OUTPUT:
- Prezzo totale da pagare (prezzo_tot)

ALTRE VARIABILI:
- COSTANTE prezzo prima ora (PREZZO_PRIMA_ORA)
- COSTANTE prezzo ore successive (PREZZO_ORA)

PASSAGGI RISOLUTIVI:
- impostiamo le costanti PREZZO_PRIMA_ORA = 2.5 e PREZZO_ORA = 1.5
- chiediamo in input numero_ore
- se numero_ore <= 1 allora
    prezzo_tot = PREZZO_PRIMA_ORA
- altrimenti
    prezzo_tot = PREZZO_PRIMA_ORA + PREZZO_ORA * (numero_ore - 1)
- mandiamo in output prezzo_tot
"""
# - impostiamo le costanti PREZZO_PRIMA_ORA = 2.5 e PREZZO_ORA = 1.5
PREZZO_PRIMA_ORA = 2.5
PREZZO_ORA = 1.5

# - chiediamo in input numero_ore
numero_ore = int(input("Inserisci il numero di ore: "))

# - se numero_ore <= 1 allora prezzo_tot = PREZZO_PRIMA_ORA
if numero_ore <= 1:  # la condizione è: numero_ore <= 1
    # Cosa succede se la condizione è VERA?
    # ATTENZIONE! L'indentazione è fondamentale: il rientro di 4 spazi
    # (il tasto Tab dell'editor di solito li inserisce in automatico)
    # indica che queste righe formano un BLOCCO di codice dentro l'if.
    prezzo_tot = PREZZO_PRIMA_ORA
# - altrimenti prezzo_tot = PREZZO_PRIMA_ORA + PREZZO_ORA * (numero_ore - 1)
else:
    # Cosa succede se la condizione è FALSA?
    prezzo_tot = PREZZO_PRIMA_ORA + PREZZO_ORA * (numero_ore - 1)

# - mandiamo in output prezzo_tot
# NB: il nome della variabile deve essere IDENTICO a quello usato sopra
#     (prezzo_tot e prezzoTot per Python sono due variabili diverse!)
print(f"Il prezzo da pagare è: {prezzo_tot:.2f} €")
