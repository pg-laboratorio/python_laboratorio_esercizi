'''
La Missione Ares-1 ha come obiettivo primario la distruzione di una barriera nemica prima dell'esaurimento delle risorse balistiche. La missione ha inizio con la Fase di Preparazione, durante la quale il sistema richiede all'operatore di definire la dotazione iniziale di munizioni. In questa fase, è attivo un protocollo di validazione: se viene inserito un valore inferiore a 1, il sistema segnalerà un errore per munizioni insufficienti, reiterando la richiesta finché non viene fornito un dato valido. Solo a quel punto verrà confermato che i sistemi sono pronti al fuoco.

Si passa quindi alla Fase di Battaglia, un processo ciclico che vede la contrapposizione tra l'arsenale della nave e una barriera energetica nemica con 50 punti resistenza. Il combattimento prosegue senza sosta finché la barriera resta integra e sono disponibili colpi in stiva. Durante ogni turno, l'utente decide l'entità del danno da infliggere; ogni attivazione consuma un'unità di munizioni e riduce i punti della barriera del valore scelto. Al termine di ogni azione, il sistema aggiorna in tempo reale lo stato tattico, indicando i residui della barriera e il conteggio delle munizioni rimaste.

L'Esito della Missione viene determinato automaticamente alla conclusione delle ostilità. Se l'integrità della barriera scende a zero o meno, il sistema proclamerà la vittoria per distruzione dell'obiettivo. Al contrario, qualora la barriera risultasse ancora attiva nonostante l'esaurimento delle munizioni, verrà dichiarata la sconfitta e il fallimento della missione.

'''
# --- FASE 1: PREPARAZIONE ---
munizioni = 0

# Ciclo di validazione: continua finché il numero non è almeno 1
while munizioni < 1:
    munizioni = int(input("Inserisci il numero di munizioni iniziali (minimo 1): "))
    if munizioni < 1:
        print("Errore: Munizioni insufficienti! Riprova.")

print("Sistemi pronti al fuoco!")

# --- FASE 2: BATTAGLIA ---
barriera_nemica = 50

# Il ciclo continua finché il nemico è vivo E abbiamo colpi
while barriera_nemica > 0 and munizioni > 0:
    print(f"\nStato: Barriera Nemica {barriera_nemica} | Munizioni {munizioni}")

    # Chiediamo il danno da infliggere
    danno = int(input("Quanto danno vuoi infliggere? "))

    # Aggiorniamo le risorse
    munizioni -= 1  # Consumiamo un colpo
    barriera_nemica -= danno  # Scaliamo il danno

    print(f"Colpo esploso! Barriera nemica colpita.")

# --- FASE 3: ESITO ---
if barriera_nemica <= 0:
    print("VITTORIA: Barriera distrutta! Missione compiuta.")
else:
    print("SCONFITTA: Munizioni esaurite! Missione fallita.")