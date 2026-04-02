'''
CONSEGNA:
Vogliamo riempire una vasca da bagno che ha una capienza massima di 50 litri.
L'utente aggiunge secchi d'acqua (di quanti litri vuole)
finché la vasca non è piena o trabocca.
PROGETTO
RIASSUNTO: Aggiungi secchi d'acqua ad un vasca finchè non trabocca (50 l)

DATI INPUT:
- litri d'acqua aggiunti (secchio)

DATI OUPUT:
- livello capieza (livello_acqua)

PASSAGGI:
- settiamo la capienza massima a 50 (CAPIENZA_MAX)
- settiamo livello acqua iniziale a 0 (livello_acqua)
- avvio ciclo while: finchè livello_acqua < CAPIENZA_MAX
    - chiediamo in input quanti litri vuole versare
    - aggiorniamo il livello_acqua
    - stampiamo livello_acqua
- avviso fine programma
'''
# settiamo la capienza massima a 50 (CAPIENZA_MAX)
CAPIENZA_MAX = 50
# settiamo livello acqua iniziale a 0 (livello_acqua)
livello_acqua = 0

# avvio ciclo while: finchè livello_acqua < CAPIENZA_MAX
while livello_acqua < CAPIENZA_MAX:
    # chiediamo in input quanti litri vuole versare
    secchio = float(input("Inserisci i litri aggiunti: "))
    # aggiorniamo il livello_acqua
    livello_acqua = livello_acqua + secchio
    # stampiamo livello_acqua
    print(f"La vasca contiene {livello_acqua:.2f} l")

# avviso fine programma
print("La vasca ha superato la capienza massima")