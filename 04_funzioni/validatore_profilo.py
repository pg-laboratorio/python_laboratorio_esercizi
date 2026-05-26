"""
SISTEMA DI VALIDAZIONE REGISTRAZIONE
Autore: @nickname

Composizione di funzioni, ovvero l'utilizzo di funzioni più piccole e specializzate all'interno di una funzione principale per risolvere un problema più complesso.

Isolamento delle responsabilità: Ogni funzione fa una sola cosa e la fa bene (valida_username controlla solo la lunghezza, valida_password cerca solo il numero). Questo rende il codice facile da leggere e da modificare in futuro (ad esempio, se la lunghezza minima dell'username dovesse passare a 8 caratteri, basterà modificare solo la prima funzione).
Il Return Precoce nel ciclo: Nella funzione valida_password, l'istruzione return True interrompe immediatamente sia il ciclo for sia l'intera funzione non appena viene trovata la prima cifra numerica. Non è necessario scorrere tutta la password se il requisito è già stato soddisfatto.
"""

def valida_username(username):
    """
    Ritorna True se la lunghezza è maggiore o uguale a 5, altrimenti False.
    args:
    - username (str): l'username da verificare
    return: bool
    """
    return len(username) >= 5


def valida_password(password):
    """
    Controlla se è presente almeno un carattere numerico.
    args:
    - password (str): la password da verificare
    return: bool
    """
    for carattere in password:
        if carattere.isdigit():
            return True  # Interrompe il ciclo e restituisce True appena trova un numero
    return False  # Se il ciclo finisce senza trovare numeri, restituisce False


def crea_profilo(username, password):
    """
    Invocazione delle due funzioni precedenti (Composizione)
    e stampa del risultato finale.
    return: bool (True se il profilo è creato, False altrimenti)
    """
    username_valido = valida_username(username)
    password_valida = valida_password(password)

    # Controllo finale basato sui valori booleani restituiti
    if username_valido and password_valida:
        print("\n✅ Profilo creato con successo!")
        return True
    else:
        print("\n❌ Dati non validi! Riprova.")
        return False


def mostra_menu():
    """ Mostra i requisiti di sistema """
    print("\n")
    print("--- Registrazione Nuovo Utente ---")
    print("Requisiti:")
    print("- Username: minimo 5 caratteri")
    print("- Password: deve contenere almeno un numero")
    print("- q : chiudere il programma")
    print("\n")


def avvia_registrazione():
    """
    Funzione principale per la gestione dell'input utente e del ciclo di gioco
    """
    while True:
        mostra_menu()

        # 1. Gestione input username + controllo uscita
        input_username = input("Scegli un username: ").strip()
        if input_username.lower() == 'q':
            print("\nChiusura in corso... Arrivederci!")
            break

        # 2. Gestione input password + controllo uscita
        input_password = input("Scegli una password: ").strip()
        if input_password.lower() == 'q':
            print("\nChiusura in corso... Arrivederci!")
            break

        print("\nElaborazione in corso...")

        # 3. Chiamata alla funzione principale e controllo esito
        # Se la registrazione va a buon fine (True), interrompiamo il ciclo
        if crea_profilo(input_username, input_password):
            print("Benvenuto a bordo!")
            break


# Blocco principale del programma (Esecuzione)
if __name__ == "__main__":
    avvia_registrazione()