'''
PROGETTO
CONSEGNA
Un distributore automatico ha una capacità massima di 50 caffè.
I clienti arrivano uno alla volta e inseriscono il numero di caffè che desiderano acquistare. Ogni caffè costa 0,60 €.

DATI INPUT
-Chiedere all'utente quanti caffe vuol acquistare (caffe_richiesti)

DATI OUTPUT
-Prezzo totale dei caffe acquistati(costo_totale)
-Caffe restanti(caffe_restanti)
-sistema spento se finiscono i caffe

VARIABILI COSTANTI
-PREZZO_CAFFE = 0.60

PASSAGGI
-Imposto la cpienza della macchinetta a 50 caffe(caffe_restanti)
-Imposto la costante del prezzo del caffe a 0.60 (PREZZO_CAFFE)
-Avvio il ciclo while per verificare che ci siano caffe nella macchinetta
    chiedo all'utente quanti caffe vuole
    Se caffe_richiesti <= caffe_restanti:
        calcolo il costo totale dei caffe
        stampo il costo totale
        calcolo i caffe restanti
        stampo i caffe restanti
    altrimenti
        errore, troppa richiesta di caffe
        stampo i caffe restanti
spengo il sistema per mancanza di caffe
'''

#Imposto la cpienza della macchinetta a 50 caffe
caffe_restanti = 50

#Imposto la costante del prezzo del caffe a 0.60
PREZZO_CAFFE = 0.60

#Avvio il ciclo while per verificare che ci siano caffe nella macchinetta
while caffe_restanti > 0:
    #chiedo all'utente quanti caffe vuole
    caffe_richiesti = int(input("Quanti caffe vuoi acquistare: "))
    #Se caffe_richiesti <= caffe_restanti:
    if caffe_richiesti <= caffe_restanti:
        #calcolo il costo totale dei caffe
        costo_totale = PREZZO_CAFFE * caffe_richiesti
        #stampo il costo totale
        print(f"Il totale da pagare è:{costo_totale} €")
        #calcolo i caffe restanti
        caffe_restanti = caffe_restanti - caffe_richiesti
        #stampo i caffe restanti
        print(f"i caffe restanti nella macchinetta sono:{caffe_restanti}")
    else:
        #errore, troppa richiesta di caffe
        print(f"Troppi caffe richiesti, i caffe restanti sono:{caffe_restanti}")
#spengo il sistema per mancanza di caffe
print(f"Spegnimento del sistema, caffe esuriti")















