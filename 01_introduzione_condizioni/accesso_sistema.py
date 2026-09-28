"""
PROGETTO
CONSEGNA:
Un amministratore di sistema sta configurando un accesso sicuro.
Solo gli utenti con un livello di sicurezza superiore a 5 possono accedere al server critico.
Il programma chiede il livello dell'utente e decide se concedere l'accesso.

DATI INPUT:
- Livello dell'utente (livello_utente)

DATI OUTPUT:
- Messaggio "Accesso consentito" oppure "Accesso negato"

ALTRE VARIABILI:
- COSTANTE livello di sicurezza richiesto = 5 (LIVELLO_ACCESSO)

PASSAGGI RISOLUTIVI:
- impostiamo la costante LIVELLO_ACCESSO = 5
- chiediamo in input livello_utente
- se livello_utente > LIVELLO_ACCESSO allora
    mandiamo in output "Accesso consentito"
- altrimenti
    mandiamo in output "Accesso negato"
"""
# - impostiamo la costante LIVELLO_ACCESSO = 5
LIVELLO_ACCESSO = 5

# - chiediamo in input livello_utente
livello_utente = int(input("Inserisci il livello utente: "))

# - se livello_utente > LIVELLO_ACCESSO allora "Accesso consentito"
# NB: usiamo la costante e non il numero 5 scritto a mano: se domani il livello
#     richiesto diventa 7, basta cambiare UNA sola riga in cima al programma.
if livello_utente > LIVELLO_ACCESSO:
    print("Accesso consentito")
# - altrimenti "Accesso negato"
else:
    print("Accesso negato")
