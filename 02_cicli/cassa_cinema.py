'''
CONSEGNA:
    L'obiettivo del programma è quello di sviluppare un software per la gestione automatizzata delle prenotazioni di una sala cinematografica con una capienza massima di 20 posti. Il sistema deve operare attraverso un ciclo principale di vendita che consenta acquisti multipli fino all'esaurimento della disponibilità o alla chiusura manuale del servizio. Per ogni transazione, l'utente specificherà il numero di biglietti desiderati, attivando una validazione dei dati: in caso di richiesta superiore ai posti disponibili, il software dovrà segnalare l'insufficienza e indicare il residuo esatto; qualora venisse inserito un valore nullo o negativo, il sistema dovrà notificare l'errore e richiedere nuovamente l'inserimento.
    È prevista inoltre una funzione di chiusura forzata dedicata all'operatore, il quale può interrompere il ciclo in qualsiasi momento inserendo il codice speciale -1, simulando così la chiusura immediata della cassa. Al termine della sessione — sia essa avvenuta per esaurimento posti o per intervento manuale — il programma deve generare un riepilogo delle statistiche finali, comunicando il totale dei biglietti venduti e il numero di posti rimasti vacanti.
DATI:
    INPUT:
        posti richiesti (posti_richiesti)
    OUTPUT:
        statistica finale (posti_venduti) (posti_rimasti)
    ALTRI:
        posti rimasti(posti_rimasti)
        posti venduti(posti_venduti)
PROGETTO:
    Obiettivo:
        Gestire le prenotazioni per una sala cinematografica con posti limitati, permettendo più acquisti finché la sala non è piena o l'operatore decide di chiudere la cassa.
    Requisiti:
        Capienza:
            La sala ha 20 posti totali.
        Ciclo Principale:
            Il programma deve continuare a vendere biglietti finché ci sono posti disponibili.
        Input Utente:
            L'utente inserisce quanti biglietti vuole comprare.Validazione:
            Se l'utente chiede più biglietti di quelli rimasti, il programma deve dire "Posti insufficienti" e mostrare quanti ne restano.
            Se l'utente inserisce un numero negativo o zero, deve segnalare l'errore e richiedere l'input .
        Chiusura Forzata:
            Se l'operatore inserisce un codice segreto (es. -1), il ciclo si interrompe immediatamente anche se ci sono ancora posti (simulando la chiusura della cassa).Statistiche Finali: Alla fine, mostra il totale dei biglietti venduti e quanti posti sono rimasti vuoti
'''
#settar variabili iniziali
posti_rimasti=20
posti_venduti=0
#ciclo while per sapere se abbiamo ancora i posti
while posti_rimasti > 0:
    #richiedere input
    posti_richiesti=int(input("quanti posti voui acquistare?"))
    #condizione per codice segreto; codice segreto =-1
    if posti_richiesti == -1:
        print (f"Cassa chiusa; sono stati venduti {posti_venduti} e sono rimasti {posti_rimasti}")
        #interuzione
        break
    elif posti_richiesti <= 0:
        print ("Non inserir valori invalidi")
        continue
    elif posti_richiesti > posti_rimasti:
        print ("Non richiedere di un valore eccesivo")
        continue
    else:
        #calcoli
        posti_venduti= posti_venduti + posti_richiesti
        posti_rimasti= posti_rimasti - posti_richiesti
        #output
        print (f"Aqcuisto effetuato; sono rimasti {posti_rimasti}")





