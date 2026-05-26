"""
SISTEMA DI VALIDAZIONE REGISTRAZIONE
Autore: @nickname

Composizione di funzioni, ovvero l'utilizzo di funzioni più piccole e specializzate all'interno di una funzione principale per risolvere un problema più complesso.

Isolamento delle responsabilità: Ogni funzione fa una sola cosa e la fa bene (valida_username controlla solo la lunghezza, valida_password cerca solo il numero). Questo rende il codice facile da leggere e da modificare in futuro (ad esempio, se la lunghezza minima dell'username dovesse passare a 8 caratteri, basterà modificare solo la prima funzione).
Il Return Precoce nel ciclo: Nella funzione valida_password, l'istruzione return True interrompe immediatamente sia il ciclo for sia l'intera funzione non appena viene trovata la prima cifra numerica. Non è necessario scorrere tutta la password se il requisito è già stato soddisfatto.
"""
def valida_username(username):
    # Ritorna True se la lunghezza è maggiore o uguale a 5, altrimenti False
    return len(username) >= 5


def valida_password(password):
    # Controlla se è presente almeno un carattere numerico
    for carattere in password:
        if carattere.isdigit():
            return True  # Interrompe il ciclo e restituisce True appena trova un numero
    return False  # Se il ciclo finisce senza trovare numeri, restituisce False


def crea_profilo(username, password):
    # Invocazione delle due funzioni precedenti (Composizione)
    username_valido = valida_username(username)
    password_valida = valida_password(password)

    # Controllo finale basato sui valori booleani restituiti
    if username_valido and password_valida:
        print("Profilo creato con successo")
    else:
        print("Dati non validi")


# Blocco principale del programma (Esecuzione)
if __name__ == "__main__":
    print("--- Registrazione Nuovo Utente ---")
    input_username = input("Scegli un username (minimo 5 caratteri): ")
    input_password = input("Scegli una password (deve contenere almeno un numero): ")

    print("\nElaborazione in corso...")
    # Chiamata alla funzione principale
    crea_profilo(input_username, input_password)