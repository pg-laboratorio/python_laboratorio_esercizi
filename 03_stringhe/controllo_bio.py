'''
Progetto:

PASSAGGI RISOLUTIVI:
1. Chiedere la stringa della bio all'utente.
2. Misurare la lunghezza con len().
3. Usare un if-else per controllare se supera i 50 caratteri.
4. Calcolare i caratteri in eccesso se necessario.
'''
# Input della bio
biografia = input("Scrivi la tua nuova biografia (max 50 caratteri): ")

# Calcolo lunghezza
lunghezza = len(biografia)
limite_massimo = 50

# Controllo condizioni
if lunghezza <= limite_massimo:
    print("Biografia salvata!")
else:
    # Calcolo dei caratteri extra
    caratteri_extra = lunghezza - limite_massimo
    print(f"Errore: la bio è troppo lunga di {caratteri_extra} caratteri.")