'''
In questa versione avanzata, lo sportello permette di effettuare operazioni multiple senza dover reinserire il PIN ogni volta. Dopo aver superato la fase di login (sempre con il limite dei 3 tentativi), l'utente entra in una fase operativa continua. Qui può inserire diversi importi da prelevare uno dopo l'altro. Il ciclo di prelievo si interrompe solo quando l'utente digita il valore 0, segnalando la volontà di uscire. Il programma deve essere in grado di "tenere il conto" di tutto il denaro erogato durante la sessione tramite un accumulatore. Al termine, il sistema deve generare un riepilogo finale che mostri la somma totale prelevata e quanto denaro è rimasto effettivamente sul conto corrente.

Nota Tecnica: Per questa sfida non puoi usare liste o strutture dati complesse; devi gestire tutto il flusso esclusivamente con variabili numeriche e cicli nidificati.



------------

Problema:
Si desidera creare un simulatore di sportello bancario avanzato che permetta a un utente, dopo essersi autenticato con successo, di effettuare più operazioni di prelievo in una singola sessione. Il sistema deve calcolare quanto denaro viene erogato in totale prima di chiudere la sessione.
Dati in ingresso:
PIN numerico per l'autenticazione (max 3 tentativi).
Una serie di importi da prelevare inseriti uno dopo l'altro.
Il valore 0 per indicare la volontà di terminare la sessione.
Dati in uscita:
Conferma per ogni singolo prelievo effettuato con successo.
Riepilogo finale al termine della sessione che mostri il Totale prelevato complessivamente e il Saldo finale rimasto sul conto.
Specifiche tecniche:Gestire la fase di login iniziale (max 3 tentativi).Se l'accesso è autorizzato, avviare un secondo ciclo per gestire i prelievi ripetuti.Utilizzare una variabile "accumulatore" per sommare tutti i prelievi validi effettuati durante la sessione.

Nota bene: Non è consentito l'uso di liste; tutta la gestione deve avvenire tramite variabili numeriche e cicli.

'''
# --- CONFIGURAZIONE E STATO INIZIALE ---
pin_segreto = 1234
saldo = 1000.0
totale_prelevato_sessione = 0.0  # Accumulatore per il riepilogo finale
tentativi = 3
autenticato = False             # Flag di controllo per l'accesso

# 1. FASE DI AUTENTICAZIONE
# Il ciclo gestisce i tentativi di accesso dell'utente
while tentativi > 0:
    pin = int(input(f"Inserisci PIN (Tentativi rimasti: {tentativi}): "))

    if pin == pin_segreto:
        break                   # Esco dal ciclo di login

    tentativi -= 1              # Riduco i tentativi solo in caso di errore
    if tentativi > 0:
        print("PIN errato. Riprova.")

# 2. FASE OPERATIVA (Eseguita solo se autenticato == True)
if pin == pin_segreto:
    print("--- Sessione di Prelievo Aperta ---")

    # Ciclo infinito per permettere prelievi multipli
    while True:
        print(f"Saldo attuale: {saldo}€")
        richiesta = float(input("Importo da prelevare (Inserisci 0 per terminare): "))

        # Condizione di uscita dal ciclo operativo
        if richiesta == 0:
            print("Chiusura sessione in corso...")
            break

        # --- CONTROLLI DI VALIDITÀ DEL PRELIEVO ---
        if richiesta > saldo:
            print("Errore: Fondi insufficienti sul conto.")
        elif richiesta < 0:
            print("Errore: Non puoi inserire un importo negativo.")
        else:
            # OPERAZIONE ANDATA A BUON FINE
            # Sottraiamo dal saldo e aggiungiamo al contatore della sessione
            saldo -= richiesta
            totale_prelevato_sessione += richiesta
            print(f"Successo: Erogazione di {richiesta}€ effettuata.")

    # 3. RIEPILOGO FINALE (Output di chiusura)
    print("      RIEPILOGO CHIUSURA")
    print(f"Totale prelevato oggi: {totale_prelevato_sessione}€")
    print(f"Saldo residuo finale:  {saldo}€")

else:
    # Messaggio mostrato solo se i tentativi sono finiti senza successo
    print("Accesso negato: Carta bloccata o troppi tentativi falliti.")