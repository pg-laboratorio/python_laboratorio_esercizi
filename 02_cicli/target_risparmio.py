'''
CONSEGNA
L'obiettivo è sviluppare un'applicazione che funga da assistente al risparmio personalizzato.
Il software deve inizialmente permettere all'utente di definire un traguardo economico (ad esempio, il costo di un nuovo computer).
Una volta stabilito il target, il programma entrerà in un ciclo iterativo in cui richiederà all'utente di inserire l'importo dei singoli versamenti quotidiani. Per garantire l'integrità dei dati, il sistema deve implementare una validazione: se viene inserito un valore negativo, l'operazione deve essere annullata con un messaggio d'errore ("Non puoi prelevare, solo depositare!"). Dopo ogni deposito valido, il programma deve fornire un feedback immediato, visualizzando il totale accumulato e la cifra esatta ancora mancante per completare l'obiettivo. Il processo si conclude solo quando la somma versata raggiunge o supera la soglia prefissata; in quel momento, il programma mostrerà un messaggio di congratulazioni, indicando anche l'eventuale eccedenza (avanzo) rispetto al traguardo iniziale.

PROGETTO:
Obiettivo: Creare un programma che aiuti l'utente a risparmiare una somma specifica per un obiettivo (es. un nuovo computer), accumulando versamenti finché il target non viene raggiunto.
Requisiti:Impostazione Obiettivo: All'inizio, l'utente inserisce la cifra totale che vuole risparmiare (es. 500€).Ciclo di Versamento: Il programma chiede ripetutamente all'utente quanto vuole depositare oggi.Validazione: * Se l'utente inserisce una cifra negativa, il programma deve mostrare un errore ("Non puoi prelevare, solo depositare!") e non aggiungere nulla al totale.Aggiornamento in tempo reale: Dopo ogni deposito valido, il programma deve dire:
Quanto è stato risparmiato finora.
Quanto manca esattamente per raggiungere l'obiettivo.
Conclusione: Il ciclo termina quando la somma accumulata è uguale o superiore all'obiettivo iniziale. A quel punto, il programma deve congratularsi e mostrare l'eventuale "avanzo" rispetto al target.



DATI INPUT

- importo del budget (importo_budget)
- importo del versamento (importo_versamento)

DATI OUTPUT

- importo totale (importo_totale)
- importo mancante per raggiungere il budget (importo_mancante_budget)

PROCEDIMENTO

- chidiamo in input l'importo del budget (importo_budget)
- settiamo importo_versamento = 0


- avviamo il ciclo while importo_versamento < importo_budget
- chiediamo in input l'importo del versamento

- se l'importo del versamento < 0
    - stampiamo (Versamento annullato! Inserire un importo positivo)
    break

- altrimenti
    - l'importo mancante = l'importo del budget - l'importo totale
    - stampiamo l'importo mancante

'''

importo_budget = float(input("Inserisci il budget da raggiungere: "))
importo_versamento = 0
importo_totale = 0


while importo_totale < importo_budget:
    importo_versamento = float(input("Inserire l'importo del versamento: "))

    if importo_versamento < 0:
        print("Versamento annullato! Non puoi prelevare, solo versare")
        continue

    importo_totale += importo_versamento
    importo_mancante = importo_budget - importo_totale

    if importo_totale < importo_budget:
        print(f"L'importo mancante è: {importo_mancante:.2f} ")

    else:
        importo_eccedente = importo_totale - importo_budget
        print(f"Complimenti, hai raggiunto il budget! L'importo eccedente è: {importo_eccedente:.2f} ")


    print(f"L'importo totale: {importo_totale:.2f} ")

print("Grazie per aver utilizzato il nostro servizio!")









