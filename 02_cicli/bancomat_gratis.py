'''
PROGETTO:
OBIETTIVO:
Un utente può prelevare denaro da un bancomat virtuale, ma non può superare il saldo disponibile.
PASSAGGI RISOLUTIVI:
Il conto parte con un saldo di 200 €.
---> avvio un ciclo fintanto che il saldo è positivo
L'utente inserisce l'importo che vuole prelevare.
Se il saldo è sufficiente, il prelievo viene effettuato e il saldo aggiornato viene mostrato.
Se il saldo è insufficiente, il sistema avvisa l'utente e chiede un nuovo importo.
Il ciclo continua finché il saldo si azzera.
'''
# Il conto parte con un saldo di 200 €.
saldo = 200

# avvio un ciclo fintanto che il saldo è positivo
while saldo > 0:
    print(f"Il saldo disponibile è: {saldo} euro")
    # chiediamo l'importo da prelevare
    prelievo = int(input("Quanto vuoi prelevare? "))
    #verifico se il saldo è sufficiente
    if prelievo > saldo:
        print("Saldo insuffciente")
    else:
        #aggiorno il saldo e stampo il prelievo
        saldo = saldo - prelievo
        print(f"Hai prelevato {prelievo} euro")

print("Il saldo è terminato, grazie!")