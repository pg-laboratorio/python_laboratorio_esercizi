"""
PROGETTO
CONSEGNA:
Un negozio applica uno sconto in base all'importo totale di un acquisto.
Se l'importo è superiore a 200 €, viene applicato uno sconto del 15%.
Se l'importo è superiore a 100 €, lo sconto è del 10%.
Scrivi un programma che richieda in input l'importo totale,
calcoli lo sconto applicabile e visualizzi l'importo finale da pagare.

DATI INPUT:
- Importo totale dell'acquisto (importo_totale)

DATI OUTPUT:
- Importo finale da pagare (importo_finale)

PASSAGGI RISOLUTIVI:
- chiedere l'importo totale (importo_totale)
- calcolare l'importo scontato in base all'importo totale:
    se importo_totale > 200
        applico lo sconto del 15%
    altrimenti se importo_totale > 100
        applico lo sconto del 10%
    altrimenti
        non applico nessuno sconto
- mandare in output l'importo finale da pagare (importo_finale)

NB: l'ORDINE dei controlli è importante! Se controllassimo prima "> 100",
    un importo di 250 € rientrerebbe già lì e riceverebbe solo il 10%.
"""
# - chiedere l'importo totale (importo_totale)
importo_totale = float(input("Qual è l'importo totale? "))

# - se importo_totale > 200 applico lo sconto del 15%
if importo_totale > 200:
    importo_finale = importo_totale - importo_totale * 15 / 100
    print("Lo sconto applicato è del 15%")
# - altrimenti se importo_totale > 100 applico lo sconto del 10%
elif importo_totale > 100:
    importo_finale = importo_totale - importo_totale * 10 / 100
    print("Lo sconto applicato è del 10%")
# - altrimenti non applico nessuno sconto
else:
    importo_finale = importo_totale
    print("Nessuno sconto applicato")

# - mandare in output l'importo finale
print(f"La cifra da pagare è di: {importo_finale:.2f} €")
