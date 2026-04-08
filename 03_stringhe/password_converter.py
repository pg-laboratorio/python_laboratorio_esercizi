'''
CONSEGNA:
Crea un programma che generi una password così composta:
Chiedi all’utente una parola preferita.
Sostituisci tutte le "a" con “@", le "i" con “!”, le “e” con “&

PROGETTO
OBIETTIVO:
Modificare i caratteri di una password

DATI INPUT:
La parola preferita dell'utente (password)

DATI OUPUT:
La password aggiornata con i caratteri sostituiti

PASSAGGI:
- Chiedo all'utente la parola preferita
- Modifico i caratteri
- Mando in output la nuova password
'''
# Chiedo all'utente la parola preferita
password = input("Inserisci la tua parola preferita: ") #alberi

# Chiedo all'utente la parola preferita
passwrod = password.replace("a","@") #alberi -> @lberi
password = password.replace("i","!") #@lberi -> @lber!
password = password.replace("e","&") #@lber! -> @lb&r!

# Mando in output la nuova password
print(password) #@lb&r!





