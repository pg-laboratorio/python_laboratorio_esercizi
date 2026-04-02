'''
Un cinema vuole calcolare gli incassi della giornata. Scrivi un programma che: Chieda quanti spettacoli ci sono stati oggi. Per ogni spettacolo, chieda quanti biglietti sono stati venduti e il prezzo di ogni biglietto. Calcoli e stampi l'incasso totale della giornata.


progetto:
obbiettivo: stampare l'incasso totale
Dati input:

-chiediamo in input quanti film sono stati riprodotti (numero_film)
- chiediamo in input quanti biglietti sono stati venduti per ogni spettacolo (numero_biglietti)
- chiediamo il prezzo del biglietto per ogni film (prezzo_biglietto)
Dati output:
incasso della giornata (incasso_tot)
Passaggi:
settiamo l'incasso_tot = 0
-chiediamo in input quanti film sono stati riprodotti (numero_film)
avviamo il ciclo for che per ogni spettacolo:
    chiediamo in input quanti biglietti sono stati venduti per ogni spettacolo (numero_biglietti)
   chiediamo il prezzo del biglietto per ogni film (prezzo_biglietto)
    calcoliamo l'incasso_tot
stampiamo l'incasso_tot
'''
# settiamo l'incasso_tot = 0
incasso_tot = 0
# chiediamo in input quanti film sono stati riprodotti (numero_film)
numero_film = int(input("quanti film sono stati riprodotti?: "))
# avviamo il ciclo for che per ogni spettacolo:
for i in range (numero_film):
    print (f"spettacolo {i+1}")
    # chiediamo in input quanti biglietti sono stati venduti per ogni spettacolo
    numero_biglietti = int(input("quanti biglietti sono stati venduti? : "))
    # chiediamo il prezzo del biglietto per ogni film
    prezzo_biglietto = float(input("quanto costa un biglietto? : "))
    incasso_tot = incasso_tot + (prezzo_biglietto * numero_biglietti)
print (f"hai incassoto {incasso_tot} euro")