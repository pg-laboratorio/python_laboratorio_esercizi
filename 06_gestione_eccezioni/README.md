# Unità 6: Gestione delle Eccezioni

In questa cartella sono raccolti gli esercizi dedicati alla gestione delle eccezioni in Python. Gli script mostrano come rendere i programmi robusti agli errori, intercettare situazioni impreviste durante l'esecuzione e comunicare messaggi chiari all'utente, utilizzando i blocchi `try`, `except`, `else`, `finally` e la parola chiave `raise`.

---

## Testi degli Esercizi e Soluzioni

---

### 1. Divisione Sicura
Completa una funzione in modo che non vada in crash quando il divisore è zero. Usa `try/except` per gestire l'errore e restituisci `None` in quel caso.

* Codice sorgente: [Vedi la soluzione](https://github.com/pg-laboratorio/python_laboratorio_esercizi/blob/main/06_gestione_eccezioni/divisione_sicura.py)

---

### 2. Conversione con Protezione
Scrivi una funzione `converti_intero(s)` che converta una stringa in numero intero. Se la stringa non è un numero valido, stampa un messaggio di errore e restituisce `0`.

* Codice sorgente: [Vedi la soluzione](https://github.com/pg-laboratorio/python_laboratorio_esercizi/blob/main/06_gestione_eccezioni/conversione_protetta.py)

---

### 3. Accesso Sicuro a una Lista
Scrivi una funzione `elemento(lista, indice)` che restituisce l'elemento alla posizione indicata. Se l'indice non esiste, restituisce la stringa `"indice non valido"`.

* Codice sorgente: [Vedi la soluzione](https://github.com/pg-laboratorio/python_laboratorio_esercizi/blob/main/06_gestione_eccezioni/accesso_lista.py)

---

### 4. Più Eccezioni Insieme
Scrivi una funzione `calcola(a, b)` che restituisce `a / b`. Gestisci sia il caso in cui `a` o `b` non siano numeri, sia il caso in cui `b` sia zero, con messaggi di errore distinti.

* Codice sorgente: [Vedi la soluzione](https://github.com/pg-laboratorio/python_laboratorio_esercizi/blob/main/06_gestione_eccezioni/piu_eccezioni.py)

---

### 5. Lettura da Dizionario
Hai un dizionario di voti. Scrivi una funzione `voto_studente(dizionario, nome)` che restituisce il voto dello studente. Se il nome non esiste, gestisci l'eccezione e restituisce `"studente non trovato"`.

* Codice sorgente: [Vedi la soluzione](https://github.com/pg-laboratorio/python_laboratorio_esercizi/blob/main/06_gestione_eccezioni/lettura_dizionario.py)


## Concetti Chiave

| Parola chiave | Descrizione |
|---|---|
| `try` | Blocco con il codice "rischioso" da eseguire |
| `except` | Cosa fare se si verifica un determinato errore |
| `else` | Eseguito solo se il blocco `try` non ha sollevato errori |
| `finally` | Eseguito sempre, con o senza errore |

### Eccezioni più comuni

| Eccezione | Quando si verifica |
|---|---|
| `ZeroDivisionError` | Divisione per zero |
| `ValueError` | Valore di tipo giusto ma contenuto non valido (es. `int("ciao")`) |
| `TypeError` | Operazione su un tipo non compatibile |
| `IndexError` | Indice fuori dai limiti di una lista o tupla |
| `KeyError` | Chiave non presente in un dizionario |
| `FileNotFoundError` | File o percorso inesistente |
