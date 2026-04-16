'''
Scrivi un programma che: Chieda una frase all’utente. Conti quante vocali sono presenti. Stampi: "La frase contiene [X] vocali”.

PROGETTO
OBIETTIVO:
Contare vocali in una frase

DATI INPUT:
- Frase dall'utente (frase)

DATI OUTPUT:
- numero vocali nella frase (conteggio_vocali)

PASSAGGI:
- Imposto conteggio_vocali
- Chiedo una frase all'utente
- ....
- Stampo il conteggio_vocali
'''
# Imposto conteggio_vocali
conteggio_vocali = 0
# Chiedo una frase all'utente
frase = input("Inserisci una frase: ")
# Imposto la variabile vocali
vocali = "aeiouAEIOUàèìòù"
# Ciclo per contare le vocali nella frase
for i in frase:
    if i in vocali:
        conteggio_vocali += 1
# stampo conteggio_vocali
print(f"Le vocali nella frase sono {conteggio_vocali}")





