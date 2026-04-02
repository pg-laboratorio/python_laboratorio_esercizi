'''
Operazione Deep Space
Il comando della missione ti ha assegnato un obiettivo critico: portare la sonda Ares-1 oltre il blocco nemico. Il successo dipende dalla precisione dei sistemi di bordo e dalla tua capacità di gestire le risorse limitate.
Fase 1: Carico navicella
Prima di accendere i motori, è obbligatorio registrare le risorse di bordo attraverso due cicli di validazione:
Carburante: Il sistema deve richiedere l'inserimento dei litri di propellente. Se l'operatore inserisce un valore negativo, il programma deve mostrare l'errore "Valore negativo non ammesso!" e ripetere la richiesta finché non viene fornito un numero valido, confermando infine con "Carburante registrato correttamente".
Arsenale: Subito dopo, il sistema deve richiedere il numero di munizioni (colpi laser) disponibili. Anche in questo caso, non sono ammessi valori negativi: in caso di errore, deve apparire il messaggio "Errore: arsenale non valido!" fino all'inserimento di un dato corretto, concludendo con "Sistemi d'arma pronti".
Fase 2: Ingaggio
Una volta nello spazio, la Ares-1 si troverà di fronte a un incrociatore nemico con scudi al 100%. Dovrai implementare un ciclo di combattimento che continui finché gli scudi nemici sono sopra lo zero ed hai ancora munizioni disponibili.
Durante ogni turno, si applicano le seguenti regole:
No danni negativi: L'utente inserisce i danni inflitti. Se il valore inserito è negativo, il sistema deve visualizzare "Valore non valido" e richiedere nuovamente l'input senza scalare munizioni (il turno viene annullato).
Consumo risorse: Per ogni attacco valido (maggiore o uguale a zero), viene sottratto 1 colpo dall'arsenale e il danno viene sottratto agli scudi nemici.
Rigenerazione scudi: Se l'attacco infligge un danno basso (minore di 5), l'incrociatore nemico ne approfitta per rigenerare il 2% dei propri scudi. Il sistema deve avvisare l'utente del recupero energetico del nemico.
Fase 3: Conclusione della missione
Il programma termina mostrando l'esito finale:
SUCCESSO: Se gli scudi nemici vengono azzerati, il messaggio sarà: "Nave nemica distrutta! Passaggio libero."
FALLIMENTO: Se le munizioni finiscono prima di aver abbattuto le difese avversarie, il messaggio sarà: "Batterie esaurite! Ritirata d'emergenza."
'''
# --- FASE 1: PREPARAZIONE AL LANCIO ---

# Validazione Carburante
carburante = -1
while carburante < 0:
    carburante = float(input("Inserisci i litri di propellente: "))
    if carburante < 0:
        print("Valore negativo non ammesso!")

print("Carburante registrato correttamente.")

# Validazione Munizioni (Arsenale)
munizioni = -1
while munizioni < 0:
    munizioni = int(input("Inserisci il numero di colpi laser (munizioni): "))
    if munizioni < 0:
        print("Errore: arsenale non valido!")

print("Sistemi d'arma pronti.\n")


# --- FASE 2: INGAGGIO TATTICO ---

scudi_nemici = 100.0

print("--- ATTENZIONE: Incrociatore nemico intercettato! ---")

# Ciclo di combattimento: continua finché il nemico ha scudi E noi abbiamo colpi
while scudi_nemici > 0 and munizioni > 0:
    print(f"[Stato: Scudi Nemici {max(0, round(scudi_nemici, 1))}% | Munizioni: {munizioni}]")

    danno = float(input("Comandante, inserisci i danni da infliggere: "))

    # 1. Protezione dai Danni Negativi
    if danno < 0:
        print("Valore non valido! Il colpo non è partito.")
        # Il 'continue' fa ripartire il ciclo dall'inizio senza eseguire le righe sotto
        continue

    # 2. Esecuzione attacco (solo se il danno era valido)
    scudi_nemici = scudi_nemici - danno
    munizioni = munizioni - 1

    # 3. Rigenerazione Scudi Nemici
    # Se il danno è scarso (< 5) e il nemico non è ancora esploso (> 0)
    if danno < 5 and scudi_nemici > 0:
        scudi_nemici = scudi_nemici + 2
        # Limite massimo degli scudi al 100%
        if scudi_nemici > 100:
            scudi_nemici = 100
        print("Attacco debole! Il nemico rigenera gli scudi (+2%).")

# --- CONCLUSIONE DELLA MISSIONE ---

print("\n--- RAPPORTO FINALE MISSIONE ---")
if scudi_nemici <= 0:
    print("Nave nemica distrutta! Passaggio libero. Ben fatto, Comandante.")
else:
    print("Batterie esaurite! Ritirata d'emergenza. La missione è fallita.")