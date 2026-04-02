'''
PROGETTO
Consegna:
Un negozio applica uno sconto in base all’importo totale di un acquisto.
Se l’importo è superiore a 200 €, viene applicato uno sconto del 15%.
Se l’importo è superiore a 100 €, lo sconto è del 10%.
Scrivi un programma che richieda in input l’importo totale,
calcoli lo sconto applicabile e visualizzi l’importo finale da pagare.

dati input:
- quanto è l'importo totale

dati output:
- quanto è l'importo finale da pagare

passaggi:

- chiedere quanto è l'importo totale ( importo_totale )

- calcolare l'importo scontato in base all' importo totale
    se importo_totale > 200
        applico lo sconto del 15%
    se importo_totale > 100
        applico lo sconto del 10%
    altrimenti
        non applico nessuno sconto

- mandare in output la cifra finale da pagare ( importo_finale )

'''
#chiedere quanto è l'importo totale ( importo_totale )
importo_totale = float(input("qual'è l'importo totale " ))

#se importo_totale > 200 applico lo sconto del 15%
if importo_totale > 200:
    importo_finale = importo_totale - importo_totale * 15 / 100
    print("lo sconto applicato è del 15% ")
# se importo_totale > 100 applico lo sconto del 10%
elif importo_totale > 100:
    importo_finale = importo_totale - importo_totale * 10 / 100
    print("lo sconto applicato è del 10%")
#altrimenti non applico nessuno sconto
else:
    importo_finale = importo_totale

# output valore finale
print(f"la cifra che devi pagare è di: {importo_finale:.2f}€")