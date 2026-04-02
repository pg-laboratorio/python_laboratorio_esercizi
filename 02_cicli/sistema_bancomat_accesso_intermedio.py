'''
Il software deve evolversi per proteggere sia la banca che il cliente. Il sistema di login non è più infinito: l'utente ha a disposizione un massimo di 3 tentativi. Ogni volta che sbaglia, il programma deve comunicargli quanti tentativi gli rimangono; se fallisce per la terza volta, la carta viene virtualmente "bloccata" e l'esecuzione termina. Se invece l'accesso va a buon fine, entra in gioco la gestione del portafoglio. Prima di confermare il prelievo, il sistema deve verificare che l'importo richiesto non superi il saldo disponibile (inizializzato, ad esempio, a 500€). In caso di successo, il bancomat eroga il denaro e mostra il saldo rimanente; in caso contrario, avvisa della mancanza di fondi.




----------




Problema:
Progettare un software per un bancomat che includa controlli di sicurezza sui tentativi di accesso e verifichi la disponibilità dei fondi sul conto corrente prima di autorizzare un'operazione.
Dati in ingresso:
PIN numerico inserito dall'utente.
Importo del prelievo desiderato.
Dati in uscita:
Messaggio con il numero di tentativi rimasti in caso di errore.
Messaggio di "Carta bloccata" dopo 3 fallimenti consecutivi.
Messaggio di "Saldo insufficiente" se l'importo richiesto supera il denaro disponibile.
Conferma dell'operazione e saldo residuo in caso di successo.
Specifiche tecniche:Inizializzare un saldo di partenza (es. 500€) e un contatore di tentativi (max 3).
Il ciclo di login deve interrompersi se il PIN è corretto o se i tentativi sono esauriti.
Usare strutture condizionali (if-else) per gestire sia l'esito del login che la validità del prelievo in base al saldo.

'''
# --- CONFIGURAZIONE INIZIALE ---
pin_segreto = 1234
saldo_disponibile = 500.0
tentativi_rimasti = 3

# --- FASE 1: AUTENTICAZIONE UTENTE ---
# Il ciclo continua finché ci sono tentativi disponibili
while tentativi_rimasti > 0:
    pin_inserito = int(input(f"Inserisci PIN ({tentativi_rimasti} tentativi rimasti): "))

    if pin_inserito == pin_segreto:
        print("Accesso effettuato!")
        break # Esce dal ciclo se il PIN è corretto
    else:
        tentativi_rimasti -= 1 # Decrementa il contatore in caso di errore

        if tentativi_rimasti > 0:
            print("PIN errato.")
        else:
            # Messaggio critico al raggiungimento dello zero
            print("Carta bloccata. Rivolgersi in filiale.")

# --- FASE 2: GESTIONE OPERAZIONI (Solo se autenticato) ---
# Verifichiamo che l'uscita dal ciclo sia avvenuta per PIN corretto e non per esaurimento tentativi
if pin_inserito == pin_segreto:
    prelievo = float(input("Quanto desideri prelevare? "))

    # Controllo copertura fondi
    if prelievo <= saldo_disponibile:
        # Aggiornamento del saldo e conferma
        saldo_disponibile -= prelievo
        print(f"Prelievo autorizzato. Saldo residuo: {saldo_disponibile}€")
    else:
        # Errore in caso di fondi insufficienti
        print("Saldo insufficiente per questa operazione.")


