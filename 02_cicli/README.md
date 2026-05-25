# Unità 2: Cicli e Strutture Iterative

In questa cartella sono raccolti gli esercizi dedicati alle strutture iterative in Python. Gli esercizi mostrano come gestire ripetizioni di blocchi di codice sia quando il numero di iterazioni non è noto a priori (ciclo `while`), sia quando è predefinito (ciclo `for`).

---

## Testi degli Esercizi e Soluzioni

### Cicli Indefiniti (Costrutto while)

### 1. Registra KM
Un programma per un allenamento di corsa. L'utente deve inserire quanti km ha corso. Se inserisce un numero negativo (impossibile), il programma continua a chiederglielo finché non inserisce un numero positivo.

* **Codice sorgente:** [Vedi la soluzione](./registra_km.py)

---

### 2. Vasca
Vogliamo riempire una vasca da bagno che ha una capienza massima di 50 litri. L'utente aggiunge secchi d'acqua (di quanti litri vuole) finché la vasca non è piena o trabocca.

* **Codice sorgente:** [Vedi la soluzione](./vasca.py)

---

### 3. Distributore Caffè
Un distributore automatico ha una capacità massima di 50 caffè. I clienti arrivano uno alla volta e inseriscono il numero di caffè che desiderano acquistare. Ogni caffè costa 0,60 €.

* **Codice sorgente:** [Vedi la soluzione](./distributore_caffe.py)

---

### 4. Distributore Caffè Premium
Un distributore automatico ha una capacità massima di 50 caffè. I clienti arrivano uno alla volta e inseriscono il numero di caffè che desiderano acquistare, scegliendo tra Caffè Standard (0,60 €) o Caffè Premium (1,00 €).

* **Codice sorgente:** [Vedi la soluzione](./distributore_caffe_premium.py)

---

### 5. Bancomat Gratis
Un utente può prelevare denaro da un bancomat virtuale, ma non può superare il saldo disponibile. Il conto parte con un saldo di 200 €. Il ciclo continua finché il saldo si azzera. Se il saldo è sufficiente, il prelievo viene effettuato e il saldo aggiornato viene mostrato. Se il saldo è insufficiente, il sistema avvisa l'utente e chiede un nuovo importo.

* **Codice sorgente:** [Vedi la soluzione](./bancomat_gratis.py)

---

### 6. Pesa Sacchi Noccioline
Una ditta produce sacchetti di noccioline, confezionate con una macchina automatica. La tolleranza di peso ammessa è data tra i 40 e 50 grammi. Sviluppare un programma che visualizza quanti sono i sacchetti il cui peso rientra nella tolleranza ammessa e i sacchetti totali pesati. Il peso viene dato in input, l’inserimento termina quando l’utente comunica che non ci sono più sacchetti da pesare inserendo il valore 0.

* **Codice sorgente:** [Vedi la soluzione](./pesa_sacchi_noccioline.py)

---

### 7. Cassa Cinema
Sviluppare un software per la gestione automatizzata delle prenotazioni di una sala cinematografica con una capienza massima di 20 posti. Il sistema deve operare attraverso un ciclo principale di vendita che consenta acquisti multipli fino all'esaurimento della disponibilità o alla chiusura manuale del servizio.

Per ogni transazione, l'utente specificherà il numero di biglietti desiderati, attivando una validazione dei dati: in caso di richiesta superiore ai posti disponibili, il software dovrà segnalare l'insufficienza e indicare il residuo esatto; qualora venisse inserito un valore nullo o negativo, il sistema dovrà notificare l'errore e richiedere nuovamente l'inserimento. È prevista inoltre una funzione di chiusura forzata dedicata all'operatore, il quale può interrompere il ciclo in qualsiasi momento inserendo il codice speciale -1. Al termine della sessione il programma deve generare un riepilogo delle statistiche finali (totale biglietti venduti e posti rimasti vacanti).

* **Codice sorgente:** [Vedi la soluzione](./cassa_cinema.py)

---

### 8. Target Risparmio
Sviluppare un'applicazione che funga da assistente al risparmio personalizzato. Il software deve inizialmente permettere all'utente di definire un traguardo economico (target). Una volta stabilito, il programma richiederà di inserire l'importo dei singoli versamenti quotidiani.

Se viene inserito un valore negativo, l'operazione deve essere annullata con un messaggio d'errore ("Non puoi prelevare, solo depositare!"). Dopo ogni deposito valido, il programma deve visualizzare il totale accumulato e la cifra esatta ancora mancante. Il processo si conclude quando la somma versata raggiunge o supera la soglia prefissata, mostrando un messaggio di congratulazioni e l'eventuale eccedenza (avanzo).

* **Codice sorgente:** [Vedi la soluzione](./target_risparmio.py)

---

### 9. Sistema Bancomat Accesso Base
Sviluppare il modulo di autenticazione per uno sportello automatico. Il sistema deve richiedere all'utente di inserire un PIN numerico segreto e continuare a chiederlo ciclicamente finché non viene inserito quello corretto. Solo dopo il login effettuato con successo, l'utente viene accolto da un messaggio di conferma e può inserire la cifra che desidera prelevare. L'operazione si conclude visualizzando l'importo appena erogato.

* **Codice sorgente:** [Vedi la soluzione](./sistema_bancomat_accesso_base.py)

---

### 10. Sistema Bancomat Accesso Intermedio
Progettare un software per un bancomat che includa controlli di sicurezza sui tentativi di accesso e verifichi la disponibilità dei fondi prima di autorizzare un'operazione. Il sistema di login offre un massimo di 3 tentativi (comunicando ogni volta quanti ne rimangono); al terzo fallimento la carta viene "bloccata" e l'esecuzione termina. Se l'accesso va a buon fine, il sistema verifica che l'importo richiesto non superi il saldo disponibile (es. 500€). In caso di successo eroga il denaro e mostra il saldo rimanente, altrimenti avvisa della mancanza di fondi.

* **Codice sorgente:** [Vedi la soluzione](./sistema_bancomat_accesso_intermedio.py)

---

### 11. Sistema Bancomat Accesso Avanzato
Creare un simulatore di sportello bancario avanzato che permetta a un utente, dopo essersi autenticato (max 3 tentativi), di effettuare operazioni multiple di prelievo in una singola sessione senza reinserire il PIN. Il ciclo di prelievo si interrompe quando l'utente digita il valore 0.

Il programma deve convalidare che non si inseriscano importi negativi o superiori al saldo e deve accumulare tutto il denaro erogato. Al termine della sessione, viene generato un riepilogo finale con il totale prelevato complessivamente e il saldo finale rimasto sul conto corrente (senza l'uso di liste).

* **Codice sorgente:** [Vedi la soluzione](./sistema_bancomat_accesso_avanzato.py)

---

### Cicli Definiti (Costrutto for)

### 12. Scrivo Scrivo Scrivo
Scrivere un programma che chiede all’utente di inserire un numero maggiore o uguale a zero e stampa il messaggio “sto ciclando” un numero di volte pari al numero inserito. Se il valore inserito è negativo, il programma stampa un messaggio di errore.

* **Codice sorgente:** [Vedi la soluzione](./scrivo_scrivo_scrivo.py)

---

### 13. Cinema For
Un cinema vuole calcolare gli incassi della giornata. Scrivi un programma che chieda quanti spettacoli ci sono stati oggi. Per ogni spettacolo, chieda quanti biglietti sono stati venduti e il prezzo di ogni biglietto. Calcoli e stampi l'incasso totale della giornata.

* **Codice sorgente:** [Vedi la soluzione](./cinema_for.py)

---

### 14. Media Voti
In una scuola, si vuole scrivere un programma per calcolare la media dei voti di comportamento di una classe. Dopo aver inserito il numero di studenti della classe, il programma deve calcolare e mostrare la media di tali voti.

* **Codice sorgente:** [Vedi la soluzione](./media_voti.py)

---

### 15. Meteo
Un servizio meteo vuole analizzare le precipitazioni degli ultimi 7 giorni. Scrivi un programma che chieda all’utente di inserire la precipitazione giornaliera per 7 giorni, calcoli la precipitazione media della settimana e riporti qual è stata la precipitazione massima e quale la minima.

* **Codice sorgente:** [Vedi la soluzione](./meteo.py)

---

