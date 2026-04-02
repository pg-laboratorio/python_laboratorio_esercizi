'''
CONSEGNA:
Un programma per un allenamento di corsa. L'utente deve inserire quanti km ha corso.
Se inserisce un numero negativo (impossibile),
il programma continua a chiederglielo finché non inserisce un numero positivo.

PROGETTO
RIASSUNTO: Registriamo i km solo se sono un numero positivo.

DATI INPUT:
- km percorsi dall'utente (km_percorsi)
DATI OUPUT:
- Avviso registrazione avvenuta

PASSAGGI RISOLUTIVI:
- Chiedo in input i km_percorsi
- avvio un ciclo while: finchè km_percorsi <0:
    - stampo errore ("Valore negativo non ammesso")
    - Richiedo di nuovo l'input dei km_percorsi
- Stampo "Hai corso Km_percorsi"
'''
# Chiedo in input i km_percorsi
km_percorsi = float(input("Inserisci i Km percorsi: "))

# avvio un ciclo while: finchè km_percorsi <0:
while km_percorsi < 0:
    # stampo errore ("Valore negativo non ammesso")
    print("Valore negativo non ammesso")
    # Richiedo di nuovo l'input dei km_percorsi
    km_percorsi = float(input("Inserisci i Km percorsi: "))

# Stampo "Hai corso km_percorsi"
print(f"Hai corso {km_percorsi:.3f} km")
