# Unità 1: Introduzione e Condizioni

In questa cartella sono raccolti gli esercizi dedicati ai concetti fondamentali di Python: l'uso delle variabili, l'input/output da terminale e la gestione del flusso del programma tramite i costrutti condizionali (`if`, `elif`, `else`).

Gli esercizi sono in ordine di difficoltà crescente: ognuno aggiunge un solo concetto nuovo rispetto al precedente.

**Come usare i casi di prova:** dopo aver scritto il programma, eseguilo con gli input della tabella e controlla che l'output coincida. Se non coincide, c'è un errore da trovare! Le righe segnate con ⚠️ sono *casi limite*: valori "al confine" dove si nascondono gli errori più frequenti.

> Per ora supponiamo che l'utente inserisca sempre numeri validi. Nell'Unità 6 (Gestione delle eccezioni) vedremo come proteggere il programma da input sbagliati, come `ciao` al posto di un numero.

---

## Testi degli Esercizi e Soluzioni

### 1. Biglietteria Museo
*Concetti: variabili, costanti, `input()`, conversione con `int()`, `print()` con f-string*

Il sistema gestionale del museo d'arte contemporanea della nostra città ha bisogno di aiuto. Gli serve un programma che, dato il numero di persone del gruppo che svolge la visita, calcoli in automatico il prezzo complessivo. Considera che il prezzo di un biglietto è un fisso di 10€.

| Input (persone) | Output atteso |
|---|---|
| 4 | 40 € |
| 1 | 10 € |

* **Codice sorgente:** [Vedi la soluzione](./biglietteria_museo.py)

---

### 2. Accesso al Sistema
*Concetti: prima condizione `if` / `else`, operatori di confronto*

Un amministratore di sistema sta configurando un accesso sicuro. Solo gli utenti con un livello di sicurezza superiore a 5 possono accedere al server critico. Il programma chiede il livello dell'utente e decide se concedere l'accesso.

| Input (livello) | Output atteso |
|---|---|
| 8 | Accesso consentito |
| 6 | Accesso consentito |
| ⚠️ 5 | Accesso negato ("superiore a 5" esclude il 5) |

* **Codice sorgente:** [Vedi la soluzione](./accesso_sistema.py)

---

### 3. Biglietteria Parcheggio
*Concetti: `if` / `else` con calcoli diversi nei due rami*

Sapendo che in un parcheggio la prima ora costa 2.50 € mentre tutte le successive costano 1.50 €, scrivere un programma che richieda in input il numero complessivo delle ore e visualizzi il totale da pagare.

| Input (ore) | Output atteso |
|---|---|
| 3 | 5.50 € |
| ⚠️ 1 | 2.50 € |
| ⚠️ 0 | 2.50 € (si paga comunque la prima ora) |

* **Codice sorgente:** [Vedi la soluzione](./biglietteria_parcheggio.py)

---

### 4. Sistema di Ventilazione
*Concetti: numeri decimali con `float()`, calcolo della media, precedenza degli operatori*

Il sistema di ventilazione di un edificio si accende quando la media dei valori di areazione, registrati in tre diverse stanze, è inferiore a un valore fissato. Implementa un programma che consenta di fissare un limite minimo, ricevere in input i dati delle tre stanze, calcolare la media e segnalare se il sistema verrà acceso o meno.
*Esempio valore areazione: 0,5-6 [vol/h]*

| Limite | Stanze | Output atteso |
|---|---|---|
| 2 | 1, 1, 1 | media 1.00 → Sistema acceso |
| 2 | 3, 4, 5 | media 4.00 → Sistema spento |
| ⚠️ 2 | 1, 2, 3 | media 2.00 → Sistema spento (la media non è *inferiore* al limite) |

* **Codice sorgente:** [Vedi la soluzione](./sistema_ventilazione.py)

---

### 5. Calcolo Sconti
*Concetti: `if` / `elif` / `else`, importanza dell'ordine delle condizioni*

Un negozio applica uno sconto in base all'importo totale di un acquisto. Se l'importo è superiore a 200 €, viene applicato uno sconto del 15%. Se l'importo è superiore a 100 €, lo sconto è del 10%. Scrivi un programma che richieda in input l'importo totale, calcoli lo sconto applicabile e visualizzi l'importo finale da pagare.

| Input (importo) | Output atteso |
|---|---|
| 80 | 80.00 € (nessuno sconto) |
| 150 | 135.00 € (sconto 10%) |
| 250 | 212.50 € (sconto 15%) |
| ⚠️ 100 | 100.00 € (nessuno sconto) |
| ⚠️ 200 | 180.00 € (sconto 10%, non 15%) |

* **Codice sorgente:** [Vedi la soluzione](./calcolo_sconti.py)

---

### 6. Il Triangolo
*Concetti: operatore logico `and`, condizioni composte*

Dati tre bastoncini, è possibile formare un triangolo solo se ogni lato è minore della somma degli altri due. Scrivi un programma che riceva tre lunghezze e determini se è possibile costruire un triangolo, stampando "Sì" o "No".

| Input (lati) | Output atteso |
|---|---|
| 3, 4, 5 | Sì |
| 1, 1, 5 | No |
| ⚠️ 1, 2, 3 | No (i bastoncini si "appiattiscono" su una linea) |

* **Codice sorgente:** [Vedi la soluzione](./il_triangolo.py)

---

### 7. Costo Energetico (Riscaldamento)
*Concetti: `if` annidati, costanti multiple, differenza tra `<` e `<=`*

Un sistema di riscaldamento si attiva quando la temperatura media di tre stanze è inferiore a un valore impostato. Il costo energetico è di 20 € all'ora. Se la temperatura media è inferiore di almeno 5°C rispetto al limite, il costo orario aumenta del 25% (extra consumo). Implementa un programma che calcoli il costo totale basandosi su temperature, limite e ore di funzionamento.

| Limite | Stanze | Ore | Output atteso |
|---|---|---|---|
| 20 | 18, 18, 18 | 3 | 60.00 € |
| 20 | 14, 14, 14 | 3 | 75.00 € (extra consumo) |
| 20 | 21, 21, 21 | 3 | Riscaldamento spento, 0.00 € |
| ⚠️ 20 | 15, 15, 15 | 3 | 75.00 € ("almeno 5°C" include il 5) |

* **Codice sorgente:** [Vedi la soluzione](./costo_energetico.py)
