"""
CALCOLO COSTO SPEDIZIONE
Autore: @nickname

Parametri nominati (Keyword Args) e Valori di Default
Creare funzioni flessibili che funzionano con configurazioni standard, ma che possono essere personalizzate
"""

def calcola_spedizione(peso_pacco, destinazione="Italia", urgente=False):
    """
    Calcola il costo totale di una spedizione.
    
    I parametri 'destinazione' e 'urgente' hanno valori di default.
    Se chi chiama la funzione non li fornisce, Python userà questi.
    """
    # Costo base: 1 euro al kg
    costo = peso_pacco * 1.0

    # Controllo destinazione
    if destinazione.strip().lower() != "italia":
        costo += 10.0

    # Controllo urgenza
    if urgente:
        costo *= 2

    return costo

def mostra_menu():
    """Mostra le opzioni del programma"""
    print("\n-- Preventivo Spedizioni --")
    print("Scegli un'opzione:")
    print("1. Calcola una nuova spedizione")
    print("q. Esci dal programma")

def avvia_programma():
    """Funzione principale per la gestione dell'input utente"""
    while True:
        mostra_menu()
        scelta = input("Seleziona un'opzione: ").strip().lower()

        if scelta == 'q':
            print("\nGrazie per aver usato il nostro servizio. Arrivederci!")
            break

        if scelta == '1':
            # 1. Gestione del peso (Obbligatorio)
            peso = float(input("Inserisci il peso del pacco (in kg): "))
            if peso <= 0:
                print("Il peso deve essere maggiore di zero!")
                continue

            # 2. Gestione destinazione (Opzionale per l'utente)
            dest = input("Inserisci la destinazione (Premi Invio per la nazione standard): ").strip()

            # 3. Gestione urgenza (Opzionale per l'utente)
            scelta_urgenza = input("La spedizione è urgente? (s/n): ").strip().lower()
            is_urgente = (scelta_urgenza == 's')

            # --- APPLICAZIONE DEI DEFAULT E KEYWORD ARGS ---
            
            if dest == "" and not is_urgente:
                # CASO 1: L'utente vuole tutto standard.
                # Passiamo SOLO il parametro obbligatorio.
                # Python applicherà da solo destinazione="Italia" e urgente=False.
                costo_finale = calcola_spedizione(peso)

            elif dest == "":
                # CASO 2: L'utente omette la destinazione, ma ha chiesto l'urgenza.
                # Usiamo il Keyword Arg (urgente=is_urgente) per "saltare" la destinazione.
                # Python userà la destinazione di default.
                costo_finale = calcola_spedizione(peso, urgente=is_urgente)

            else:
                # CASO 3: L'utente ha inserito una destinazione specifica.
                # Usiamo i Keyword Args per passare tutto in modo esplicito e leggibile. L'uso dei parametri nominati (peso_pacco=peso, destinazione=dest...) rende immediato capire quale valore stiamo assegnando a quale variabile.
                costo_finale = calcola_spedizione(peso_pacco=peso, destinazione=dest, urgente=is_urgente)

            # Output dei dettagli del preventivo
            # Se 'dest' è vuota, mostriamo a schermo che è scattato il default
            dest_display = "Italia (Default)" if dest == "" else dest
            
            print("\n--- Riepilogo Preventivo ---")
            print(f"Dati: {peso} kg | Destinazione: {dest_display} | Urgente: {'Sì' if is_urgente else 'No'}")
            print(f"Costo totale: {costo_finale:.2f} €")
            print("----------------------------")
        else:
            print("Opzione non valida!")

# Avvio effettivo del programma
if __name__ == "__main__":
    avvia_programma()
