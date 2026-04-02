'''
In questo scenario, devi sviluppare il modulo di autenticazione per uno sportello automatico. Il sistema deve agire come un guardiano: finché l'utente non inserisce il PIN corretto (che avrai precedentemente memorizzato in una variabile), il programma deve continuare a chiederlo ciclicamente. Solo una volta superato lo scoglio del login, l'utente viene accolto con un messaggio di conferma e gli viene data la possibilità di inserire la cifra che desidera prelevare. L'operazione si conclude visualizzando sullo schermo l'importo appena erogato.

-----------

Problema:
Un istituto bancario ha bisogno di un programma per gestire l'accesso ai propri sportelli automatici. Il sistema deve richiedere all'utente di inserire un PIN numerico e consentire il passaggio alla fase di prelievo solo se il codice è corretto.
Dati in ingresso:
Un numero intero inserito dall'utente (PIN).
Un numero decimale che rappresenta l'importo da prelevare (inserito solo dopo il login).
Dati in uscita:
Messaggio di errore "PIN errato" se il codice non corrisponde.
Messaggio di conferma "Accesso effettuato" una volta indovinato il PIN.
Messaggio finale che conferma l'importo prelevato.
Specifiche tecniche:
Definire un PIN segreto all'interno del codice.
Utilizzare un ciclo while per ripetere la richiesta del PIN finché l'utente non inserisce quello corretto.
Al termine del ciclo, gestire il prelievo dell'importo.

'''




#### SOLUZIONE A
# Definizione del PIN segreto
pin_segreto = 1234

# Ciclo di richiesta PIN con while True
while True:
    pin_inserito = int(input("Inserisci il tuo PIN: "))

    if pin_inserito == pin_segreto:
        print("Accesso effettuato")
        break # Esci dal ciclo se il PIN è corretto
    else:
        print("PIN errato. Riprova.")

# Fase di prelievo (eseguita solo dopo il login)
importo = float(input("Inserisci l'importo da prelevare: "))
print(f"Operazione completata. Hai prelevato: {importo}€")


### SOLUZIONE B
# Definizione del PIN segreto
pin_segreto = 1234

# Prima richiesta di input
pin_inserito = int(input("Inserisci il PIN per accedere: "))

# Ciclo di controllo con condizione espressa nel ciclo
while pin_inserito != pin_segreto:
    print("PIN errato! Riprova.")
    pin_inserito = int(input("Inserisci il PIN: ")) #NB devo richiedere il PIN

# Fase di prelievo (eseguita solo dopo il login)
print("Accesso effettuato!")
importo = float(input("Inserisci l'importo da prelevare: "))
print(f"Operazione completata. Hai prelevato {importo}€.")

