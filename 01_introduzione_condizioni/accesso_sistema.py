'''
Progetto
Consegna:
Un amministratore di sistema sta configurando un accesso sicuro.

Solo gli utenti con un livello di sicurezza superiore a 5 possono accedere al server critico.

Il programma chiede il livello dell'utente e decide se concedere l'accesso.

Dati input:
livello dell'utente (livello_utente)

Dati output:
accesso consentito o negato

altre veriabili:
COSTANTE: livello sicureza accesso = 5

Passaggi:
- settiamo le variabili LIVELLO_ACCESSO = 5
- chiediamo il livello dell'utente
- se livello_utente > 5 allora
    mandiamo in output accessoConsentito
- altrimenti
    mandiamo in output accesso_negato
'''

# - settiamo le variabili LIVELLO_ACCESSO = 5
LIVELLO_ACCESSO = 5
# - chiediamo il livello dell'utente
livello_utente = int(input("Inserisci il livello utente: "))
# - se livello_utente > 5 allora
     #mandiamo in output accessoConsentito
if livello_utente > 5:
    print ("Accesso consentito")
# - altrimenti
    #mandiamo in output accessoNegato
else:
    print ("Accesso negato")