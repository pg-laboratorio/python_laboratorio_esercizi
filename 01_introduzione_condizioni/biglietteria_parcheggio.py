'''
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
- COSTANTE prezzo prima ora (PREZZOPRIMAORA)
- COSTANTE prezzo ore succevvive (PREZZOORA)

PASSAGGI RISOLUTIVI:
- settiamo le variabili costanti PREZZO_PRIMAORA=2.5 e PREZZO_ORA=1.5
- chiediamo in input numero_ore
- se il numero di ore <= 1 allora
    il prezzo sarà 2.5
- altrimenti
    il prezzo sarà 2.5 + 1.5 * (numero_ore-1)
- mando in output il prezzo_tot
'''
# - settiamo le variabili costanti PREZZOPRIMAORA=2.5 e PREZZOORA=1.5
PREZZO_PRIMAORA = 2.5
PREZZO_ORA = 1.5
# - chiediamo in input numeroOre
numero_ore = int(input("Inserisci il numero ore: "))
# - se il numero di ore <= 1 allora
#    il prezzo sarà PREZZO_PRIMAORA
if numero_ore <= 1: #la mia condizione è numero_ore<=1
    #cosa succede se la condizione è vera?
    #ATTENTO! L'indentazione (Tab) è fondamentale!
    #Questo rientro a destra del testo indica un blocco di codice!
    prezzo_tot = PREZZO_PRIMAORA
#- altrimenti
#    il prezzo sarà PREZZOPRIMAORA + PREZZOORA * (numeroOre-1)
else:
    #cosa faccio se la condizione è falsa?
    prezzo_tot = PREZZO_PRIMAORA + PREZZO_ORA * (numero_ore - 1)
# - mando in output il prezzoTot
print(f"Il prezzo da pagare è: {prezzoTot} €")




