'''
CONSEGNA:
Un sistema di riscaldamento si attiva quando la temperatura media di tre stanze è inferiore a un valore impostato.
Il costo energetico è di 20 € all’ora.
Se la temperatura media è inferiore di almeno 5°C rispetto al limite, il costo orario aumenta del 25% (extra consumo).
Implementa un programma che calcoli il costo totale basandosi su temperature, limite e ore di funzionamento.
DATI INPUT:
-numero_ore
-temperatura_stanza1/2/3
-temperatura_limite

DATI OUTPUT:
-costo_totale

ALTRE VARIABILI:
-costo_energetico

PASSAGGI:
-impostare la variabile costo_energetico = 20
-impostare i 5 input: numero_ore, temperatura_stanza1/2/3, temperatura_limite
-calcolo della temperatura_media
-se temperatura_media < temperatura_limite
    -se temperatura_media < temperatura_limite - 5
        -allora aggiungere 25% in più al costo_totale
    -calcolo costo_totale
    - stampa il costo_totale con il 25% in più
-altrimenti
    -stampa "riscaldamento spento"
'''
#impostare la variabile costo_energetico = 20
costo_energetico = 20

#impostare i 5 input: numero_ore, temperatura_stanza1/2/3, temperatura_limite
numero_ore = int(input("Inserire numero ore: "))
temperatura_stanza1 = float(input("Inserire temperatura della stanza 1: "))
temperatura_stanza2 = float(input("Inserire temperatura della stanza 2: "))
temperatura_stanza3 = float(input("Inserire temperatura della stanza 3: "))
temperatura_limite = float(input("Inserire temperatura limite: "))

#calcolo della temperatura_media
temperatura_media = (temperatura_stanza1 + temperatura_stanza2 +temperatura_stanza3)/3
print(f"La temperatura media è {temperatura_media:.2f} °C")

#se temperatura_media < temperatura_limite
if temperatura_media < temperatura_limite:
    #-se temperatura_media < temperatura_limite - 5
    print("sistema acceso")
    if temperatura_media < temperatura_limite - 5:
        #-allora aggiungere 25% in più al costo_totale
        costo_energetico = costo_energetico + costo_energetico * 0.25
    #calcolo costo_totale
    costo_totale = numero_ore * costo_energetico
    print(f"Il costo totale è di {costo_totale:.2f}€")

# -altrimenti stampa "riscaldamento spento"
else:
    print("sistema spento")
    costo_totale = 0
    print(f"Il costo totale è di {costo_totale:.2f}€")



