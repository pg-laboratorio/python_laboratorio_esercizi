'''
PROGETTO
CONSEGNA:
Quando la media di tre valori in input
è inferiore ad un valore in input accendo il sistema.
#NB: invece che riscrivere il problema ho
fatto un riassunto evidenziando i punti chiave.

DATI INPUT:
- I tre valori (stanza_1, stanza_2, stanza_3)
- Valore chiesto all'utente (valore_fisso)

DATI OUTPUT:
- la media dei tre valori (media_valori)
- accendo o spengo il sistema

ALTRE VARIABILI:

PASSAGGI RISOLUTIVI:
-acquisisco in input le tre 4 variabili
- faccio la media dei tre valori
- mando in output la media
-se la condizione è valore_fisso > media_valori allora:
    stampo acceso
altrimenti:
    stampo spento

'''
#acquisisco in input le tre 4 variabili
stanza_1 = float(input("inserisci la temperatura della stanza: "))
stanza_2 = float(input("inserisci la temperatura della stanza: "))
stanza_3 = float(input("inserisci la temperatura della stanza: "))
valore_fisso = float(input("inserisci il valore fisso: "))
#faccio la media dei tre valori
media_valori = (stanza_1 + stanza_2 + stanza_3)/3
print(f"La media è: {media_valori:.2f} vol/h") #con fsting posso usare :.2f per indicare due decimali
#se la condizione è valore_fisso > media_valori allora: stampo acceso
if valore_fisso > media_valori:
    print("Acceso")
#altrimenti:
else:
    print("Spento")

