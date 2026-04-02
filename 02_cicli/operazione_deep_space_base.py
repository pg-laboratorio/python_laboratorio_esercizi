'''
In questo scenario tattico, assumi il comando di un incrociatore stellare impegnato in un duello ravvicinato. L'obiettivo primario è la neutralizzazione di una nave nemica che si presenta con gli scudi energetici al 100% della loro potenza. L'intero scontro si articola attorno ad un ciclo operativo continuo,  finché gli scudi nemici hanno energia, l'incrociatore rimane in assetto di combattimento.

Durante ogni fase del ciclo, il sistema d'arma richiede l'intervento dell'utente per definire l'intensità del colpo laser da sferrare. Una volta stabilito il valore del danno, questo viene sottratto direttamente dal totale della protezione nemica. Per garantire la consapevolezza tattica, il computer di bordo stampa immediatamente dopo ogni colpo la potenza residua degli scudi, permettendo di monitorare l'efficacia dell'attacco in tempo reale. Il processo si interrompe non appena la resistenza nemica viene azzerata e comunica ufficialmente la distruzione della nave nemica.
'''
scudi_nemici = 100 # Impostazione risorsa iniziale

while scudi_nemici > 0: # Ciclo finché la risorsa è disponibile
    danno = int(input("Inserisci potenza del colpo: "))
    scudi_nemici = scudi_nemici - danno # Decremento progressivo

    if scudi_nemici > 0:
        print(f"Scudi rimanenti: {scudi_nemici}%")
    else:
        print("Scudi al 0%")

print("Nave nemica distrutta!") # Messaggio di fine ciclo