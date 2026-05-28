# Unità 5: Gestione strutture dati

In questa cartella si impara a gestire non più un singolo dato, ma insiemi complessi di informazioni.

* Liste

* Tuple

* Dizionari

---

## Testi degli Esercizi e Soluzioni

### 0. Prova Stringhe
Script introduttivo per sperimentare con le varie strutture

* **Codice sorgente:** [Vedi la soluzione](./prova_strutture_dati.py)

---
### 1. Lista Cose da Fare (liste)
Obiettivo
Progettare e sviluppare un'applicazione a riga di comando (CLI) in Python che permetta all'utente di gestire una lista di impegni giornalieri. L'obiettivo principale è combinare l'uso delle liste e delle funzioni, strutturando il codice in modo modulare, pulito e riutilizzabile.

Requisiti del Programma
L'applicazione deve essere suddivisa in funzioni specifiche, ognuna con un singolo compito:

mostra_lista(lista_task): Riceve come parametro la lista degli impegni. Se la lista è vuota, stampa un messaggio di complimenti. Se contiene elementi, li stampa uno per uno sotto forma di elenco puntato.

aggiungi_impegno(lista_task, nuovo_impegno): Riceve la lista e una stringa, aggiungendo il nuovo impegno in coda alla lista.

completa_impegno(lista_task, impegno_fatto): Riceve la lista e il nome dell'impegno da rimuovere. Deve verificare se l'elemento esiste prima di eliminarlo, per evitare il blocco del programma.

mostra_menu(): Stampa a schermo le opzioni disponibili per l'utente (1. Mostra, 2. Aggiungi, 3. Rimuovi, 4. Esci).

app_to_to_list(): La funzione principale che inizializza una lista con alcuni impegni predefiniti, avvia un ciclo continuo (while) per mostrare il menu, raccoglie l'input dell'utente ed esegue l'azione corretta in base alla scelta.

* **Codice sorgente:** [Vedi la soluzione](./prova_strutture_dati.py)


---

### 2. Diario di bordo navele (tuple)

Obiettivo
Sviluppare un sistema software navale per mappare le tappe di un viaggio in nave. L'obiettivo dell'esercizio è padroneggiare l'uso di tuple annidate per proteggere dati sensibili e immutabili (come le coordinate GPS) all'interno di una struttura dati dinamica e mutabile (la rotta espressa come lista).

Requisiti del Programma
Ogni funzione implementata deve possedere una Docstring formattata con le sezioni Args e Returns.

mostra_rotta(diario_bordo): Riceve la lista dei viaggi. Estrae da ogni record il nome della tappa, la sotto-tupla delle coordinate e lo stato. Stampa i dati formattando la latitudine e la longitudine.

aggiungi_tappa(diario_bordo, nome_porto, lat, lon): Prende i dati della posizione, impacchetta latitudine e longitudine in una tupla autonoma, unisce questa tupla al nome del porto e allo stato predefinito "Pianificata", inserendo il tutto nella lista.

naviga_a_tappa(diario_bordo, nome_porto): Cerca il porto all'interno della lista. Poiché la tupla della tappa non può essere modificata direttamente (le tuple sono immutabili), la funzione deve generare una nuova tupla aggiornata e sostituirla nella lista all'indice corrispondente.

mostra_menu(): Gestisce l'interfaccia grafica dei comandi a disposizione del capitano.

app_dirario_viaggio_nave(): Avvia la simulazione di bordo pre-caricando due tappe storiche e attivando il ciclo di controllo dell'imbarcazione.

* **Codice sorgente:** [Vedi la soluzione](./diario_viaggio_nave.py)


---

### 3. Rubrica telefonica (dizionari)

Obiettivo
Progettare e sviluppare un'applicazione a riga di comando (CLI) in Python per la gestione di una rubrica di contatti telefonici. L'obiettivo principale è comprendere la struttura delle coppie chiave-valore dei dizionari e imparare a manipolarle in sicurezza all'interno delle funzioni.

Requisiti del Programma
Il codice deve essere strutturato in funzioni autonome. Ogni funzione deve includere una Docstring che specifichi chiaramente gli argomenti accettati (Args) e il valore restituito (Returns).

mostra_rubrica(rubrica): Riceve il dizionario dei contatti. Se la rubrica è vuota, avvisa l'utente. Se contiene dati, mostra l'elenco completo dei contatti (Nome e Numero) sfruttando il metodo .items().

aggiungi_o_aggiorna_contatto(rubrica, nome, numero): Riceve il dizionario, una chiave (nome) e un valore (numero). Aggiunge il contatto se non esiste, oppure sovrascrive il numero se il nome è già presente.

cerca_contatto(rubrica, nome): Riceve il dizionario e il nome da cercare. Verifica la presenza della chiave prima di accedere al valore, mostrando il numero di telefono se trovato o un messaggio di errore se assente.

mostra_menu(): Stampa a schermo le opzioni disponibili (1. Mostra, 2. Aggiungi/Modifica, 3. Cerca, 4. Esci).

app_rubrica(): La funzione principale che inizializza la rubrica con alcuni contatti predefiniti, gestisce il ciclo continuo dell'applicazione (while), raccoglie gli input e invoca le funzioni corrette.

* **Codice sorgente:** [Vedi la soluzione](./rubrica_telefonica.py)

