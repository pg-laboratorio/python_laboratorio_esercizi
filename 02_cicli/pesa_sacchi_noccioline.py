'''
CONSEGNA:
Una ditta produce sacchetti di noccioline, confezionate con una macchina
automatica. La tolleranza di peso ammessa, è data tra i 40 e 50 grammi.
Sviluppare un programma che visualizza quanti sono i sacchetti il cui peso
rientra nella tolleranza ammessa e i sacchetti totali pesati. Il peso viene dato
in input, l’inserimento termina quando l’utente comunica che non ci sono più
sacchetti da pesare inserendo il valore 0.

PROGETTO:
DATI INPUT:
- peso sacchetto (peso)

DATI OUTPUT:
- i sacchi che rientrano nella tolleranza (sacchi_validi)
- il totale dei sacchi pesati (tot_sacchi)

PASSAGGI:
- Settare le variabili della tolleranza 
- Iniziallizziamo i contatori
- ......
- Visualizzare i sacchetti validi ed il toale dei sacchetti pesati
'''
# NB DI SEGUITO TRAVERETE DUE SOLUZIONI 


### SOLUZIONE A: condizione esplicita

# Settare le variabili della tolleranza 
SOGLIA_MIN = 40
SOGLIA_MAX = 50
# Iniziallizziamo i contatori
sacchi_validi = 0
tot_sacchi = 0

# --- primo input fuori dal ciclo
# serve un valore iniziale alla variabile peso per poter entrare nel while
peso = float(input("Inserisci il peso (g): "))

# ciclo contuinua solo se il peso è diverso da 0
while peso != 0:
    
    #aggiungo uno ai sacchi contati
    tot_sacchi +=1 # è come dire tot_sacchi = tot_sacchi + 1
    
    # verifico la tolleranza
    if peso >= SOGLIA_MIN and peso <= SOGLIA_MAX:
        #aggiungo uno ai sacchi validi
        sacchi_validi += 1 # è come dire sacchi_validi = sacchi_validi + 1
        print("Ok sacchetto valido!")
    else:
        print("Non valido, fuori dalla soglia!")
    
    # --- secondo input in fondo al ciclo
    # fondamentale chiedere il prossimo valore da inserire per ricominciare il giro
    # se qui l'utente insersce 0 il ciclo termina perchè la condizione non è più verificata
    peso = float(input("Inserisci il peso (g): "))

# Visualizzare i sacchetti validi ed il toale dei sacchetti pesati
print(f"Totale dei sacchetti pesati: {tot_sacchi}")
print(f"Sacchetti validi: {sacchi_validi}")
print(f"Grazie!")


### SOLUZIONE B: condizione nascosta nel cilo while

# Settare le variabili della tolleranza 
SOGLIA_MIN = 40
SOGLIA_MAX = 50
# Iniziallizziamo i contatori
sacchi_validi = 0
tot_sacchi = 0

# scrivo l'istruzione input una sola volta,
# ma il controllo della condizione è "nascosto" nel ciclo e non nell'instestazione del while
while True:
    # istruzione input in questo caso me ne basta una! Logica più naturale (azione->controllo->azione)
    peso = float(input("Inserisci il peso (g): "))
    
    # controllo che se il peso è 0 allora interrompo il ciclo
    if peso == 0:
        break # istruzione per uscire dal ciclo, il resto del codice del ciclo non viene eseguito
    
    #aggiungo uno ai sacchi contati
    tot_sacchi +=1 # è come dire tot_sacchi = tot_sacchi + 1
    
    # verifico la tolleranza
    if peso >= SOGLIA_MIN and peso <= SOGLIA_MAX:
        #aggiungo uno ai sacchi validi
        sacchi_validi += 1 # è come dire sacchi_validi = sacchi_validi + 1
        print("Ok sacchetto valido!")
    else:
        print("Non valido, fuori dalla soglia!")

# Visualizzare i sacchetti validi ed il toale dei sacchetti pesati
print(f"Totale dei sacchetti pesati: {tot_sacchi}")
print(f"Sacchetti validi: {sacchi_validi}")
print(f"Grazie!")