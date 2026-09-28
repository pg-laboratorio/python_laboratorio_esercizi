"""
PROGETTO
CONSEGNA:
Il sistema di ventilazione di un edificio si accende quando la media dei valori
di areazione, registrati in tre diverse stanze, è inferiore a un valore fissato.
Implementa un programma che consenta di fissare un limite minimo, ricevere in input
i dati delle tre stanze, calcolare la media e segnalare se il sistema verrà acceso o meno.
Esempio valore areazione: 0,5-6 [vol/h]

IN SINTESI (NB: riassumere la consegna aiuta a individuarne i punti chiave):
se la media dei tre valori è inferiore al limite, accendo il sistema.

DATI INPUT:
- Limite minimo di areazione (limite_minimo)
- I valori di areazione delle tre stanze (stanza_1, stanza_2, stanza_3)

DATI OUTPUT:
- La media dei tre valori (media_valori)
- Messaggio "Sistema acceso" oppure "Sistema spento"

PASSAGGI RISOLUTIVI:
- acquisisco in input le 4 variabili
- calcolo la media dei tre valori
- mando in output la media
- se media_valori < limite_minimo allora
    stampo "Sistema acceso"
- altrimenti
    stampo "Sistema spento"
"""
# - acquisisco in input le 4 variabili
limite_minimo = float(input("Inserisci il limite minimo di areazione (vol/h): "))
stanza_1 = float(input("Inserisci il valore di areazione della stanza 1 (vol/h): "))
stanza_2 = float(input("Inserisci il valore di areazione della stanza 2 (vol/h): "))
stanza_3 = float(input("Inserisci il valore di areazione della stanza 3 (vol/h): "))

# - calcolo la media dei tre valori
# NB: le parentesi servono! Senza, Python dividerebbe per 3 solo stanza_3
media_valori = (stanza_1 + stanza_2 + stanza_3) / 3

# - mando in output la media
print(f"La media è: {media_valori:.2f} vol/h")  # con le f-string, :.2f mostra due decimali

# - se media_valori < limite_minimo allora stampo "Sistema acceso"
if media_valori < limite_minimo:
    print("Sistema acceso")
# - altrimenti stampo "Sistema spento"
else:
    print("Sistema spento")
