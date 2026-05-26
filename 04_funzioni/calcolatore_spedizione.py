"""
CALCOLO COSTO SPEDIZIONE
Autore: @nickname

Parametri nominati (Keyword Args) e Valori di Default
Creare funzioni flessibili che funzionano con configurazioni standard, ma che possono essere personalizzate
"""

def calcola_spedizione(peso_pacco, destinazione="Italia", urgente=False):
    """
    Calcola il costo totale di una spedizione in base al peso,
    alla destinazione e alla priorità.

    args:
    - peso_pacco (float): il peso del pacco in kg
    - destinazione (str): la nazione di destinazione (default: "Italia")
    - urgente (bool): flag per spedizione urgente (default: False)

    return:
    - float: il costo totale della spedizione in euro
    """
    # Costo base: 1 euro al kg
    costo = peso_pacco * 1.0

    # Controllo destinazione (reso case-insensitive con .lower())
    if destinazione.strip().lower() != "italia":
        costo += 10.0

    # Se la spedizione è urgente, raddoppia il costo totale accumulato finora
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
    """
    Funzione principale per la gestione dell'input utente
    """
    while True:
        mostra_menu()
        scelta = input("Seleziona un'opzione: ").strip().lower()

        if scelta == 'q':
            print("\nGrazie per aver usato il nostro servizio. Arrivederci!")
            break

        if scelta == '1':
            # 1. Gestione e validazione del peso
            peso = float(input("Inserisci il peso del pacco (in kg): "))
            if peso <= 0:
                print("Il peso deve essere maggiore di zero!")
                continue

            # 2. Gestione destinazione
            dest = input("Inserisci la destinazione (Premi Invio per 'Italia'): ").strip()
            if dest == "":
                dest = "Italia" # Sfrutta il comportamento logico del default

            # 3. Gestione urgenza
            scelta_urgenza = input("La spedizione è urgente? (s/n): ").strip().lower()
            urgente = scelta_urgenza == 's'

            # Calcolo del costo finale usando la funzione
            costo_finale = calcola_spedizione(peso, dest, urgente)

            # Output dei dettagli del preventivo
            print("\n--- Riepilogo Preventivo ---")
            print(f"Dati: {peso} kg | Destinazione: {dest} | Urgente: {'Sì' if urgente else 'No'}")
            print(f"Costo totale: {costo_finale:.2f} €")
            print("----------------------------")
        else:
            print("Opzione non valida!")

# Avvio effettivo del programma
if __name__ == "__main__":
    avvia_programma()