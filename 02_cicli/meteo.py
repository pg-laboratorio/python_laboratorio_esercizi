"""
PROGETTO: Analisi Precipitazioni Settimanali (Senza Liste)

CONSEGNA:
Un servizio meteo vuole analizzare le precipitazioni degli ultimi 7 giorni.
Scrivi un programma che:
1. Chieda all’utente di inserire la precipitazione giornaliera per 7 giorni.
2. Calcoli la precipitazione media della settimana.
3. Riporti qual è stata la precipitazione massima e quale la minima.

DATI INPUT:
- pioggia (float): valore in millimetri inserito dall'utente a ogni ciclo (viene sovrascritto).

DATI OUTPUT:
- media (float): media aritmetica calcolata alla fine del ciclo.
- massima (float): il valore più alto registrato durante i confronti.
- minima (float): il valore più basso registrato durante i confronti.

PASSAGGI RISOLUTIVI:
1. Inizializzazione: Si azzera la variabile per la somma totale e si impostano a None
   le variabili 'massima' e 'minima'.
2. Ciclo di lettura (7 iterazioni): Viene chiesto l'input per ogni giorno.
   - Il valore viene sommato a 'somma_totale'.
   - Se è il giorno 1, il valore diventa sia il massimo che il minimo iniziale.
   - Nei giorni successivi (da 2 a 7), il valore viene confrontato con 'massima' e 'minima'
     correnti per aggiornarli se necessario.
3. Calcolo della Media: Finita la raccolta dati, si divide la 'somma_totale' per 7.
4. Visualizzazione: Si stampano a video i risultati finali.
"""

# 1. Inizializzazione delle variabili
somma_totale = 0.0
massima = None
minima = None

# 2. Ciclo di 7 giorni per raccolta e confronto dati in tempo reale
for i in range(1, 8):
    pioggia = float(input(f"Inserisci la precipitazione del giorno {i} (in mm): "))

    # Accumulo per la media
    somma_totale += pioggia

    # Logica per determinare massimo e minimo senza memorizzare i dati in liste
    if i == 1:
        # Il primo giorno il valore inserito è sia il record massimo che minimo
        massima = pioggia
        minima = pioggia
    else:
        # Dai giorni successivi si fanno i confronti con i record precedenti
        if pioggia > massima:
            massima = pioggia
        if pioggia < minima:
            minima = pioggia

# 3. Calcolo finale della media
media = somma_totale / 7

# 4. Visualizzazione dei dati di Output
print("\n--- Resoconto Meteo della Settimana ---")
print(f"Precipitazione media: {media:.2f} mm")
print(f"Precipitazione massima: {massima:.2f} mm")
print(f"Precipitazione minima: {minima:.2f} mm")