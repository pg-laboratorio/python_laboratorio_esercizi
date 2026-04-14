'''
Progetto:

PASSAGGI RISOLUTIVI
1. Chiedere all'utente una frase.
2. Usare title() per mettere l'iniziale maiuscola a ogni parola.
3. Usare replace() per eliminare gli spazi.
4. Concatenare il "#" all'inizio.
'''
# Input dell'utente
frase = input("Inserisci la frase per il tuo post: ")

# Formattazione
frase_titolo = frase.title() # Es: "Oggi C'è Il Sole"
frase_senza_spazi = frase_titolo.replace(" ", "") # Es: "OggiC'èIlSole"

# Creazione hashtag finale
hashtag = "#" + frase_senza_spazi

# Output
print(f"Il tuo hashtag generato è: {hashtag}")