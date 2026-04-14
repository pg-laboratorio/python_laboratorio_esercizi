'''
CONSEGNA:
Scrivi un programma che chieda all’utente l’username e la password, e mostri il messaggio “Accesso consentito” nel caso che l’user sia “admin” e la password “secure123".

OBIETTIVO: stampi accesso consentito se nome utente e psw corrispondono

DATI INPUT:
- username utente (user)
- psw utente (psw)

DATI OUTPUT
- messaggio accesso consentito

PASSAGGI:
- settare la veriabili di accesso
- chiado all'utente username e psw
- condizione di accesso
    se vero stampo accesso consentito
    se falso messaggio di errore
'''
# settare la veriabili di accesso
user_corretto = 'admin'
psw_corretta = 'secure123'
# chiado all'utente username e psw
user = input("Inserisci username: ")
psw = input("Inserisci psw: ")
# condizione di accesso
if user == user_corretto and psw == psw_corretta:
    print("Accesso consentito")
else:
    print("Credenziali non corrette")

