# Unità 4: Funzioni

In questa cartella sono raccolti gli esercizi dedicati all'introduzione e all'utilizzo delle funzioni in Python. Gli script mostrano come modularizzare il codice, definire blocchi riutilizzabili con il costrutto def, gestire i parametri e restituire risultati tramite il valore di ritorno (return).

---

## Testi degli Esercizi e Soluzioni

### 1. Calcolatrice
Sviluppare un programma che implementi una calcolatrice modulare. Il codice deve definire funzioni separate per le operazioni aritmetiche di base (somma, sottrazione, moltiplicazione e divisione). Il programma principale deve richiedere all'utente i due numeri e l'operazione desiderata, invocando la funzione corretta e gestendo in modo sicuro l'eventuale divisione per zero.

* **Codice sorgente:** [Vedi la soluzione](./calcolatrice.py)

---
### 2. Simulatore Bancomat
Creare una simulazione di uno sportello bancomat organizzando le diverse operazioni disponibili all'interno di funzioni dedicate (es. controllo del saldo, versamento e prelievo). Il programma deve presentare un menu di scelta continuo e invocare la funzione corrispondente all'azione richiesta dall'utente, modificando e restituendo il saldo aggiornato.

* **Codice sorgente:** [Vedi la soluzione](./simulatore_bancomat.py)


---
### 3. Simulatore Dadi
Sviluppare un programma per la simulazione del lancio di dadi da gioco. La logica di generazione del numero casuale (da 1 a 6) deve essere incapsulata all'interno di una funzione. Il sistema può essere strutturato per richiedere all'utente quanti dadi lanciare o se ripetere il lancio, mostrando i singoli risultati e il totale complessivo.

* **Codice sorgente:** [Vedi la soluzione](./simulatore_dadi.py)

---

### 4. Sasso Carta Forbice
Realizzare il classico gioco "Sasso, Carta, Forbice" contro il computer, strutturando la logica tramite l'uso delle funzioni. È richiesto di isolare in funzioni distinte le responsabilità del programma, come ad esempio la generazione della mossa casuale della CPU e la funzione di controllo per decretare il vincitore del turno.

* **Codice sorgente:** [Vedi la soluzione](./sasso_carta_forbice.py)

---
### 5. Convertitore Valuta
Scrivi una funzione chiamata converti_euro_in_dollari che riceve come parametro un importo in euro e restituisce (tramite return) l'importo convertito in dollari (usa un tasso di cambio fisso, es. 1.08). Il programma principale deve chiedere l'importo all'utente, invocare la funzione e solo alla fine stampare a schermo il risultato.

* **Codice sorgente:** [Vedi la soluzione](./converti_valuta.py)

---

### 6. calcolatore_spedizione.py
Crea una funzione chiamata calcola_spedizione che accetta tre parametri: peso_pacco, destinazione (stringa) e urgente (booleano). Imposta i valori di default in modo che la destinazione standard sia "Italia" e urgente sia False. La funzione deve calcolare il costo base in base al peso (es. 1 euro al kg). Se la destinazione non è "Italia", aggiungi 10 euro. Se urgente è True, raddoppia il costo totale.

* **Codice sorgente:** [Vedi la soluzione](./calcolatore_spedizione.py)

---
### 7. gioco_punteggio.py
Definisci una variabile globale chiamata punteggio e impostala a 0. Crea una funzione chiamata aggiungi_punti che riceve un parametro numerico e tenta di sommarlo al punteggio. Crea una seconda funzione chiamata azzera_punteggio. Mostra come le variabili definite dentro le funzioni siano isolate rispetto all'esterno.

* **Codice sorgente:** [Vedi la soluzione](./gioco_punteggio.py)


---
### 8. validatore_profilo.py
Testo: Crea un sistema di validazione per la registrazione di un utente composto da tre funzioni distinte:

valida_username(username): restituisce True se l'username è lungo almeno 5 caratteri.

valida_password(password): restituisce True se la password contiene almeno un numero.

crea_profilo(username, password): questa funzione deve invocare le due funzioni precedenti. Se entrambe sono valide, stampa "Profilo creato con successo", altrimenti stampa "Dati non validi".

* **Codice sorgente:** [Vedi la soluzione](./validatore_profilo.py)
